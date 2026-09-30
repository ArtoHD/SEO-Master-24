#!/usr/bin/env python3
"""
SEO-Master-24 — Technical & On-Page SEO Auditor
Engineered by 24 Software (https://24software.com.tr) & Harutyun Arto Davulciyan (https://davulciyan.com)

Performs deep technical on-page SEO analysis with zero external dependencies.
"""

import sys
import json
import re
import urllib.request
import urllib.error
from html.parser import HTMLParser

class SEOHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta_tags = []
        self.canonical = None
        self.hreflangs = []
        self.h1_tags = []
        self.h2_tags = []
        self.h3_tags = []
        self.current_tag = None
        self.current_text = []
        self.images = []
        self.json_ld = []
        self.in_json_ld = False
        self.json_ld_buffer = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self.current_tag = tag

        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            self.meta_tags.append(attr_dict)
        elif tag == "link":
            rel = attr_dict.get("rel", "").lower()
            if rel == "canonical":
                self.canonical = attr_dict.get("href")
            elif rel == "alternate" and "hreflang" in attr_dict:
                self.hreflangs.append({
                    "hreflang": attr_dict.get("hreflang"),
                    "href": attr_dict.get("href")
                })
        elif tag in ("h1", "h2", "h3"):
            self.current_text = []
        elif tag == "img":
            self.images.append({
                "src": attr_dict.get("src", ""),
                "alt": attr_dict.get("alt")
            })
        elif tag == "script" and attr_dict.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.json_ld_buffer = []

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            text = "".join(self.current_text).strip()
            if text:
                self.h1_tags.append(text)
        elif tag == "h2":
            text = "".join(self.current_text).strip()
            if text:
                self.h2_tags.append(text)
        elif tag == "h3":
            text = "".join(self.current_text).strip()
            if text:
                self.h3_tags.append(text)
        elif tag == "script" and self.in_json_ld:
            self.in_json_ld = False
            raw = "".join(self.json_ld_buffer).strip()
            if raw:
                try:
                    self.json_ld.append(json.loads(raw))
                except Exception:
                    self.json_ld.append({"raw_error": raw[:200]})
        self.current_tag = None

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_json_ld:
            self.json_ld_buffer.append(data)
        elif self.current_tag in ("h1", "h2", "h3"):
            self.current_text.append(data)

