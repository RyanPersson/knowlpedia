## Basic constraint (static sites / GitHub Pages)

A **static site** is served as fixed files (HTML/CSS/JS) with no server-side code at request time. **GitHub Pages** is static hosting, so any commenting system must be either:

1. **Third-party hosted** (you embed a script; comments live on their servers), or
2. **Backed by another platform you already use** (e.g. GitHub Issues/Discussions), or
3. **Self-hosted elsewhere** (you run a small server/VPS; your static site embeds it).

For math, what you actually want is **TeX-style math typesetting**: users type a TeX/LaTeX-like math syntax (e.g. `$x^2$`), and a renderer turns it into formatted math.

* **MathJax** is an open-source JavaScript display engine that typesets TeX/LaTeX-style math on the web. ([GitHub Docs][1])
* **KaTeX** is another renderer; it is fast but does not implement every LaTeX-ish math feature people expect (e.g. some environments). ([katex.org][2])

---

## Comparison table (your candidates)

| System         | Hosting model (works on GitHub Pages?)                                  | Account friction                                  | Math in comments                                       | Moderation / spam                                       | Privacy posture                                   | Pros                                             | Cons                                                       |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| **Giscus**     | GitHub Discussions-backed embed (yes)                                   | **Requires GitHub OAuth**                         | **Native via GitHub math**                             | Moderate via GitHub tools                               | “No tracking, no ads”; data in GitHub Discussions | Very low-maintenance; themes; no DB; OSS         | Requires GitHub account; comments live on GitHub           |
| **Utterances** | GitHub Issues-backed embed (yes)                                        | **Requires GitHub account**                       | **Native via GitHub math**                             | Moderate via GitHub issues                              | “No tracking, no ads”; data in GitHub Issues      | Simple; OSS; proven                              | Requires GitHub account; issues-as-comments can be awkward |
| **Remark42**   | Self-hosted comment server + embed (yes, but you host server elsewhere) | Can do **email login** and **optional anonymous** | Not “native”; typically add MathJax/KaTeX on your site | Built-in moderation; blocking; notifications            | Explicitly “no tracking”; privacy-focused         | Best match for “no GitHub required” + moderation | You must run a service (VPS/Docker), backups/updates       |
| **Isso**       | Self-hosted Python server + embed (yes, but host elsewhere)             | **Anonymous comments** supported                  | Not “native”; add MathJax/KaTeX on your site           | Moderation queue; “Guard” rate-limits                   | Positioning: lightweight, anti-Disqus             | SQLite; simple; good for anonymous               | Harder spam problem if anonymous; fewer “modern” features  |
| **Commento**   | Self-hosted (and also a hosted service exists)                          | Usually OAuth/SSO style                           | Not “native”; add MathJax/KaTeX on your site           | Moderation + spam detection + email notifs (per README) | Markets itself as privacy-respecting              | Feature-rich; OSS                                | Maintenance/trajectory is less clear than Remark42/Isso    |
| **Commento++** | Fork of Commento; self-host                                             | OAuth logins; (feature set varies by fork)        | Not clearly “native”                                   | Claims moderation + spam detection + email notifs       | “No adverts” positioning                          | Lots of features listed                          | Fork status + long-term maintenance uncertainty            |
| **Hyvor Talk** | Hosted paid service (yes)                                               | Depends on their auth options                     | **KaTeX support** available                            | Moderation features exist (varies by plan)              | Markets privacy-focus                             | No server to run; math supported                 | Paid; closed-source; vendor dependency                     |
| **Disqus**     | Hosted service (yes)                                                    | Common logins                                     | No official MathJax/LaTeX support                      | Moderation exists                                       | Explicit data collection + ad/tracking ecosystem  | Ubiquitous; turnkey                              | Privacy tradeoffs; math support is awkward/unofficial      |

### Source anchors for the strongest claims

