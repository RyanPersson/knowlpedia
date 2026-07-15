Here are the findings regarding commenting systems for a static math blog.

### **Executive Summary**

There is **no perfect "out-of-the-box" solution** that meets every requirement simultaneously. You face a primary trade-off:

1. **Ease of Use & LaTeX Support:** **Giscus** is the best technical performer but **requires** a GitHub account.
2. **Accessibility (No Account) & Privacy:** **Remark42** or **Comentario** are excellent but require **manual script injection** to render LaTeX.

If your audience includes many pure mathematicians who may not have GitHub accounts, **Remark42** (Self-Hosted) with a custom MathJax script is the strongest recommendation.

---

### **Candidate Comparison**

#### **1. Giscus (GitHub-based)**

* **Mechanism:** Uses GitHub Discussions API.
* **LaTeX Support:** **Native (mostly).** Since GitHub Discussions added MathJax support in May 2022, Giscus inherits this. You can write `$e^{i\pi} + 1 = 0$` and it generally renders.
* **Pros:** Zero maintenance (no server), open source, no tracking, free.
* **Cons:** **Strict requirement for a GitHub account.** This is a major friction point for non-programmer mathematicians.
* **Verdict:** The best "set it and forget it" option if you believe your specific audience overlaps significantly with the coding community.

#### **2. Remark42 (Self-Hosted)**

* **Mechanism:** Go-based server (binary or Docker).
* **LaTeX Support:** **Not Native.** Renders Markdown but not MathJax by default.
* **Workaround:** You must inject a MathJax script into your page and configure it to "watch" the Remark42 DOM elements (see *Implementation Note* below).
* **Pros:** Allows anonymous comments, email login, and social login (Google, GitHub, etc.). Privacy-focused. Full data ownership.
* **Cons:** Requires hosting a server instance (e.g., a $5/mo VPS or free tier on Fly.io/Render).
* **Verdict:** The best balance of features. It solves the "accessibility" problem but requires initial technical effort to set up math rendering.

#### **3. Comentario (Formerly Commento)**

* **Status:** **Commento is dead/abandoned.** You should use the active fork, **Comentario**.
* **Mechanism:** Go + PostgreSQL.
* **LaTeX Support:** **Not Native.** Requires the same script injection strategy as Remark42.
* **Pros:** Very clean UI, privacy-focused.
* **Cons:** Heavier backend requirement (PostgreSQL) compared to Remark42 (embedded BoltDB), making it harder to self-host on minimal resources.

#### **4. Isso (Self-Hosted)**

* **Mechanism:** Python + SQLite.
* **LaTeX Support:** **Not Native.** Requires script injection.
* **Pros:** extremely lightweight.
* **Cons:** The UI is dated; fewer moderation features than Remark42.

#### **5. Third-Party Services (Hyvor Talk, Disqus)**

* **Hyvor Talk:** Paid (~$12/mo). Excellent privacy and UI. LaTeX requires script injection.
* **Disqus:** Free but heavy tracking/ads. LaTeX requires script injection. **Not recommended** due to privacy concerns conflicting with your requirements.

---

### **Implementation Note: The "MathJax Injection"**

If you choose a self-hosted option (Remark42, Isso, Comentario), the system will load comments dynamically (via JavaScript) *after* the initial page load. Standard MathJax will miss these.

To fix this, you must add a script to your site that triggers a "re-render" whenever comments are loaded.

**Conceptual Code Snippet:**

```javascript
// Example for Remark42 + MathJax
window.remark_config = {
  // ... your config ...
};

// Create a MutationObserver to watch for new comments
const observer = new MutationObserver((mutations) => {
  // When Remark42 injects comments, trigger MathJax
  if (window.MathJax) {
    window.MathJax.typesetPromise();
  }
});

// Start observing the comment container
const commentNode = document.getElementById('remark42');
if (commentNode) {
  observer.observe(commentNode, { childList: true, subtree: true });
}

```

---

### **Answers to Key Questions**

1. **Does ANY commenting system natively support LaTeX?**
* **Giscus** and **Utterances** support it natively (inherited from GitHub).
* **Discourse** (forum software) supports it via plugins but is overkill for a blog.
* Most others require the "Injection" workaround.


2. **Can we inject MathJax into comment rendering?**
* **Yes.** This is the standard solution for static sites. You load MathJax globally on your page and use a `MutationObserver` (as shown above) to detect when the comment widget loads content, forcing MathJax to process the new text.


3. **What % of mathematicians have GitHub?**
* **Applied Math / CS / Data Science:** High (>80%).
* **Pure Math / Academia:** Moderate to Low (<40%). Many older or purely theoretical mathematicians rely on email and university pages; requiring a GitHub account will effectively silence them.


4. **Is self-hosting viable?**
* **Remark42** is very viable. It compiles to a single binary file. You can run it on a cheap VPS (DigitalOcean, Hetzner) or a container service. It stores data in a local file (BoltDB), so backups are just copying one file.


5. **What do other math blogs use?**
* **Terence Tao / Tim Gowers:** WordPress (Server-side LaTeX plugins).
* **Example Static Math Blogs:** Often use **Disqus** (legacy choice) or **Giscus** (modern choice, accepting the exclusion of non-GitHub users).
* **Niche:** Email-only. "Reply to this post by emailing me at..." This is the highest friction for you (manual updates) but lowest for them.



---

### **Recommendation**

**Option A: The "Inclusive" Choice (Recommended)**

* **System:** **Remark42**
* **Why:** It meets the "Must Have" criteria (works with static sites) and the "Strong Preference" for no GitHub account. It respects privacy and allows anonymous/email commenting.
* **Trade-off:** You must set up a small server (Docker container) and add the JavaScript snippet to handle MathJax rendering.

**Option B: The "Low Maintenance" Choice**

* **System:** **Giscus**
* **Why:** It is free, zero-maintenance, and handles LaTeX natively.
* **Trade-off:** You explicitly accept that readers without GitHub accounts cannot comment.

**Option C: The "Indie Web" Choice**

* **System:** **Email + Manual Appends**
* **Why:** Zero technical debt, 100% accessible to anyone with an email address. High quality filter (spam is irrelevant).
* **Trade-off:** You must manually copy-paste emails into your Markdown files to publish them as "comments." Ideal for low-volume, high-quality discussion.