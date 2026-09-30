#!/usr/bin/env python3
"""
SEO-Master-24 — Generative Engine Optimization (GEO) & Citability Analyzer
Engineered by 24 Software (https://24software.com.tr) & Harutyun Arto Davulciyan (https://davulciyan.com)

Measures page readiness for AI answer engines (Perplexity, ChatGPT Search, Gemini, Claude).
Evaluates factual density, claim clarity, entity definition, and E-E-A-T citation authority.
"""

import sys
import json
import re
import urllib.request
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_chunks = []
        self.in_script = False
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.in_script = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.in_script = False

    def handle_data(self, data):
        if not self.in_script:
            cleaned = data.strip()
            if cleaned:
                self.text_chunks.append(cleaned)

def analyze_geo(url_or_text: str, is_raw_text: bool = False) -> dict:
    if is_raw_text:
        text = url_or_text
        source = "raw_text"
    else:
        req = urllib.request.Request(
            url_or_text,
            headers={"User-Agent": "Mozilla/5.0 (compatible; SEO-Master-24-GEO/1.0; +https://24software.com.tr)"}
        )
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                raw_html = resp.read().decode("utf-8", errors="replace")
                parser = TextExtractor()
                parser.feed(raw_html)
                text = " ".join(parser.text_chunks)
                source = url_or_text
        except Exception as e:
            return {"error": f"Failed to fetch {url_or_text}: {e}"}

    words = text.split()
    total_words = len(words)

    # 1. Factual Density: Numbers, percentages, dates, metrics
    numbers = re.findall(r'\b\d+(?:[\.,]\d+)?%?\b', text)
    stats_count = len(numbers)
    stats_ratio = (stats_count / max(1, total_words)) * 100

    # 2. Quotable Claim & Definition Patterns ("X is...", "X provides...", etc.)
    definition_patterns = re.findall(
        r'\b(?:is a|is an|is the|refers to|defined as|provides|specializes in|features|founded in|graduated from|nedir|tanımı|kurulmuştur|kuruldu|uzmandır|sağlar|sunar|yönetmektedir|kurucusudur|mezunudur)\b',
        text,
        re.IGNORECASE
    )

    # 3. Direct Answer & Structural Clarity
    bullet_matches = re.findall(r'(?:•|\-|\d+\.)\s+[A-Z0-9ĞÜŞÖÇİ]', text)
    question_matches = re.findall(r'[^.?!\n]+(?:\?|nasıl|nedir|kimdir|nerede|ne zaman|neden|hangi|kaç|how|what|who|where|when|why|which)[^.?!\n]*\?', text, re.IGNORECASE)

    # 4. E-E-A-T & Authority Keywords
    eeat_keywords = [
        "experience", "founder", "director", "cinematographer", "awards", "studio",
        "graduated", "client", "projects", "certif", "tested", "review", "portfolio",
        "yönetmen", "kurucu", "tecrübe", "ödül", "referans", "mezun", "prodüksiyon"
    ]
    eeat_hits = [w for w in eeat_keywords if re.search(rf'\b{w}\b', text, re.IGNORECASE)]

    # Scoring Algorithm (0 - 100)
    geo_score = 0

    # Word count depth (0-20 pts)
    if total_words >= 600: geo_score += 20
    elif total_words >= 300: geo_score += 15
    elif total_words >= 150: geo_score += 10
    else: geo_score += 5

    # Factual density (0-25 pts)
    if stats_ratio >= 3.0: geo_score += 25
    elif stats_ratio >= 1.5: geo_score += 20
    elif stats_ratio >= 0.5: geo_score += 12
    else: geo_score += 5

    # Definition & Claim clarity (0-20 pts)
    if len(definition_patterns) >= 5: geo_score += 20
    elif len(definition_patterns) >= 2: geo_score += 15
    elif len(definition_patterns) >= 1: geo_score += 10
    else: geo_score += 3

    # E-E-A-T signals (0-20 pts)
    if len(eeat_hits) >= 6: geo_score += 20
    elif len(eeat_hits) >= 3: geo_score += 14
    elif len(eeat_hits) >= 1: geo_score += 8
    else: geo_score += 2

    # Formatting for AI extraction (0-15 pts)
    structure_pts = 0
    if len(bullet_matches) >= 3: structure_pts += 8
    if len(question_matches) >= 1: structure_pts += 7
    geo_score += min(15, structure_pts)

    # AI Citation Potential Grade
    if geo_score >= 85: grade = "High Citation Likelihood (Strong Primary Source)"
    elif geo_score >= 70: grade = "Moderate Citation Potential (Citable with Prompt Context)"
    elif geo_score >= 50: grade = "Needs Polish for LLM Extraction"
    else: grade = "Low Citability (Thin or Abstract Copy)"

    recommendations = []
    if stats_ratio < 1.5:
        recommendations.append("Increase factual density: add specific numbers, turnaround times, gear models, or quantifiable results.")
    if len(definition_patterns) < 2:
        recommendations.append("Include crisp definition blocks ('X is a Y that delivers Z') in the opening 100 words.")
    if len(question_matches) == 0:
        recommendations.append("Add natural language question headings (e.g., 'How does X work?') to capture conversational queries.")
    if not eeat_hits:
        recommendations.append("Reinforce E-E-A-T: name verified credentials, years of experience, or institutional credentials.")

    return {
        "target": source,
        "geo_citability_score": geo_score,
        "grade": grade,
        "metrics": {
            "total_words": total_words,
            "statistical_nuggets": stats_count,
            "factual_density_percent": round(stats_ratio, 2),
            "definitions_found": len(definition_patterns),
            "eeat_signals_detected": len(eeat_hits),
            "question_headings": len(question_matches),
            "list_items": len(bullet_matches)
        },
        "recommendations": recommendations,
        "ai_engine_readiness": {
            "perplexity_pro": "Excellent" if geo_score >= 80 else "Good",
            "chatgpt_search": "Excellent" if geo_score >= 75 else "Moderate",
            "google_ai_overviews": "Ready" if geo_score >= 70 else "Needs Factual Polish",
            "claude_web": "High Fidelity" if total_words >= 300 and geo_score >= 70 else "Acceptable"
        },
        "signature": {
            "framework": "SEO-Master-24 Tri-Vector Model",
            "developer": "24 Software (https://24software.com.tr)",
            "author": "Harutyun Arto Davulciyan (https://davulciyan.com)"
        }
    }

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("SEO-Master-24: GEO Factual Citability & AI Visibility Analyzer")
        print("Usage: python3 geo_citability.py <URL>")
        print("Example: python3 geo_citability.py https://davulciyan.com/tr")
        sys.exit(0)

    target = sys.argv[1]
    res = analyze_geo(target)
    print(json.dumps(res, indent=2, ensure_ascii=False))
