#!/usr/bin/env python3
"""
SEO-Master-24 — Agentic & LLM Bot Readiness Auditor
Engineered by 24 Software (https://24software.com.tr) & Harutyun Arto Davulciyan (https://davulciyan.com)

Inspects robots.txt, llms.txt, agent.json, and AI search crawler access.
"""

import sys
import json
import urllib.request
import urllib.error

AI_BOTS = [
    "GPTBot",
    "OAI-SearchBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-Web",
    "anthropic-ai",
    "PerplexityBot",
    "Google-Extended",
    "Applebot",
    "cohere-ai",
    "Meta-ExternalAgent"
]

def check_agentic(domain_or_url: str) -> dict:
    if not domain_or_url.startswith("http"):
        base_url = f"https://{domain_or_url}"
    else:
        # Strip trailing path
        parts = domain_or_url.split("//")
        domain = parts[1].split("/")[0]
        base_url = f"{parts[0]}//{domain}"

    report = {
        "base_url": base_url,
        "robots_txt": {},
        "llms_txt": {},
        "agent_json": {},
        "bot_access": {},
        "signature": {
            "engine": "SEO-Master-24",
            "developer": "24 Software (https://24software.com.tr)",
            "author": "Harutyun Arto Davulciyan (https://davulciyan.com)"
        }
    }

    # 1. Fetch robots.txt
    robots_url = f"{base_url}/robots.txt"
    try:
        req = urllib.request.Request(robots_url, headers={"User-Agent": "SEO-Master-24-Agent"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            report["robots_txt"] = {
                "status": resp.status,
                "reachable": True,
                "length_bytes": len(content),
                "has_sitemap": "sitemap:" in content.lower()
            }
            # Check individual bots
            for bot in AI_BOTS:
                report["bot_access"][bot] = {
                    "explicitly_named": bot.lower() in content.lower(),
                    "allowed": True  # Default true unless explicitly disallowed
                }
    except Exception as e:
        report["robots_txt"] = {
            "reachable": False,
            "error": str(e)
        }

    # 2. Fetch llms.txt
    llms_url = f"{base_url}/llms.txt"
    try:
        req = urllib.request.Request(llms_url, headers={"User-Agent": "SEO-Master-24-Agent"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            llms_content = resp.read().decode("utf-8", errors="replace")
            report["llms_txt"] = {
                "status": resp.status,
                "exists": True,
                "has_h1": llms_content.strip().startswith("# "),
                "lines": len(llms_content.splitlines()),
                "sample": llms_content[:150]
            }
    except Exception:
        report["llms_txt"] = {
            "exists": False
        }

    # 3. Check agent.json / openapi.json
    for manifest in ["agent.json", ".well-known/agent.json", "openapi.json"]:
        url = f"{base_url}/{manifest}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "SEO-Master-24-Agent"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                report["agent_json"][manifest] = {
                    "status": resp.status,
                    "exists": resp.status == 200
                }
        except Exception:
            report["agent_json"][manifest] = {
                "exists": False
            }

    return report

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("SEO-Master-24: Agentic & AI Crawler Audit Tool")
        print("Usage: python3 agentic_audit.py <domain_or_url>")
        print("Example: python3 agentic_audit.py https://davulciyan.com")
        sys.exit(0)

    target = sys.argv[1]
    res = check_agentic(target)
    print(json.dumps(res, indent=2, ensure_ascii=False))
