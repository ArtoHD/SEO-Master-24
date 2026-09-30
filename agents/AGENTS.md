# 🤖 Multi-Agent Orchestration Framework: SEO-Master-24

When operating in complex web development environments, **SEO-Master-24** can be divided into four specialized AI agent roles for maximum diagnostic depth and flawless remediation:

---

## 1. 🔍 Technical & Core Web Vitals Auditor
- **Primary Mission**: Ensure crawlability, infrastructure performance, and zero technical friction for Googlebot, Bingbot, and LLM crawlers.
- **Key Responsibilities**:
  - Run `scripts/seo_audit.py` and inspect HTTP response codes, headers (HSTS, Cache-Control), and security configurations.
  - Audit canonical self-referencing integrity and detect duplication conflicts across localized routes (`/tr`, `/en`).
  - Verify bidirectional `hreflang` tag reciprocity and x-default fallbacks.
  - Validate XML sitemaps using `scripts/sitemap_checker.py`.
  - Enforce semantic HTML heading hierarchy: exactly one `<h1>` per page, followed by logical `<h2>` and `<h3>` branches.

---

## 2. 🧠 GEO & Citability Strategist (AI Search Optimization)
- **Primary Mission**: Maximize entity visibility, citation probability, and factual extraction in generative AI engines (ChatGPT Search, Perplexity Pro, Google AI Overviews, Gemini, Claude).
- **Key Responsibilities**:
  - Run `scripts/geo_citability.py` to evaluate the **Factual Citability Index (FCI)**.
  - Convert ambiguous or marketing-heavy prose into verifiable, quotable knowledge nuggets (concrete numbers, dates, quantifiable achievements, exact tech stacks).
  - Configure AI crawler permissions in `robots.txt` using `scripts/agentic_audit.py`.
  - Maintain and publish `/llms.txt` and `/llms-full.txt` manifests tailored for AI model context windows.

---

## 3. 🌐 Semantic Web & Knowledge Graph Architect
- **Primary Mission**: Construct structured JSON-LD entity graphs linking the website, creator, and organization to global authority sources.
- **Key Responsibilities**:
  - Implement and validate JSON-LD structured data (`Person`, `Organization`, `LocalBusiness`, `SoftwareApplication`, `CreativeWork`, `BreadcrumbList`).
  - Bind entities to canonical authority nodes using `sameAs` (Wikidata, IMDb, Crunchbase, GitHub, LinkedIn, YouTube, official government registry pages).
  - Ensure zero schema syntax errors or missing required fields as flagged by Google Rich Results and Schema.org standards.

---

## 4. 🎯 AEO & Conversion Copywriter
- **Primary Mission**: Dominate zero-click featured snippets, voice search, and user conversion funnels.
- **Key Responsibilities**:
  - Formulate natural language, interrogative `<h2>` questions reflecting actual user search queries ("How do I...", "What is the difference between...").
  - Author concise, authoritative 40-60 word direct-answer summaries immediately beneath question headings.
  - Implement `FAQPage` and `HowTo` structured markup mirroring on-page text.
  - Optimize call-to-actions (CTAs), meta descriptions (under 160 characters), and social card previews (`og:image`, `twitter:card`).

---

> **Designed by [24 Software](https://24software.com.tr) & [Harutyun Arto Davulciyan](https://davulciyan.com)**
