---
name: seo-master-24
description: >
  Next-generation AI-native SEO, GEO (Generative Engine Optimization), and AEO (Answer Engine Optimization) toolkit. Engineered by 24 Software (https://24software.com.tr) & Harutyun Arto Davulciyan (https://davulciyan.com). Synthesizes technical crawl audits, AI search citation modeling (ChatGPT, Perplexity, Gemini, Claude), Answer Engine Optimization for featured snippets & voice search, and automated Python diagnostic scripts.
---

# 🚀 SEO-Master-24 — The AI-Native Search & Citability Engine

> **Engineered & Maintained by [24 Software](https://24software.com.tr) & [Harutyun Arto Davulciyan](https://davulciyan.com)**  
> *Architected for modern search engines, generative AI answer engines, and autonomous web agents.*

---

## 🌟 Overview & Architecture: The Tri-Vector Model

Modern digital discovery no longer belongs to traditional keyword-matching crawlers alone. Today, user journeys flow through three intersecting discovery engines:

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

1. **Vector 1: Technical & Programmatic SEO (Foundational Discovery)**
   - Fast, resilient crawlability, status code hygiene, strict canonical governance.
   - Dynamic XML sitemaps, bidirectional hreflang validation, HSTS security headers.
   - Core Web Vitals (LCP, INP, CLS) and mobile viewport compliance.

2. **Vector 2: GEO — Generative Engine Optimization (AI & LLM Visibility)**
   - Optimized specifically for **ChatGPT Search**, **Perplexity Pro**, **Google AI Overviews**, **Gemini Live**, and **Claude Web**.
   - **Factual Citability Index (FCI)**: High-density, verifiable factual claims, distinct data points, statistical nuggets that LLM retrieval modules cite directly as authoritative primary sources.
   - **Entity Graph Modeling**: Direct linking to authoritative knowledge bases (`sameAs`: Wikidata, IMDb, Crunchbase, official platforms).
   - **Machine Manifests**: Native support for `llms.txt`, `llms-full.txt`, and `agent.json` (Agentic Web Discovery).

3. **Vector 3: AEO — Answer Engine Optimization (Zero-Click & Voice Discovery)**
   - Concise direct-answer blocks (40-60 words) placed under natural language interrogative headers (`How...`, `What is...`, `Where...`).
   - Deep structured data: `FAQPage`, `HowTo`, `LocalBusiness`, `Organization`, `Person`, `VideoObject`, `BreadcrumbList`.
   - Voice assistant parsing (Siri, Alexa, Google Assistant) and Local NAP (Name, Address, Phone) consistency.

---

## 🛠️ CLI & Automated Script Suite

SEO-Master-24 ships with production-grade, zero-dependency Python utilities inside `scripts/`:

### 1. Technical On-Page Audit (`scripts/seo_audit.py`)
Analyzes status code, HSTS, meta tags, H1-H3 hierarchy, canonicals, hreflang, OpenGraph, and JSON-LD schema:
```bash
python3 scripts/seo_audit.py https://example.com
```

### 2. GEO Citability & AI Readiness (`scripts/geo_citability.py`)
Measures page factual density, definition clarity, E-E-A-T signals, and returns a 0-100 Citability Score for AI search engines:
```bash
python3 scripts/geo_citability.py https://example.com
```

### 3. Agentic & LLM Bot Inspector (`scripts/agentic_audit.py`)
Validates `robots.txt` AI crawler rules (`GPTBot`, `OAI-SearchBot`, `ClaudeBot`, `PerplexityBot`), `llms.txt`, and `agent.json`:
```bash
python3 scripts/agentic_audit.py https://example.com
```

### 4. XML Sitemap Health Checker (`scripts/sitemap_checker.py`)
Discovers, fetches, and parses XML sitemaps, validating URL entries and index structures:
```bash
python3 scripts/sitemap_checker.py https://example.com/sitemap.xml
```

---

## 📊 The 24-Vector Scoring Rubric (100 Points)

| Category | Max Score | Key Checkpoints |
|---|:---:|---|
| **Technical SEO Architecture** | 20 | Crawl health, status codes, canonicals, robots, HSTS, sitemap |
| **On-Page & Semantic Copy** | 20 | Title, meta description, single H1 hierarchy, alt tags, internal links |
| **GEO: E-E-A-T & Entity Graph** | 20 | JSON-LD schema, sameAs links, author credentials, verifiable bio |
| **GEO: AI Citation & LLM Readiness**| 15 | AI bot crawlability, llms.txt, factual density, quote-readiness |
| **AEO: Snippets & FAQ Blocks** | 15 | FAQ schema, question H2s, direct answer blocks |
| **AEO: Voice & Local Consistency** | 10 | Conversational phrasing, NAP data, local business schema |
| **TOTAL** | **100** | **90+ Exceptional, 75-89 Strong, 60-74 Needs Polish, <60 Critical** |

---

## 🔄 End-to-End Audit & Execution Workflow

When conducting an audit with **SEO-Master-24**:

1. **Phase 1: Automated Diagnostics**
   - Run `python3 scripts/seo_audit.py <URL>` to capture technical parameters.
   - Run `python3 scripts/geo_citability.py <URL>` to measure AI citation viability.
   - Run `python3 scripts/agentic_audit.py <URL>` to inspect bot permissions.
2. **Phase 2: Source Code & Template Inspection**
   - Verify layout files, `robots.ts`, `sitemap.ts`, and component heading structures (`h1` singularization).
   - Ensure OpenGraph tags include high-resolution `images` (1200x630) on all pages.
3. **Phase 3: Synthesis & Remediation**
   - Deliver clear categorization: **High Priority Fixes (Bugs/Errors)**, **Medium Priority Improvements**, and **Strategic GEO/AEO Enhancements**.
   - Provide clean, verified code changes.

---

## 🏷️ Signatures & Official Attribution

- **Developed By**: [24 Software](https://24software.com.tr) & [Harutyun Arto Davulciyan](https://davulciyan.com)
- **Repository**: [https://github.com/ArtoHD/SEO-Master-24](https://github.com/ArtoHD/SEO-Master-24)
- **License**: MIT License (Open Source)
