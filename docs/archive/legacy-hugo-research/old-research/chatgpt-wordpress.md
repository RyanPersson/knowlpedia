## Core definitions (minimal, but precise)

* **Static site**: a website whose pages are served as pre-built files (typically HTML/CSS/JS) without server-side code running per request.
* **GitHub Pages**: a hosting service that serves static files from a GitHub repository; it does not run arbitrary server code (no PHP/Node backend).
* **WordPress.com**: Automattic’s hosted WordPress platform (you create a site under `*.wordpress.com` or map a custom domain).
* **Self-hosted WordPress**: you run WordPress software (PHP + database) on your own server/host.
* **OAuth 2.0**: a delegated authorization protocol where a **client** obtains an **access token** from an **authorization server** (after user approval) to access protected resources on a **resource server**.
* **SSO (Single Sign-On)**: a user authenticates once with an identity provider and can then authenticate to another service without creating a new credential there.
* **Webmention**: a web standard for notifying URL (B) that URL (A) links to (B); used for cross-site comments/likes/replies.
* **RSS/Atom feed**: an XML document listing recent content items (“entries”) with metadata (title, URL, timestamp, optional HTML content) so feed readers/aggregators can poll and display updates.

---

## 1) WordPress.com commenting integration for a static site

### 1.1 Can WordPress.com accounts comment on non-WordPress sites?

Not “natively.” There are only three realistic mechanisms:

1. **Use a comment system that explicitly supports WordPress.com login**

   * **IntenseDebate** supports “Sign in with WordPress.com” and is designed to be embedded on “any site” using JavaScript snippets. ([intensedebate.com][1])
     Practical implication: this is the closest thing to “Login with WordPress for comments” that works on GitHub Pages with no backend.

2. **Implement “Login with WordPress.com” yourself (OAuth2), then build your own commenting backend**

   * WordPress.com provides OAuth2 endpoints and explicitly markets WordPress.com Connect as “Login with WordPress.com.” ([WordPress.com Developer Resources][2])
     Practical blocker: a real comment system needs a server component (store comments, moderation, spam defense). GitHub Pages alone cannot do this.

3. **Run WordPress somewhere (even if your front-end is static)**

   * E.g. self-host WordPress as a backend (headless CMS or just “comments backend”), then fetch/store comments there.
   * This defeats the “pure GitHub Pages only” constraint, but it’s feasible if you’re willing to host *something*.

### 1.2 Jetpack Comments: does it solve this for a static site?

**No**—Jetpack Comments is a WordPress plugin/module that replaces the WordPress comment form and can allow readers to use WordPress.com accounts (and other social logins) on **a WordPress site**. ([Jetpack][3])
A static site can’t install Jetpack because there’s no WordPress runtime.

### 1.3 “Login with WordPress.com” as an OAuth bridge

WordPress.com Connect is real OAuth2 login infrastructure. ([WordPress.com Developer Resources][4])
But it is only an **identity/auth** layer. You still need:

* a **comment database**
* moderation tools
* spam/abuse controls
* a server-side way to sign/validate requests and protect secrets

That’s why this becomes a significant engineering project for a GitHub Pages site.

### 1.4 A subtle downside: WordPress.com identity can *increase* friction

WordPress.com can require users to sign in to “prove” identity if the email address they use for commenting is associated with a WordPress.com account (even if you want to allow guest comments). ([WordPress][5])
So “WordPress ecosystem familiarity” does not automatically mean “lower-friction commenting.”

---

## 2) What established math(-heavy) blogs actually do for comments

A strong pattern: **WordPress blogs overwhelmingly use native WordPress comments** (sometimes with moderation/policy changes), rather than fancy identity bridges.

Examples (all heavily trafficked, comment-driven at various times):

