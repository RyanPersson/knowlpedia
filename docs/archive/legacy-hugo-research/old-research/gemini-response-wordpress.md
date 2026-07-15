## Feasibility Assessment: WordPress Ecosystem

### Executive Summary

**Is WordPress integration viable?**
**No.** Attempting to "bolt on" the WordPress commenting ecosystem to a static site (GitHub Pages) is a **rabbit hole**. The technical bridges (like Jetpack for static sites) are largely deprecated or require a running WordPress backend instance anyway (Headless CMS), which negates the simplicity of a static site.

**The Reality:**
While the *content* of the math blogosphere is hosted on WordPress (Tao, Gowers, Polymath), the *community interaction* is increasingly moving to federated platforms (Mastodon/Mathstodon) or remaining on the blogs themselves via native forms. You cannot easily tap into the "WordPress User Network" without running WordPress yourself.

---

### 1. WordPress Commenting Integration

#### Can you use WordPress.com accounts to comment on non-WP sites?

**Practically, no.**

* **The Mechanism:** The primary tool for this is **Jetpack**, a plugin suite for WordPress. While Jetpack allows "Login with WordPress.com," it is designed to run *on* a WordPress installation.
* **Standalone Use:** There is no official, supported "Jetpack Comment Widget" for purely static HTML sites. To use it, you would effectively have to run a "Headless WordPress" instance (a live server running PHP/MySQL) just to serve the comment API to your static frontend. This defeats the purpose of hosting on GitHub Pages.
* **Bridging:** There are no active, reliable "bridges" that federate WordPress comments to static sites.

#### What do the giants use?

* **Terence Tao (What's New):** Native WordPress.com comments.
* **Timothy Gowers:** Native WordPress.com comments.
* **Quanta Magazine:** Commenting is often disabled or offloaded to social media; they historically used systems like Disqus but have moved away from on-site comments to reduce moderation overhead.

**Verdict:** The "WordPress login" is not a universal passport you can easily import.

---

### 2. RSS & Syndication for Math Blogs

#### How does RSS work in the math community?

* **Usage:** High. The math community is one of the last strongholds of RSS usage because it allows researchers to follow low-frequency, high-density blogs without relying on social media algorithms.
* **Aggregators:**
* **Mathblogging.org:** Still exists but feels dated.
* **Hacker News & Reddit (r/math):** These are the *de facto* aggregators today.
* **Planet Math:** Mostly defunct or replaced by newer networks.



#### The "MathJax in RSS" Problem

* **Does RSS render LaTeX?** **No.**
* **The Issue:** RSS readers (Feedly, Reeder, Newsboat) aggressively strip `<script>` tags for security. MathJax (the standard for web math) relies on JavaScript. Therefore, your beautiful equations will render as raw code (`$\int_0^\infty$`) or disappear entirely in a feed reader.
* **Best Practice:**
1. **Leave it as raw LaTeX:** Most mathematicians can read `$\sum_{n=1}^\infty \frac{1}{n^2}$` fluently.
2. **Hard-code images:** Some tools (like certain pandoc pipelines) convert LaTeX to SVG/PNG at build time. This ensures visibility but breaks accessibility and scaling.
3. **The "Feed Note":** Add a standard header to your RSS feed items: *"Note: This post contains complex mathematics that may not render in your feed reader. Please visit the site for the best experience."*



---

### 3. The WordPress Math Blog Landscape

* **Dominance:** WordPress is indeed dominant for established professors (Tao, Gowers, Baez) because it was the only viable option 15 years ago.
* **The Shift:** New math blogs are increasingly built on static site generators (Hugo, Jekyll, Quarto) because they handle LaTeX natively and version control (Git) aligns with how mathematicians write papers.
* **Community Hubs:** The conversation has moved. It is no longer "blog-to-blog" via pingbacks. It is now "Blog-to-Mathstodon." The Mastodon instance **mathstodon.xyz** is currently the most vibrant hub for academic math discussion.

---

### 4. Recommendation

**Abandon the WordPress Integration.**
It is high-effort technical debt that yields minimal community return. The "WordPress user base" is not a closed garden you need special access to; they are just people with email addresses.

**Alternative Strategy (The "Modern Stack" Approach):**

1. **Comment System:** Use **Giscus** or **Utterances**.
* *Why:* They store comments as GitHub Discussions/Issues.
* *Pros:* Zero maintenance, free, Markdown/LaTeX support is excellent.
* *Cons:* Requires a GitHub account to comment. (Note: This alienates some older non-coder academics, but captures the younger demographic).
* *Compromise:* **Cusdis** (lightweight, privacy-friendly, allows anonymous/email comments) or **Remark42** (if you have a server to host it).


2. **Community Integration:**
* **Fediverse / Mastodon:** Instead of comments, add a "Discuss on Mastodon" link at the bottom of posts.
* *Mechanism:* You post the article link to Mathstodon. You use the Mastodon API to fetch replies to that post and display them as comments on your static blog.
* *Benefit:* This taps into the *active* conversation rather than the *legacy* WordPress infrastructure.


3. **Content Delivery:**
* Build with **Quarto** or **Hugo** (with a math-focused theme). These are superior to WordPress for rendering equations.
* Ensure your RSS feed is valid and includes the "Read on site for LaTeX" disclaimer.



### Next Step

Would you like me to outline the architecture for a "Mastodon-powered comment section" for a static site, or would you prefer a comparison of static site generators (like Quarto vs. Hugo) specifically for math content?