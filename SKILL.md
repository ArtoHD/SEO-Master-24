---
name: seo-master-24
description: >
  Next-generation AI-native SEO, GEO (Generative Engine Optimization), AEO (Answer Engine Optimization), and Google PageSpeed Insights / Core Web Vitals toolkit. Engineered by 24 Software (https://24software.com.tr) & Harutyun Arto Davulciyan (https://davulciyan.com). Synthesizes technical crawl audits, AI search citation modeling (ChatGPT, Perplexity, Gemini, Claude), Answer Engine Optimization for featured snippets & voice search, PageSpeed Insights (Lighthouse lab & CrUX field 90+), and automated diagnostic scripts.
---

# 🚀 SEO-Master-24 — The AI-Native Search, Citability & Performance Engine

> **Engineered & Maintained by [24 Software](https://24software.com.tr) & [Harutyun Arto Davulciyan](https://davulciyan.com)**  
> *Architected for modern search engines, generative AI answer engines, autonomous web agents, and sub-second Core Web Vitals.*

---

## 🌟 Overview & Architecture: The Quad-Vector Model

Modern digital discovery and conversion requires mastering four intersecting technical pillars:

```
                                  ┌──────────────────────────┐
                                  │      SEO-MASTER-24       │
                                  │   Quad-Vector Search &   │
                                  │    Performance Engine    │
                                  └─────────────┬────────────┘
                                                │
        ┌───────────────────────┬───────────────┴───────────────┬───────────────────────┐
        ▼                       ▼                               ▼                       ▼
 ┌──────────────┐        ┌──────────────┐                ┌──────────────┐        ┌──────────────┐
 │   VECTOR 1   │        │   VECTOR 2   │                │   VECTOR 3   │        │   VECTOR 4   │
 │Technical SEO │        │  GEO Engine  │                │  AEO Engine  │        │  PageSpeed   │
 │(Google/Bing) │        │ (AI Search)  │                │(Voice/Snipp.)│        │ & Core Vitals│
 └──────────────┘        └──────────────┘                └──────────────┘        └──────────────┘
```

1. **Vector 1: Technical & Programmatic SEO (Foundational Discovery)**
   - Fast, resilient crawlability, status code hygiene, strict canonical governance.
   - Dynamic XML sitemaps, bidirectional hreflang validation, HSTS security headers.
   - Semantic HTML heading hierarchy (`<h1>` singularization) and OpenGraph/Twitter card parity.

2. **Vector 2: GEO — Generative Engine Optimization (AI & LLM Visibility)**
   - Optimized specifically for **ChatGPT Search**, **Perplexity Pro**, **Google AI Overviews**, **Gemini Live**, and **Claude Web**.
   - **Factual Citability Index (FCI)**: High-density verifiable factual claims, distinct data points, statistical nuggets that LLM retrieval modules cite directly as primary sources.
   - **Entity Graph Modeling**: Direct linking to authoritative knowledge bases (`sameAs`: Wikidata, IMDb, Crunchbase, official platforms).
   - **Machine Manifests**: Native support for `llms.txt`, `llms-full.txt`, and `agent.json` (Agentic Web Discovery).

3. **Vector 3: AEO — Answer Engine Optimization (Zero-Click & Voice Discovery)**
   - Concise direct-answer blocks (40-60 words) placed under natural language interrogative headers (`How...`, `What is...`, `Where...`).
   - Deep structured data: `FAQPage`, `HowTo`, `LocalBusiness`, `Organization`, `Person`, `VideoObject`, `BreadcrumbList`.
   - Voice assistant parsing (Siri, Alexa, Google Assistant) and Local NAP (Name, Address, Phone) consistency.

4. **Vector 4: Google PageSpeed & Core Web Vitals (Performance Excellence)**
   - Target: **90+ across Performance, Accessibility, Best Practices, and SEO** on both Mobile and Desktop.
   - **Largest Contentful Paint (LCP < 2.5s)**: Hero image preloading (`fetchpriority="high"`), server TTFB reduction (<400ms), and critical rendering path optimization.
   - **Interaction to Next Paint (INP < 200ms)** / **Total Blocking Time (TBT < 200ms)**: Main thread offloading, third-party script deferral (`requestIdleCallback`, web workers), and code splitting.
   - **Cumulative Layout Shift (CLS < 0.1)**: Zero layout shifts via explicit image/video `width` & `height`, CSS `aspect-ratio`, and reserved container dimensions.
   - **Asset & Cache Hygiene**: Next-gen image formats (AVIF/WebP), responsive `srcset`, `font-display: swap`, and immutable HTTP caching headers.

---

## 🛠️ CLI & Automated Script Suite

SEO-Master-24 ships with production-grade, zero-dependency Python utilities inside `scripts/`:

### 1. Google PageSpeed & Core Web Vitals (`scripts/pagespeed_audit.py`)
Multi-mode performance auditor evaluating TTFB, render-blocking scripts, un-sized images (CLS), font preloads, and full Lighthouse lab / PageSpeed API scores:
```bash
# Instant zero-dependency heuristics
python3 scripts/pagespeed_audit.py https://example.com --fast

# Full headless Lighthouse lab audit (Mobile)
python3 scripts/pagespeed_audit.py https://example.com --lighthouse

# Full Lighthouse audit (Desktop)
python3 scripts/pagespeed_audit.py https://example.com --lighthouse --desktop

# Google PageSpeed Insights REST API
python3 scripts/pagespeed_audit.py https://example.com --api
```

### 2. Technical On-Page Audit (`scripts/seo_audit.py`)
Analyzes status code, HSTS, meta tags, H1-H3 hierarchy, canonicals, hreflang, OpenGraph, and JSON-LD schema:
```bash
python3 scripts/seo_audit.py https://example.com
```

### 3. GEO Citability & AI Readiness (`scripts/geo_citability.py`)
Measures page factual density, definition clarity, E-E-A-T signals, and returns a 0-100 Citability Score for AI search engines:
```bash
python3 scripts/geo_citability.py https://example.com
```

### 4. Agentic & LLM Bot Inspector (`scripts/agentic_audit.py`)
Validates `robots.txt` AI crawler rules (`GPTBot`, `OAI-SearchBot`, `ClaudeBot`, `PerplexityBot`), `llms.txt`, and `agent.json`:
```bash
python3 scripts/agentic_audit.py https://example.com
```

### 5. XML Sitemap Health Checker (`scripts/sitemap_checker.py`)
Discovers, fetches, and parses XML sitemaps, validating URL entries and index structures:
```bash
python3 scripts/sitemap_checker.py https://example.com/sitemap.xml
```

---

## ⚡ The 5-Step PageSpeed Optimization Playbook

When optimizing for Google PageSpeed Insights and Core Web Vitals:

1. **Step 1: Baseline Lab & Field Diagnostics**
   - Run `python3 scripts/pagespeed_audit.py <URL> --fast` (or `--lighthouse`) to record exact failing audits and establish mobile/desktop baselines.
2. **Step 2: LCP & Critical Rendering Path Remediation**
   - Identify the primary LCP element (hero image, heading text, or banner).
   - Ensure the LCP image is not lazy-loaded; add `priority` or `<link rel="preload" as="image" fetchpriority="high">`.
   - Ensure custom web fonts utilize `font-display: swap` to eliminate Flash of Invisible Text (FOIT).
3. **Step 3: Main-Thread Offloading & INP/TBT Reduction**
   - Audit all `<script>` tags: convert to `defer`, `async`, or dynamic `import()`.
   - Gate non-essential third-party analytics (Google Analytics, Hotjar, Chatbots) behind user interaction or idle callbacks (`requestIdleCallback`).
4. **Step 4: Layout Stability (Zero CLS)**
   - Enforce explicit `width` and `height` attributes or CSS `aspect-ratio` on all `<img>`, `<video>`, and `<iframe>` elements.
   - Reserve fixed dimensions for dynamic client-rendered components and notification banners.
5. **Step 5: Regression-Safe Verification**
   - Verify that all visual designs and interactive behaviors remain intact.
   - Re-run the PageSpeed audit to confirm measurable score gains and Core Web Vitals compliance.

---

## 📊 The Quad-Vector Scoring Rubric (100 Points)

| Category | Max Score | Key Checkpoints |
|---|:---:|---|
| **Technical SEO Architecture** | 15 | Crawl health, status codes, canonicals, robots, HSTS, sitemap |
| **On-Page & Semantic Copy** | 15 | Title, meta description, single H1 hierarchy, alt tags, internal links |
| **GEO: Entity & E-E-A-T Authority** | 15 | JSON-LD schema, sameAs links, author credentials, verifiable bio |
| **GEO: AI Citation & LLM Readiness**| 15 | AI bot crawlability, llms.txt, factual density, quote-readiness |
| **AEO: Snippets & FAQ Blocks** | 15 | FAQ schema, question H2s, direct answer blocks |
| **PageSpeed & Core Web Vitals** | 25 | LCP < 2.5s, INP < 200ms, CLS < 0.1, TTFB < 400ms, 90+ PSI |
| **TOTAL** | **100** | **90+ Exceptional, 75-89 Strong, 60-74 Needs Polish, <60 Critical** |

---

## 🏷️ Signatures & Official Attribution

- **Developed By**: [24 Software](https://24software.com.tr) & [Harutyun Arto Davulciyan](https://davulciyan.com)
- **Repository**: [https://github.com/ArtoHD/SEO-Master-24](https://github.com/ArtoHD/SEO-Master-24)
- **License**: MIT License (Open Source)