* **Terence Tao — “What’s new”** is on WordPress.com (`terrytao.wordpress.com`). ([What's new][6])
* **Timothy Gowers — “Gowers’s Weblog”** is on WordPress.com (`gowers.wordpress.com`). ([Gowers's Weblog][7])
* **Gil Kalai — “Combinatorics and more”** is on WordPress.com (`gilkalai.wordpress.com`). ([Combinatorics and more][8])
* **John Baez — “Azimuth”** is on WordPress.com (`johncarlosbaez.wordpress.com`). ([Azimuth][9])
* **n-Category Café** has a WordPress.com presence (`ncategory.wordpress.com`). ([The n-Category Café][10])
* **Scott Aaronson — “Shtetl-Optimized”** uses WordPress-style “Leave a Reply” commenting and has an explicit comment policy; it also notes TeX-in-comments conventions. ([Shtetl-Optimized][11])

What this indicates (empirically): the “math blog commenting culture” grew up around *native WP comments* and *loose identity requirements* (often name/email), not around federated identity across platforms.

---

## 3) Bridging / federating comments (WordPress ↔ static)

### 3.1 Webmention is the closest thing to a real “federation protocol”

* Webmention is a W3C Recommendation. ([W3C][12])
* WordPress has a Webmention plugin to send/receive webmentions. ([WordPress.org][13])
* Bridgy can translate social-network replies/likes into webmentions sent back to your site. ([brid.gy][14])

**Key limitation**: Webmention works best when commenters are posting replies on *their own URLs* (their own site, or a social post with a stable URL bridged back). It does not automatically “mirror” a WordPress-native comment thread onto a static site.

### 3.2 “Comments appear in both places” (mirroring)

This is not off-the-shelf. The workable architectures are:

* **One canonical comment store, two displays**:

  * Example: canonical comments live on a WordPress post; your static site fetches and displays them.
  * You can do this at **build time** (periodic rebuild) or **client-side** (JS fetch at page load).
  * You still need to implement mapping, pagination, and moderation decisions.

* **Mirror posts to WordPress.com just for comments**

  * Operationally simple (WordPress handles auth/spam/moderation).
  * But you now have split canonical URLs, SEO/canonical-link considerations, and you’ll likely end up linking users “go comment over there” rather than truly integrating.

* **ActivityPub route**

  * If you want federation *like Mastodon*, ActivityPub is the protocol; Webmention + Bridgy Fed is one practical way to integrate static sites into that world. ([Bridgy Fed][15])
  * This is typically “replies on Mastodon become comments on your site,” not “WordPress.com accounts comment on your site.”

---

## 4) RSS & syndication in the math blog community

### 4.1 Is RSS actually used in the math blogosphere?

Two concrete signals that it is:

* **Mathblogging.org** is an active aggregator site that exists specifically to ingest and present math blog feeds; it explicitly invites submissions. ([Math Blogging][16])
* **The Aperiodical** explicitly references reading posts “that go through Mathblogging.org.” ([The Aperiodical][17])

So even if individual reader habits vary, the ecosystem infrastructure (aggregators/curators) still assumes feeds.

### 4.2 Static sites generating RSS/Atom is routine

* **Jekyll**: `jekyll-feed` generates an Atom feed (Atom is RSS-like). ([GitHub][18])
* **Hugo**: generates RSS feeds by default and lets you control which page kinds output RSS. ([Hugo][19])
* **Quarto**: can generate RSS for blogs/listings when `site-url` etc. are set. ([Quarto][20])

### 4.3 Does RSS render LaTeX?

Usually **no**, because most feed readers:

* **do not execute JavaScript**, so MathJax won’t run. ([Mathematics Meta Stack Exchange][21])

What works (imperfectly):

* **Raw TeX in feed content**: readers show the TeX markup; acceptable for some technical audiences.
* **MathML in feed content**: can work in some browser-based readers, but many readers don’t render it (and some sanitizers strip unusual tags). A concrete report: MathML didn’t render in at least one RSS reader experience. ([JeffTK][22])
* **Pre-render equations to images/SVG** inside the feed: more compatible, but can bloat feeds and complicate accessibility.

### 4.4 RSS metadata that matters for math blogs

Independent of platform, high-impact feed details are:

* **Stable item identifiers** (RSS `guid` / Atom `id`) so readers don’t duplicate posts.
* **Correct absolute URLs** for links.
* **Publish timestamps** (RSS `pubDate` / Atom `updated`).
* **HTML content policy**: decide between “full content in feed” vs “excerpt only.”
* **Categories/tags** if you want downstream filtering/aggregation.

If you want inclusion in aggregators, the practical requirement is simply: “your feed is valid XML, consistently updated, and not enormous.”

---

## 5) Honest feasibility assessment

### 5.1 Is WordPress integration worth pursuing?

**Native WordPress.com-commenting-on-your-static-site is mostly a rabbit hole** unless you accept one of these compromises:

* **Compromise A (lowest effort)**: use **IntenseDebate** to get “Sign in with WordPress.com” on a static site. ([intensedebate.com][1])
  Risks: it’s a smaller/older ecosystem than Disqus; customization and long-term direction are uncertain compared to “roll your own.”

* **Compromise B (operationally simple, conceptually messy)**: mirror posts to WordPress.com and treat WordPress as the comment host.

* **Compromise C (engineering heavy)**: implement WordPress.com OAuth login + build a comment backend (not compatible with “GitHub Pages only”).

### 5.2 Overlap: “people with WordPress accounts” vs “people who comment on math blogs”

No clean public statistic exists; the best grounded inference from the landscape is:

* Many *bloggers* in math have WordPress accounts because they blog on WordPress.
* Many *commenters* on WordPress blogs do not need WordPress accounts, because WordPress commenting commonly allows guest name/email (modulo site settings and the WordPress.com email/identity friction noted earlier). ([WordPress][5])

So optimizing around WordPress.com accounts specifically is unlikely to be the dominant lever for increasing comment participation.

### 5.3 Simpler ways to “be part of the community” without WordPress

* Have a clean RSS/Atom feed and submit it to Mathblogging.org. ([Math Blogging][16])
* Engage with curator ecosystems (e.g. Aperiodical weekly picks that draw from Mathblogging). ([The Aperiodical][17])
* Offer a discussion channel that matches where mathematicians already are (in 2025 that often includes the Fediverse; Webmention/Bridgy is the standards-based bridge). ([brid.gy][14])

---

## 6) Recommendation (actionable)

### If your constraints are “GitHub Pages + static-first” and you want comments:

1. **Do RSS/Atom first** (high value, low cost)

   * Enable feed generation in your SSG (Jekyll/Hugo/Quarto all support it). ([GitHub][18])
   * Submit to Mathblogging.org. ([Math Blogging][16])

2. Choose one commenting strategy based on what you’re optimizing:

* **Maximal simplicity / minimal infrastructure**:

  * No embedded comments; link to “discuss on Mastodon” (or equivalent) and optionally pull replies back via Webmention/Bridgy later. ([brid.gy][14])

* **Static-friendly, standards-based federation**:

  * Add Webmention receiving (often via a hosted endpoint like webmention.io) and optionally Bridgy for social replies. ([W3C][23])

* **You specifically want WordPress.com login on a static site** (narrow goal):

  * Treat **IntenseDebate** as the only reasonably direct route that works without a backend. ([IntenseDebate Support][24])
  * Do this as an experiment, not a foundational dependency.

### What I would *not* recommend as a first-class goal

* Building a bespoke “WordPress.com OAuth → custom comments” pipeline: it’s real software engineering, and GitHub Pages alone can’t host it. ([WordPress.com Developer Resources][4])
* Trying to “bridge native WordPress comments” into your static site in a seamless two-way way: feasible, but high maintenance and not standard.

If you want, I can produce two concrete implementation blueprints (no code unless requested):

* A “static + RSS + Mathblogging submission + Webmention/Bridgy comments” architecture.
* A “static + mirrored WordPress.com posts for comments + canonical-link strategy” architecture.

[1]: https://www.intensedebate.com/login.php?utm_source=chatgpt.com "IntenseDebate - Login"
[2]: https://developer.wordpress.com/docs/api/oauth2/?utm_source=chatgpt.com "OAuth2 Authentication - Secure API Access"
[3]: https://jetpack.com/support/comments/?utm_source=chatgpt.com "Jetpack Comments"
[4]: https://developer.wordpress.com/docs/api/wpcc/?utm_source=chatgpt.com "Seamlessly Integrate WordPress.com Connect for Login"
[5]: https://wordpress.com/forums/topic/how-to-leave-a-commentlike-without-having-to-register/?utm_source=chatgpt.com "how to leave a comment/like without having to register"
[6]: https://terrytao.wordpress.com/?utm_source=chatgpt.com "Terry Tao - WordPress.com"
[7]: https://gowers.wordpress.com/?utm_source=chatgpt.com "Gowers's Weblog - WordPress.com"
[8]: https://gilkalai.wordpress.com/?utm_source=chatgpt.com "Gil Kalai's blog: Combinatorics and more"
[9]: https://johncarlosbaez.wordpress.com/?utm_source=chatgpt.com "Azimuth - WordPress.com"
[10]: https://ncategory.wordpress.com/?utm_source=chatgpt.com "The n-Category Café - WordPress.com"
[11]: https://scottaaronson.blog/?utm_source=chatgpt.com "Shtetl-Optimized"
[12]: https://www.w3.org/news/2017/webmention-is-a-w3c-recommendation/?utm_source=chatgpt.com "Webmention is a W3C Recommendation | 2017 | News"
[13]: https://wordpress.org/plugins/webmention/?utm_source=chatgpt.com "Webmention – WordPress plugin"
[14]: https://brid.gy/about?utm_source=chatgpt.com "About"
[15]: https://fed.brid.gy/docs?utm_source=chatgpt.com "Bridgy Fed"
[16]: https://mathblogging.org/about/?utm_source=chatgpt.com "About mathblogging.org"
[17]: https://aperiodical.com/tag/blogging/page/2/?utm_source=chatgpt.com "blogging – Page 2 – The Aperiodical"
[18]: https://github.com/jekyll/jekyll-feed?utm_source=chatgpt.com "A Jekyll plugin to generate an Atom (RSS-like) feed of your ..."
[19]: https://gohugo.io/templates/rss/?utm_source=chatgpt.com "RSS templates"
[20]: https://quarto.org/docs/websites/website-blog.html?utm_source=chatgpt.com "Creating a Blog"
[21]: https://math.meta.stackexchange.com/questions/9144/latex-problem-in-rss-feed?utm_source=chatgpt.com "LaTeX problem in RSS feed - Mathematics Meta"
[22]: https://www.jefftk.com/p/hand-writing-mathml?utm_source=chatgpt.com "Hand-writing MathML - Jeff Kaufman"
[23]: https://www.w3.org/TR/webmention/?utm_source=chatgpt.com "Webmention"
[24]: https://support.intensedebate.com/generic-install/?utm_source=chatgpt.com "Generic Install"
