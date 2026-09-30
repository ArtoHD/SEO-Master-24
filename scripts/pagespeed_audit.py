#!/usr/bin/env python3
"""
SEO-Master-24: Google PageSpeed Insights & Core Web Vitals Optimizer
Engineered by 24 Software (https://24software.com.tr) & Harutyun Arto Davulciyan (https://davulciyan.com)

Multi-mode Performance Engine:
- Fast Mode (--fast): Zero-dependency HTML & Network CWV heuristics (TTFB, render-blocking JS/CSS, CLS image hazards, font preloads, payload size)
- Lab Mode (--lighthouse): Headless Lighthouse CLI execution for exact 0-100 scores (Performance, Accessibility, Best Practices, SEO) + LCP, INP/TBT, CLS
- Cloud Mode (--api): Google PageSpeed Insights v5 REST API client with optional API key
"""

import sys
import os
import json
import time
import subprocess
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class PerformanceHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.render_blocking_scripts = []
        self.async_defer_scripts = []
        self.stylesheets = []
        self.images_without_dimensions = []
        self.images_with_dimensions = []
        self.preconnect_preloads = []
        self.font_preloads = []
        self.inline_styles_count = 0
        self.inline_scripts_count = 0

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        
        if tag == "script":
            src = attr_dict.get("src")
            if src:
                is_async = "async" in attr_dict
                is_defer = "defer" in attr_dict
                is_module = attr_dict.get("type") == "module"
                if is_async or is_defer or is_module:
                    self.async_defer_scripts.append(src)
                else:
                    self.render_blocking_scripts.append(src)
            else:
                self.inline_scripts_count += 1

        elif tag == "link":
            rel = attr_dict.get("rel", "").lower()
            href = attr_dict.get("href", "")
            as_type = attr_dict.get("as", "").lower()
            
            if rel == "stylesheet":
                self.stylesheets.append(href)
            elif rel in ("preload", "preconnect", "dns-prefetch"):
                self.preconnect_preloads.append({"rel": rel, "href": href, "as": as_type})
                if as_type == "font":
                    self.font_preloads.append(href)

        elif tag == "style":
            self.inline_styles_count += 1

        elif tag == "img":
            src = attr_dict.get("src", attr_dict.get("data-src", ""))
            width = attr_dict.get("width")
            height = attr_dict.get("height")
            has_dimensions = bool(width and height)
            
            # Check style attribute for aspect-ratio or explicit dimensions
            style = attr_dict.get("style", "").lower()
            if "aspect-ratio" in style or ("width" in style and "height" in style):
                has_dimensions = True

            if has_dimensions:
                self.images_with_dimensions.append(src)
            else:
                self.images_without_dimensions.append({
                    "src": src,
                    "loading": attr_dict.get("loading", "eager"),
                    "fetchpriority": attr_dict.get("fetchpriority", "auto")
                })

import gzip

