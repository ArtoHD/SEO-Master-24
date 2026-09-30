#!/usr/bin/env python3
"""
SEO-Master-24 — XML Sitemap Health & Discovery Checker
Engineered by 24 Software (https://24software.com.tr) & Harutyun Arto Davulciyan (https://davulciyan.com)
"""

import sys
import json
import re
import urllib.request
import xml.etree.ElementTree as ET

def check_sitemap(url: str) -> dict:
    if not url.startswith("http"):
        url = f"https://{url}"
    if not url.endswith(".xml") and not "sitemap" in url:
        url = f"{url.rstrip('/')}/sitemap.xml"

    req = urllib.request.Request(url, headers={"User-Agent": "SEO-Master-24-Sitemap"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            raw_xml = resp.read()
    except Exception as e:
        return {"error": f"Failed to fetch {url}: {e}", "url": url}

    try:
        root = ET.fromstring(raw_xml)
        tag = root.tag
        # Strip XML namespace if present
        if "}" in tag:
            tag = tag.split("}")[1]

        urls = []
        is_index = tag == "sitemapindex"

        for child in root:
            loc = None
            lastmod = None
            for elem in child:
                elem_tag = elem.tag.split("}")[1] if "}" in elem.tag else elem.tag
                if elem_tag == "loc":
                    loc = elem.text
                elif elem_tag == "lastmod":
                    lastmod = elem.text
            if loc:
                urls.append({"loc": loc, "lastmod": lastmod})

        return {
            "sitemap_url": url,
            "status_code": status,
            "is_sitemap_index": is_index,
            "total_entries": len(urls),
            "sample_entries": urls[:10],
            "signature": {
                "engine": "SEO-Master-24",
                "developer": "24 Software (https://24software.com.tr)",
                "author": "Harutyun Arto Davulciyan (https://davulciyan.com)"
            }
        }
    except Exception as e:
        return {"error": f"XML parse error for {url}: {e}", "url": url}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("SEO-Master-24: XML Sitemap Health Checker")
        print("Usage: python3 sitemap_checker.py <URL>")
        print("Example: python3 sitemap_checker.py https://davulciyan.com/sitemap.xml")
        sys.exit(0)

    target = sys.argv[1]
    res = check_sitemap(target)
    print(json.dumps(res, indent=2, ensure_ascii=False))
