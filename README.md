# 🚀 SEO-Master-24

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://www.python.org/)
[![SEO-GEO-AEO](https://img.shields.io/badge/Search%20Paradigm-Tri--Vector%20Model-purple.svg)](https://github.com/ArtoHD/SEO-Master-24)
[![Maintained by 24 Software](https://img.shields.io/badge/Maintained%20by-24%20Software-0ea5e9.svg)](https://24software.com.tr)
[![Creator: Harutyun Arto Davulciyan](https://img.shields.io/badge/Creator-Arto%20Davulciyan-f43f5e.svg)](https://davulciyan.com)

> **Next-Generation AI-Native Search & Citability Toolkit.**  
> Built for traditional search engines (Google, Bing), Generative AI answer engines (ChatGPT Search, Perplexity Pro, Google AI Overviews, Gemini, Claude), and autonomous AI agents.

---

## 📖 Introduction

Search has fundamentally transformed. Search queries no longer simply return 10 blue links; autonomous LLM systems synthesize real-time answers, retrieve verified citations, and interpret structured web entities.

**SEO-Master-24** is an all-in-one open-source engineering toolkit designed by **[24 Software](https://24software.com.tr)** and **[Harutyun Arto Davulciyan](https://davulciyan.com)**. It bridges the gap between classic technical on-page SEO, Generative Engine Optimization (GEO), and Answer Engine Optimization (AEO).

---

## 🏛️ The Tri-Vector Discovery Model

```
                          ┌──────────────────────────┐
                          │     SEO-MASTER-24        │
                          │   Tri-Vector Search      │
                          └─────────────┬────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        ▼                               ▼                               ▼
 ┌──────────────┐               ┌──────────────┐                ┌──────────────┐
 │   VECTOR 1   │               │   VECTOR 2   │                │   VECTOR 3   │
 │Technical SEO │               │  GEO Engine  │                │  AEO Engine  │
 │(Google/Bing) │               │ (AI Search)  │                │(Voice/Snipp.)│
 └──────────────┘               └──────────────┘                └──────────────┘
```

### 1. Vector 1: Technical & Programmatic SEO
- **Status Code & Crawl Hygiene**: Zero 4xx/5xx crawl loops, fast TTFB, clean response headers.
- **Canonical & Hreflang Governance**: Strict self-referencing canonicals, zero duplicate content conflicts, complete bidirectional language pairs.
- **Security & Performance**: HSTS (`Strict-Transport-Security`), zero mixed-content, Core Web Vitals optimization.
- **On-Page Hierarchy**: Single semantic `<h1>`, logical heading cascades, descriptive image alt text, and complete OpenGraph/Twitter social cards.

### 2. Vector 2: Generative Engine Optimization (GEO)
- **Engineered for AI Platforms**: Targeted optimization for Perplexity Pro, ChatGPT Search, Gemini Live, Claude Web, and Google AI Overviews.
- **Factual Citability Index (FCI)**: High-density quantifiable metrics, dates, and clear factual claims that retrieval models extract as primary sources.
- **Entity Graph Modeling**: Rich JSON-LD Knowledge Graph integration (`Person`, `Organization`, `LocalBusiness`, `CreativeWork`) with authoritative `sameAs` references (IMDb, Wikidata, YouTube, LinkedIn).
- **AI Crawler Directives**: Explicit permission maps for AI bots (`GPTBot`, `OAI-SearchBot`, `ClaudeBot`, `PerplexityBot`, `Applebot`).
- **Machine Discovery Manifests**: Standardized `llms.txt`, `llms-full.txt`, and `agent.json` endpoints.

### 3. Vector 3: Answer Engine Optimization (AEO)
- **Direct Answer Blocks**: Concise 40-60 word authoritative answer paragraphs placed under natural question headers (`How does X work?`, `What is Y?`).
- **Structured Snippet Schemas**: Validated `FAQPage` and `HowTo` structured markup.
- **Voice Search Readiness**: Conversational natural-language query matching for assistants (Siri, Alexa, Google Assistant).
- **Local Business & NAP Integrity**: Consistent Name, Address, Phone, and GeoCoordinates.

---

## ⚡ Quickstart & Installation

Clone the repository into your project or AI assistant configuration:

```bash
git clone https://github.com/ArtoHD/SEO-Master-24.git
cd SEO-Master-24
```

### Direct Script Usage (Zero Dependencies)

All scripts run out-of-the-box on standard Python 3.8+ without installing external dependencies:

```bash
# 1. Run technical on-page audit
python3 scripts/seo_audit.py https://davulciyan.com/tr

# 2. Measure GEO citability & AI citation readiness (0-100 score)
python3 scripts/geo_citability.py https://davulciyan.com/tr

# 3. Inspect AI search crawler permissions, llms.txt, and agent.json
python3 scripts/agentic_audit.py https://davulciyan.com

# 4. Validate XML sitemap health
python3 scripts/sitemap_checker.py https://davulciyan.com/sitemap.xml
```

---

## 📊 The 24-Vector Scoring Rubric (100 Points)

| Category | Weight | Evaluated Factors |
|---|:---:|---|
| **Technical SEO Architecture** | 20 pts | Crawl status, canonical hygiene, HSTS headers, sitemap accessibility |
| **On-Page & Semantic Copy** | 20 pts | Title/meta tags, single `<h1>` tag, heading hierarchy, image alt text |
| **GEO: Entity & E-E-A-T Authority** | 20 pts | JSON-LD schema, sameAs authoritative links, verifiable creator bio |
| **GEO: AI Citation & LLM Readiness**| 15 pts | AI crawler rules, llms.txt format, factual density, quote-worthiness |
| **AEO: Snippets & FAQ Blocks** | 15 pts | FAQPage schema, interrogative headings, 40-60 word direct answers |
| **AEO: Voice & Local Consistency** | 10 pts | Conversational clarity, NAP data, LocalBusiness geo coordinates |
| **TOTAL SCORE** | **100 pts** | **90+ Exceptional, 75-89 Strong, 60-74 Needs Polish, <60 Critical** |

---

## 📁 Repository Structure

```text
SEO-Master-24/
├── SKILL.md                   # Master Skill definition for AI Coding Assistants (Antigravity, Claude, Cursor)
├── README.md                  # Complete documentation and user guide
├── LICENSE                    # MIT License
├── scripts/
│   ├── seo_audit.py           # Technical on-page crawler & scoring engine
│   ├── geo_citability.py      # AI citation & factual density evaluator
│   ├── agentic_audit.py       # LLM crawler permissions & machine manifest checker
│   └── sitemap_checker.py     # XML sitemap validator & parser
├── templates/
│   ├── llms.txt               # Standard LLMs.txt blueprint for AI crawlers
│   ├── agent.json             # Agentic discovery manifest
│   └── schemas/
│       ├── person.json        # High-E-E-A-T Person schema
│       ├── local_business.json# LocalBusiness schema with coordinates
│       └── faq.json           # FAQPage direct answer schema
└── agents/
    └── AGENTS.md              # Multi-agent role definitions (Auditor, GEO Analyst, Schema Engineer)
```

---

## 🤖 AI Assistant Integration (Antigravity, Claude, Cursor)

To integrate **SEO-Master-24** directly into your AI development assistant:

1. **Google Antigravity IDE**:
   Copy `SKILL.md` to `~/.gemini/config/skills/seo-master-24/SKILL.md` or `.agents/skills/seo-master-24/SKILL.md`.
2. **Claude Code**:
   Copy `SKILL.md` to `~/.claude/skills/seo-master-24/SKILL.md`.
3. **Cursor / Copilot**:
   Add to `.cursorrules` or workspace prompt instructions.

---

## 👥 Authors & Maintainers

- **24 Software**: [https://24software.com.tr](https://24software.com.tr)
- **Harutyun Arto Davulciyan**: [https://davulciyan.com](https://davulciyan.com) | [IMDb](https://www.imdb.com/name/nm12259415/) | [YouTube](https://www.youtube.com/@ArtoHD)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute in your personal and commercial projects.