def run_fast_heuristics(url):
    """Zero-dependency instant on-page Core Web Vitals and PageSpeed heuristics audit."""
    start_time = time.time()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 SEO-Master-24",
            "Accept-Encoding": "gzip, deflate"
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            ttfb_ms = round((time.time() - start_time) * 1000, 2)
            status_code = resp.status
            content = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            content_encoding = headers.get("content-encoding", "").lower()
            
            if "gzip" in content_encoding:
                try:
                    html_text = gzip.decompress(content).decode("utf-8", errors="replace")
                except Exception:
                    html_text = content.decode("utf-8", errors="replace")
            elif "deflate" in content_encoding:
                try:
                    import zlib
                    html_text = zlib.decompress(content).decode("utf-8", errors="replace")
                except Exception:
                    html_text = content.decode("utf-8", errors="replace")
            else:
                html_text = content.decode("utf-8", errors="replace")
            content_length = len(content)
    except Exception as e:
        return {"error": f"Failed to fetch {url}: {e}", "url": url}

    parser = PerformanceHTMLParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass

    # Heuristic scoring (0-100)
    score = 100
    deductions = []

    # TTFB evaluation
    if ttfb_ms > 800:
        score -= 20
        deductions.append(f"High TTFB ({ttfb_ms}ms > 800ms) - Server response is slow")
    elif ttfb_ms > 400:
        score -= 10
        deductions.append(f"Moderate TTFB ({ttfb_ms}ms > 400ms)")

    # Render-blocking scripts
    rb_count = len(parser.render_blocking_scripts)
    if rb_count > 0:
        penalty = min(25, rb_count * 8)
        score -= penalty
        deductions.append(f"{rb_count} render-blocking <script> tags without async/defer/module")

    # Render-blocking external stylesheets
    css_count = len(parser.stylesheets)
    if css_count > 4:
        score -= 10
        deductions.append(f"{css_count} external stylesheets may delay first paint")

    # Images missing dimensions (CLS hazards)
    missing_dim_count = len(parser.images_without_dimensions)
    if missing_dim_count > 0:
        penalty = min(20, missing_dim_count * 5)
        score -= penalty
        deductions.append(f"{missing_dim_count} images missing explicit width/height or aspect-ratio (CLS risk)")

    # Cache-Control validation
    cache_control = headers.get("cache-control", "").lower()
    if not cache_control:
        score -= 10
        deductions.append("Missing Cache-Control header on HTML document")

    # Compression check
    content_encoding = headers.get("content-encoding", "").lower()
    is_compressed = any(c in content_encoding for c in ["gzip", "br", "deflate"])

    score = max(0, min(100, score))

    cwv_predictions = {
        "lcp_risk": "Low" if (ttfb_ms < 500 and rb_count <= 1) else ("Medium" if ttfb_ms < 1000 else "High"),
        "cls_risk": "High" if missing_dim_count > 3 else ("Medium" if missing_dim_count > 0 else "Low"),
        "tbt_risk": "High" if rb_count > 3 else ("Medium" if rb_count > 0 else "Low")
    }

    return {
        "mode": "Fast Heuristics (Zero-Dependency)",
        "target": url,
        "status_code": status_code,
        "estimated_performance_score": score,
        "ttfb_ms": ttfb_ms,
        "html_payload_bytes": content_length,
        "compression": {
            "is_compressed": is_compressed,
            "encoding": content_encoding or "none"
        },
        "critical_rendering_path": {
            "render_blocking_scripts_count": rb_count,
            "render_blocking_scripts": parser.render_blocking_scripts[:5],
            "async_defer_scripts_count": len(parser.async_defer_scripts),
            "external_stylesheets_count": css_count,
            "external_stylesheets": parser.stylesheets[:5],
            "inline_styles_count": parser.inline_styles_count,
            "font_preloads_count": len(parser.font_preloads)
        },
        "cls_stability": {
            "images_with_dimensions": len(parser.images_with_dimensions),
            "images_missing_dimensions": missing_dim_count,
            "hazardous_images_sample": [img["src"] for img in parser.images_without_dimensions[:5]]
        },
        "cwv_risk_matrix": cwv_predictions,
        "deductions_and_opportunities": deductions,
        "recommendations": [
            "Add 'defer', 'async', or 'type=\"module\"' to all non-critical scripts." if rb_count > 0 else None,
            "Specify explicit width and height attributes or CSS 'aspect-ratio' on all <img> tags to avoid CLS." if missing_dim_count > 0 else None,
            "Preload hero LCP image via <link rel=\"preload\" as=\"image\" href=\"...\" fetchpriority=\"high\">.",
            "Use 'font-display: swap' on custom web fonts to prevent invisible text during font loading (FOIT).",
            "Leverage HTTP/2 or HTTP/3 and edge CDN caching with immutable headers for static assets."
        ],
        "signature": {
            "framework": "SEO-Master-24 Quad-Vector Engine",
            "developer": "24 Software (https://24software.com.tr)",
            "author": "Harutyun Arto Davulciyan (https://davulciyan.com)"
        }
    }

def run_lighthouse_audit(url, strategy="mobile"):
    """Run local headless Lighthouse audit via npx."""
    cmd = [
        "npx", "-y", "lighthouse", url,
        "--output=json",
        "--output-path=stdout",
        "--chrome-flags=--headless --no-sandbox --disable-gpu",
        "--only-categories=performance,accessibility,best-practices,seo"
    ]
    if strategy == "desktop":
        cmd.append("--preset=desktop")

    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=120)
        if res.returncode != 0 and not res.stdout.strip():
            return {"error": f"Lighthouse execution failed: {res.stderr[:300]}", "fallback": run_fast_heuristics(url)}
        
        data = json.loads(res.stdout)
        categories = data.get("categories", {})
        audits = data.get("audits", {})

        def get_score(cat):
            val = categories.get(cat, {}).get("score")
            return round(val * 100) if val is not None else 0

        # Core Web Vitals extraction
        lcp = audits.get("largest-contentful-paint", {})
        cls = audits.get("cumulative-layout-shift", {})
        tbt = audits.get("total-blocking-time", {})
        fcp = audits.get("first-contentful-paint", {})
        si = audits.get("speed-index", {})
        inp = audits.get("interactive", {})

        # Top performance opportunities
        opportunities = []
        opp_keys = [
            "render-blocking-resources", "unused-javascript", "unused-css-rules",
            "offscreen-images", "modern-image-formats", "uses-optimized-images",
            "server-response-time", "uses-text-compression", "efficient-animated-content"
        ]
        for key in opp_keys:
            audit = audits.get(key, {})
            if audit.get("score") is not None and audit.get("score") < 0.9:
                opportunities.append({
                    "id": key,
                    "title": audit.get("title"),
                    "display_value": audit.get("displayValue", ""),
                    "score": round((audit.get("score") or 0) * 100)
                })

        return {
            "mode": f"Lighthouse Lab Audit ({strategy.upper()})",
            "target": url,
            "scores": {
                "performance": get_score("performance"),
                "accessibility": get_score("accessibility"),
                "best_practices": get_score("best-practices"),
                "seo": get_score("seo")
            },
            "core_web_vitals": {
                "lcp": {
                    "value": lcp.get("displayValue", "N/A"),
                    "numeric_value_ms": round(lcp.get("numericValue", 0), 1),
                    "score": round((lcp.get("score") or 0) * 100)
                },
                "cls": {
                    "value": cls.get("displayValue", "N/A"),
                    "numeric_value": round(cls.get("numericValue", 0), 4),
                    "score": round((cls.get("score") or 0) * 100)
                },
                "tbt": {
                    "value": tbt.get("displayValue", "N/A"),
                    "numeric_value_ms": round(tbt.get("numericValue", 0), 1),
                    "score": round((tbt.get("score") or 0) * 100)
                },
                "fcp": {
                    "value": fcp.get("displayValue", "N/A"),
                    "numeric_value_ms": round(fcp.get("numericValue", 0), 1),
                    "score": round((fcp.get("score") or 0) * 100)
                },
                "speed_index": {
                    "value": si.get("displayValue", "N/A"),
                    "numeric_value_ms": round(si.get("numericValue", 0), 1),
                    "score": round((si.get("score") or 0) * 100)
                }
            },
            "top_bottlenecks": opportunities[:6],
            "signature": {
                "framework": "SEO-Master-24 Quad-Vector Engine",
                "developer": "24 Software (https://24software.com.tr)",
                "author": "Harutyun Arto Davulciyan (https://davulciyan.com)"
            }
        }
    except Exception as e:
        return {"error": f"Lighthouse execution error: {e}", "fallback": run_fast_heuristics(url)}