* GitHub supports LaTeX-formatted math in Markdown using MathJax; available in **Issues** and **Discussions**. ([GitHub Docs][1])
* Giscus: OSS; “no tracking/no ads”; stores data in GitHub Discussions; requires GitHub OAuth for commenting. ([GitHub][3])
* Utterances: OSS; “no tracking/no ads”; stores data in GitHub issues. ([GitHub][4])
* Remark42: self-hosted; email login + optional anonymous; moderation; notifications; “no tracking.” ([remark42.com][5])
* Isso: self-hosted; anonymous comments; integrates into static sites; moderation queue; “Guard” for basic spam protection/rate limiting. ([isso-comments.de][6])
* Hyvor Talk: KaTeX can be enabled for comments. ([hyvor.com][7])
* Disqus: privacy policy describes collection/use/sale/disclosure; ad-management terms explicitly mention ad placement/tracking/analytics. ([help.disqus.com][8])
* Disqus math: people have requested “official MathJax support,” indicating it’s not a standard supported feature. ([Google Groups][9])

---

## Key questions

### 1) Does any commenting system natively support LaTeX/MathJax?

Yes, but it’s usually “native” because the backing platform already renders math:

* **GitHub** renders math (MathJax) in Markdown in **Issues** and **Discussions**, so **Utterances**/**Giscus** inherit it. ([GitHub Docs][1])
* **Hyvor Talk** offers **KaTeX** as a built-in option. ([hyvor.com][7])
* (Outside your list) **Discourse** can support LaTeX via its math plugin (now bundled into Discourse core). ([GitHub][10])

### 2) If not native, can you “inject MathJax” into comment rendering?

Sometimes.

MathJax can typeset math on a page when loaded, and you can explicitly re-typeset after new content is inserted. ([MathJax Documentation][11])

Practical constraint: if a comment system renders comments inside a **cross-origin iframe**, your site’s MathJax cannot safely reach into that iframe. In that case, you need the comment provider itself to support math (GitHub does; Hyvor does; Disqus generally doesn’t). ([GitHub Docs][1])

### 3) What % of mathematicians have GitHub?

I don’t know of a credible statistic that isolates “mathematicians” (as opposed to software developers broadly). A defensible approach is empirical:

* Put up Giscus for a month and measure “login clicks vs. successful comments.”
* Or run a short poll on your site (“Do you have a GitHub account?”).

Any numeric claim here without a targeted survey would be guesswork.

### 4) Is self-hosting viable?

Self-hosting is viable if you can tolerate:

* A small always-on service (VPS, Fly.io, etc.),
* Upgrades and backups,
* Basic ops (TLS/reverse proxy).

Remark42 explicitly aims to be easy to deploy (Dockerized; self-contained executable; embedded storage). ([remark42.com][5])
Isso is also designed for static-site integration and is relatively simple (SQLite). ([isso-comments.de][12])

### 5) What do other math(-adjacent) blogs do?

Examples you can inspect as “prior art”:

* **Aaron Meurer’s blog** (math/software) switched from Disqus to **Utterances**. ([Asmeurer][13])
* A common pattern in technical blogging is “Disqus → (privacy concerns) → Giscus/Remark42.” For instance, a writeup of “Disqus to Remark42” exists for a static site. ([Andrea Corbellini][14])
* Giscus itself lists deployed sites (including a statistics site). ([GitHub][3])

---

## Recommendation (aligned to your priorities)

### If you can accept “GitHub account required”

Pick **Giscus**.

Reason: It hits *static-site friendly*, *low maintenance*, *moderation via GitHub*, *open-source/no-tracking claim*, and *math works because GitHub Discussions renders MathJax math*. ([GitHub][3])

Utterances is fine too, but Discussions is generally a better UX for “comments” than Issues.

### If “no GitHub account required” is truly important

Pick **Remark42** *if you can self-host*.

Reason: It explicitly supports **email login** and **optional anonymous** access, plus moderation and notifications, while claiming no tracking and a privacy-focused design. ([remark42.com][5])
For math, you add MathJax to your site and re-typeset when comments update. ([MathJax Documentation][11])

If you expect heavy math and lots of custom macros, consider isolating user-defined macros so one commenter can’t accidentally affect others; MathJax provides mechanisms intended for “blog comments” style macro-localization. ([MathJax Documentation][15])

### If you want anonymous comments and maximum simplicity (and accept spam risk)

Pick **Isso**.

Reason: Designed for static sites; anonymous comments; moderation queue; basic anti-spam via rate limits (“Guard”). ([isso-comments.de][6])
Tradeoff: anonymous commenting plus weak identity often implies more spam pressure; you’ll rely more on moderation/rate limiting than on strong spam classification.

### If you want “no server to run” and math support, and don’t mind paying

Consider **Hyvor Talk**.

Reason: Hosted, and explicitly supports KaTeX math in comments. ([hyvor.com][7])

### Avoid (given your constraints)

**Disqus**, if privacy-respecting/no-tracking is a real requirement: their ecosystem explicitly involves data collection and (for many publishers) ad/tracking/analytics. ([help.disqus.com][8])
Also, math is not a first-class supported feature. ([Google Groups][9])

---

## If you conclude “no good solution exists”

It’s more accurate to say: “There is no perfect solution that is simultaneously (i) zero-maintenance, (ii) privacy-maximal, (iii) no-accounts-needed, and (iv) fully MathJax-compatible.”

Two robust fallback patterns:

* **Email-only** (“send comments to X; selected replies get published/added as updates”). Lowest reader friction, highest author labor.
* **Split mode**: keep a lightweight comment box for short remarks + link to a “full discussion thread” elsewhere (e.g. a forum/Discourse), so serious math discussions have a proper platform.

If you want, I can propose a concrete “best-effort” architecture for Remark42+MathJax (including how to re-typeset on new comments) without committing you to any single SSG.

[1]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions "Writing mathematical expressions - GitHub Docs"
[2]: https://katex.org/docs/issues?utm_source=chatgpt.com "Common Issues"
[3]: https://github.com/giscus/giscus "GitHub - giscus/giscus: A commenting system powered by GitHub Discussions. :speech_balloon: :gem:"
[4]: https://github.com/utterance/utterances?utm_source=chatgpt.com "utterance/utterances: :crystal_ball: A lightweight comments ... - GitHub"
[5]: https://remark42.com/ "Remark42 – Privacy-focused lightweight commenting engine | Remark42"
[6]: https://isso-comments.de/docs/ "Getting started"
[7]: https://hyvor.com/blog/introducing-katex-embed?utm_source=chatgpt.com "Introducing KaTeX (Math) and Embed Support"
[8]: https://help.disqus.com/en/articles/1717103-disqus-privacy-policy?utm_source=chatgpt.com "Disqus Privacy Policy"
[9]: https://groups.google.com/g/disqus-dev/c/dlYiSytNujY?utm_source=chatgpt.com "MathJax support in Disqus comments"
[10]: https://github.com/discourse/discourse-math?utm_source=chatgpt.com "Official MathJax support for Discourse"
[11]: https://docs.mathjax.org/en/v4.0/web/typeset.html?utm_source=chatgpt.com "Typesetting Mathematics — MathJax 4.0 documentation"
[12]: https://isso-comments.de/ "Isso – a commenting server similar to Disqus"
[13]: https://asmeurer.com/blog/posts/switching-to-utterances-comments/?utm_source=chatgpt.com "Switching to Utterances Comments | Aaron Meurer's Blog"
[14]: https://andrea.corbellini.name/2023/09/05/disqus-to-remark42/?utm_source=chatgpt.com "My journey from Disqus to Remark42 - Andrea Corbellini"
[15]: https://docs.mathjax.org/en/v2.0/_sources/tex.rst.txt?utm_source=chatgpt.com "tex.rst.txt"
