# Research Synthesis: Math Blog Architecture

## DECISION: Option A with Hybrid Comments

**Final Architecture:**
```
Hugo (v0.132+) + Build-time KaTeX (htmlAndMathml) + Custom Knowls + Giscus + Form Submission
```

---

## Executive Summary

The research converges on **3 viable architecture paths**. The key insight: your requirements (knowls + pre-rendered math + accessible comments) are independently solvable, and the SSG choice is the "root" decision that shapes everything else.

---

## The Tradeoff Space

### Axis 1: Static Site Generator
**Core tradeoff: Math-first ergonomics vs. Knowl extensibility**

| SSG | Math Experience | Knowl Extensibility | Build-time Math Rendering |
|-----|----------------|---------------------|---------------------------|
| **Quarto** | 5/5 (native) | 3/5 (Lua filters, shortcodes) | Via `mathml` method only |
| **Hugo** | 4/5 (config required) | 5/5 (shortcodes, partials) | **Native KaTeX SSR (v0.132+)** |
| **Astro** | 4/5 (remark/rehype) | 5/5 (components, MDX) | Native via rehype-katex |
| **Jekyll** | 3/5 (plugins) | 3/5 (Liquid includes) | Via plugins (jekyll-katex) |

**Key finding**: Hugo v0.132+ introduced `transform.ToMath` with native build-time KaTeX rendering. This is a game-changer for eliminating math flash without a Node toolchain.

### Axis 2: Commenting System
**Core tradeoff: GitHub-required vs. Self-hosted**

| Option | Math Support | Account Requirement | Maintenance |
|--------|-------------|---------------------|-------------|
| **Giscus** | Native (GitHub renders) | GitHub account required | Zero |
| **Remark42** | Via MathJax injection | Email/anonymous/social | Self-host (VPS/Docker) |
| **Utterances** | Native (GitHub renders) | GitHub account required | Zero |
| **IntenseDebate** | Via injection | WordPress.com login option | Third-party |

**Key finding**: No perfect solution exists. Either accept GitHub-only (Giscus) for zero-maintenance + native math, or self-host (Remark42) for accessibility but with MathJax re-render on comment load.

### Axis 3: Knowl Implementation
**Core tradeoff: Use existing library vs. Custom**

| Approach | Pros | Cons |
|----------|------|------|
| **Custom vanilla JS** | No dependencies, full control, no GPL | You maintain it |
| **AIM knowl.js** | "Official" implementation | GPL-3+ license, jQuery dependency |
| **PreTeXt** | Industrial-grade knowlization | XML authoring (not Markdown) |

**Key finding**: Both ChatGPT and Gemini recommend **custom vanilla JS** (~50-100 lines) over adapting knowl.js. The LMFDB pattern (fetch HTML fragment → inject → re-typeset math) is simple enough to implement cleanly.

### Axis 4: Math Rendering Strategy
**Core tradeoff: Build-time vs. Client-side**

| Strategy | Performance | Complexity | SSG Support |
|----------|-------------|------------|-------------|
| **Build-time KaTeX (HTML+CSS)** | Instant (no flash) | Medium | Hugo, Astro, Jekyll |
| **Build-time MathML** | Instant | Low | Quarto, Hugo |
| **Client-side MathJax** | Multi-second delay | Low | All |
| **Client-side KaTeX** | ~100ms delay | Low | All |

**Key finding**: Build-time KaTeX HTML+MathML is the "industry standard" for high-performance math blogs. Hugo's native support makes this easiest.

---

## Axis 5: WordPress Integration
**Verdict: Abandon**