def run_pagespeed_api(url, strategy="mobile", api_key=None):
    """Query official Google PageSpeed Insights REST API."""
    params = {
        "url": url,
        "strategy": strategy,
        "category": ["performance", "accessibility", "best-practices", "seo"]
    }
    if api_key:
        params["key"] = api_key

    query_str = urllib.parse.urlencode(params, doseq=True)
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?{query_str}"
    
    req = urllib.request.Request(api_url, headers={"User-Agent": "SEO-Master-24-PSI"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            lighthouse = data.get("lighthouseResult", {})
            cats = lighthouse.get("categories", {})
            audits = lighthouse.get("audits", {})

            def get_score(cat):
                val = cats.get(cat, {}).get("score")
                return round(val * 100) if val is not None else 0

            return {
                "mode": f"Google PageSpeed Insights API ({strategy.upper()})",
                "target": url,
                "scores": {
                    "performance": get_score("performance"),
                    "accessibility": get_score("accessibility"),
                    "best_practices": get_score("best-practices"),
                    "seo": get_score("seo")
                },
                "core_web_vitals": {
                    "lcp": audits.get("largest-contentful-paint", {}).get("displayValue", "N/A"),
                    "cls": audits.get("cumulative-layout-shift", {}).get("displayValue", "N/A"),
                    "tbt": audits.get("total-blocking-time", {}).get("displayValue", "N/A"),
                    "fcp": audits.get("first-contentful-paint", {}).get("displayValue", "N/A"),
                    "speed_index": audits.get("speed-index", {}).get("displayValue", "N/A")
                },
                "signature": {
                    "framework": "SEO-Master-24 Quad-Vector Engine",
                    "developer": "24 Software (https://24software.com.tr)",
                    "author": "Harutyun Arto Davulciyan (https://davulciyan.com)"
                }
            }
    except Exception as e:
        return {"error": f"PageSpeed API request failed: {e}", "fallback": run_fast_heuristics(url)}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("SEO-Master-24: Google PageSpeed Insights & Core Web Vitals Optimizer")
        print("Usage:")
        print("  python3 pagespeed_audit.py <URL> [options]")
        print("")
        print("Options:")
        print("  --fast          Run instant zero-dependency CWV heuristics audit (default)")
        print("  --lighthouse    Run full local Lighthouse audit via npx (mobile)")
        print("  --desktop       Run Lighthouse audit in desktop mode")
        print("  --api           Query Google PageSpeed Insights REST API (set PAGESPEED_API_KEY if available)")
        print("")
        print("Examples:")
        print("  python3 pagespeed_audit.py https://davulciyan.com/tr --fast")
        print("  python3 pagespeed_audit.py https://davulciyan.com/tr --lighthouse")
        sys.exit(0)

    target_url = sys.argv[1]
    args = sys.argv[2:]

    # Clean recommendation list helper
    def clean_output(res):
        if "recommendations" in res:
            res["recommendations"] = [r for r in res["recommendations"] if r is not None]
        return res

    if "--lighthouse" in args:
        strategy = "desktop" if "--desktop" in args else "mobile"
        report = run_lighthouse_audit(target_url, strategy=strategy)
    elif "--api" in args:
        strategy = "desktop" if "--desktop" in args else "mobile"
        api_key = os.environ.get("PAGESPEED_API_KEY")
        report = run_pagespeed_api(target_url, strategy=strategy, api_key=api_key)
    else:
        # Fast mode by default or if --fast specified
        report = run_fast_heuristics(target_url)

    clean_output(report)
    print(json.dumps(report, indent=2, ensure_ascii=False))