def audit_url(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; SEO-Master-24-Bot/1.0; +https://24software.com.tr)"
    }
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            content_type = resp.headers.get("Content-Type", "")
            hsts = resp.headers.get("Strict-Transport-Security")
            x_robots = resp.headers.get("X-Robots-Tag")
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}", "url": url}
    except Exception as e:
        return {"error": str(e), "url": url}

    parser = SEOHTMLParser()
    parser.feed(html)

    # Extract Meta fields
    meta_desc = None
    robots_meta = None
    viewport = None
    og = {}
    twitter = {}

    for m in parser.meta_tags:
        name = m.get("name", "").lower()
        prop = m.get("property", "").lower()
        content = m.get("content", "")

        if name == "description":
            meta_desc = content
        elif name == "robots":
            robots_meta = content
        elif name == "viewport":
            viewport = content
        elif prop.startswith("og:"):
            og[prop[3:]] = content
        elif name.startswith("twitter:"):
            twitter[name[8:]] = content

    # Calculate Score & Issues
    score = 100
    issues = []
    passes = []

    # Title check
    title = parser.title.strip()
    if not title:
        score -= 20
        issues.append({"severity": "high", "rule": "title_missing", "msg": "Page is missing a <title> tag."})
    else:
        passes.append(f"Title present ({len(title)} chars): '{title[:60]}...'")
        if len(title) < 30 or len(title) > 65:
            score -= 5
            issues.append({"severity": "medium", "rule": "title_length", "msg": f"Title length ({len(title)} chars) should be between 30 and 65 chars."})

    # Meta Description check
    if not meta_desc:
        score -= 15
        issues.append({"severity": "high", "rule": "description_missing", "msg": "Page is missing a meta description."})
    else:
        passes.append(f"Meta description present ({len(meta_desc)} chars)")
        if len(meta_desc) < 100 or len(meta_desc) > 165:
            score -= 4
            issues.append({"severity": "low", "rule": "description_length", "msg": f"Meta description length ({len(meta_desc)} chars) should be between 100 and 165 chars."})

    # H1 check
    if not parser.h1_tags:
        score -= 20
        issues.append({"severity": "high", "rule": "h1_missing", "msg": "Page has no <h1> heading."})
    elif len(parser.h1_tags) > 1:
        score -= 5
        issues.append({"severity": "medium", "rule": "h1_multiple", "msg": f"Multiple <h1> tags found ({len(parser.h1_tags)}). Recommended: exactly one <h1> per page."})
    else:
        passes.append(f"Single <h1> present: '{parser.h1_tags[0][:60]}'")

    # Canonical check
    if not parser.canonical:
        score -= 10
        issues.append({"severity": "medium", "rule": "canonical_missing", "msg": "Missing rel='canonical' tag."})
    else:
        passes.append(f"Canonical URL: {parser.canonical}")
        if parser.canonical != final_url:
            score -= 5
            issues.append({"severity": "medium", "rule": "canonical_mismatch", "msg": f"Canonical target ({parser.canonical}) differs from requested/final URL ({final_url})."})

    # HSTS check
    if hsts:
        passes.append(f"HSTS enabled: {hsts}")
    else:
        score -= 5
        issues.append({"severity": "medium", "rule": "hsts_missing", "msg": "Strict-Transport-Security header is missing."})

    # OpenGraph check
    if og.get("title") and og.get("image"):
        passes.append("OpenGraph tags (title, image) present.")
    else:
        missing = []
        if not og.get("title"): missing.append("og:title")
        if not og.get("image"): missing.append("og:image")
        score -= 5
        issues.append({"severity": "low", "rule": "og_incomplete", "msg": f"Missing OpenGraph fields: {', '.join(missing)}"})

    # Image Alt checks
    images_without_alt = [img for img in parser.images if not img.get("alt")]
    if images_without_alt:
        score -= min(10, len(images_without_alt) * 2)
        issues.append({"severity": "low", "rule": "img_alt_missing", "msg": f"{len(images_without_alt)} of {len(parser.images)} images missing alt text."})
    elif parser.images:
        passes.append(f"All {len(parser.images)} images have alt text.")

    # Structured Data
    def extract_types(obj):
        found = []
        if isinstance(obj, dict):
            t = obj.get("@type")
            if t:
                if isinstance(t, list):
                    found.extend([str(x) for x in t])
                else:
                    found.append(str(t))
            if "@graph" in obj:
                found.extend(extract_types(obj["@graph"]))
        elif isinstance(obj, list):
            for item in obj:
                found.extend(extract_types(item))
        return found

    schema_types = []
    for item in parser.json_ld:
        schema_types.extend(extract_types(item))
    
    # Deduplicate while preserving order
    schema_types = list(dict.fromkeys(schema_types))

    if schema_types:
        passes.append(f"JSON-LD Schema detected: {', '.join(schema_types)}")
    else:
        score -= 10
        issues.append({"severity": "medium", "rule": "schema_missing", "msg": "No JSON-LD structured data detected on page."})

    return {
        "url": final_url,
        "status_code": status,
        "score": max(0, score),
        "title": title,
        "meta_description": meta_desc,
        "h1": parser.h1_tags,
        "h2_count": len(parser.h2_tags),
        "canonical": parser.canonical,
        "hreflang_count": len(parser.hreflangs),
        "json_ld_types": schema_types,
        "security": {
            "hsts": bool(hsts),
            "hsts_header": hsts
        },
        "issues": issues,
        "passes": passes,
        "signature": {
            "engine": "SEO-Master-24",
            "developer": "24 Software (https://24software.com.tr)",
            "author": "Harutyun Arto Davulciyan (https://davulciyan.com)"
        }
    }

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("SEO-Master-24: Technical On-Page SEO Auditor")
        print("Usage: python3 seo_audit.py <URL>")
        print("Example: python3 seo_audit.py https://davulciyan.com/tr")
        sys.exit(0)

    target_url = sys.argv[1]
    res = audit_url(target_url)
    print(json.dumps(res, indent=2, ensure_ascii=False))