Both research agents agree:
- WordPress commenting on static sites is a "rabbit hole"
- Jetpack requires a WordPress backend
- IntenseDebate is the only viable bridge (but it's aging)
- The math blog community has moved to Mastodon/Fediverse

**Alternative**: Submit RSS to mathblogging.org for community visibility.

---

## The Three Viable Architectures

### Option A: "The Modern Standard" (Recommended)

```
Hugo (v0.132+) + Build-time KaTeX + Custom Knowls + Giscus
```

**Stack:**
- **SSG**: Hugo with `transform.ToMath` (MathML or htmlAndMathml)
- **Math**: Pre-rendered at build time (zero client-side delay)
- **Knowls**: Custom vanilla JS + `/knowls/*.html` fragments
- **Comments**: Giscus (accept GitHub requirement)

**Pros:**
- Fastest builds, fastest page loads
- No Node toolchain required
- Knowl fragments also pre-render math (no flash on expand)
- Zero-maintenance comments

**Cons:**
- GitHub-only comments excludes some mathematicians
- Hugo shortcode syntax slightly more verbose

**Best for**: Maximum performance, minimal infrastructure

---

### Option B: "The Inclusive Stack"

```
Hugo/Quarto + Build-time Math + Custom Knowls + Remark42
```

**Stack:**
- **SSG**: Hugo or Quarto
- **Math**: Pre-rendered
- **Knowls**: Custom vanilla JS
- **Comments**: Remark42 (self-hosted, $5/mo VPS)

**Pros:**
- Email/anonymous comments (accessible to all mathematicians)
- Privacy-respecting
- Full control over comment data

**Cons:**
- Requires hosting a server
- Must inject MathJax re-render on comment load (MutationObserver)
- Ongoing maintenance

**Best for**: Maximizing commenter accessibility, accepting ops burden

---

### Option C: "The Scientific Publisher"

```
Quarto + MathML + Custom Knowls + Giscus + Mastodon integration
```

**Stack:**
- **SSG**: Quarto (Pandoc-based)
- **Math**: `html-math-method: mathml` (fastest, no CSS required)
- **Knowls**: Custom JS + Lua filter for authoring syntax
- **Comments**: Giscus for inline, Mastodon for extended discussion

**Pros:**
- Quarto is purpose-built for academic/scientific publishing
- Native citations, cross-references, multi-format output
- MathML is the "purest" semantic output

**Cons:**
- MathML typography depends on browser math fonts (needs tuning)
- Lua filters have learning curve
- Less control than Hugo/Astro

**Best for**: If you want academic publishing features (citations, cross-refs)

---

## Knowl Implementation (All Options)

All three architectures share the same knowl strategy:

### Content Structure
```
/knowls/
  def.vector_space.md       → builds to → def.vector_space.html
  def.linear_map.md         → builds to → def.linear_map.html
  ...
```

### Authoring Syntax (Hugo example)
```markdown
A {{< knowl id="def.vector_space" text="vector space" >}} is a set V with...
```

### Progressive Enhancement
- Without JS: link goes to `/glossary/def.vector_space/`
- With JS: fragment fetched and inserted inline

### Depth Policy (Anti-rabbit-hole)
- Track nesting depth (d)
- At d > 2: fall back to navigation instead of inline expansion

### Math in Knowls
- If using build-time rendering: knowl fragments already have rendered math
- No client-side typeset needed on expansion (major UX win)

---

## RSS Strategy (All Options)

1. Generate RSS/Atom feed (all SSGs support this)
2. Accept that math won't render in feed readers
3. Add disclaimer: "Contains LaTeX; visit site for rendered equations"
4. Submit to mathblogging.org for visibility

---

## Decision Matrix

| Criterion | Option A (Hugo+Giscus) | Option B (Hugo+Remark42) | Option C (Quarto) |
|-----------|------------------------|--------------------------|-------------------|
| Page load speed | ★★★★★ | ★★★★★ | ★★★★☆ |
| Comment accessibility | ★★☆☆☆ | ★★★★★ | ★★☆☆☆ |
| Maintenance burden | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Knowl extensibility | ★★★★★ | ★★★★★ | ★★★☆☆ |
| Academic features | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ |
| Learning curve | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |

---

## My Recommendation

**Start with Option A (Hugo + Giscus)**, with these caveats:

1. **Comments**: Giscus as primary, plus a **submission form for non-GitHub users** (see below).

2. **Math rendering**: Use Hugo's `transform.ToMath` with `htmlAndMathml` output for best of both worlds (visual + accessibility).

3. **Knowls**: Implement the ~80-line vanilla JS solution. Store definitions as markdown files, build to HTML fragments.

4. **RSS**: Set up from day one, submit to mathblogging.org.

5. **Mastodon**: Consider adding "Discuss on Mathstodon" links as a comment alternative.

---

## Hybrid Comment System (Decided)

### Architecture
```
GitHub users ──→ Giscus (direct posting to GitHub Discussions)
                      ↓
               [Comments displayed]
                      ↑
Non-GitHub users ──→ Form ──→ Form service ──→ Notification ──→ You review ──→ Post to Discussion
```

### Form Backend Options (all free tier)

| Service | Free Tier | Notes |
|---------|-----------|-------|
| **Netlify Forms** | 100 submissions/mo | If hosting on Netlify |
| **Formspree** | 50 submissions/mo | Works anywhere |
| **Formspark** | 250 submissions/mo | Works anywhere |
| **Basin** | 100 submissions/mo | Works anywhere |
| **Cloudflare Workers** | 100k requests/day | Most flexible, slight setup |

### Workflow (v1 - Manual)
1. Non-GitHub user fills form: Name, Comment, (optional: email for reply notification)
2. Form service emails you or stores in dashboard
3. You review for spam/quality
4. You post to GitHub Discussion on their behalf (attribute: "Comment from [Name]:")
5. Comment appears in Giscus widget

### Future Enhancement (v2 - Agent-Assisted)
- Form submissions go to a queue (JSON file in repo, or Airtable, etc.)
- Moderation agent reviews for spam, suggests approval/rejection
- Approved comments auto-post via GitHub API
- You review agent decisions periodically

### Why This Works
- **Zero ongoing cost** (free form tier + GitHub)
- **Durable** (everything lives on GitHub forever)
- **Accessible** (no GitHub required for readers)
- **Spam-resistant** (moderated queue)
- **Automatable later** (structured form data → agent pipeline)

---

## Open Questions (Remaining)

1. ~~**GitHub comments**: Is excluding non-GitHub users a dealbreaker?~~ → **Solved**: Hybrid form system

2. ~~**Self-hosting**: Willing to maintain VPS?~~ → **Decided**: No, prefer zero-cost durable infrastructure

3. **Academic features**: Do you need Quarto's citation/cross-reference system, or is basic markdown sufficient?

4. **Knowl depth**: What's your policy on nesting? Allow 2 levels? 3? Unlimited with UI cues?

5. **Form service**: Which free tier to use? (Formspree is simplest; Cloudflare Workers most flexible)
