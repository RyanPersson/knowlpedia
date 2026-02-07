---
title: "Cramér's theorem"
description: "Large deviations for empirical means of independent identically distributed real random variables."
---

**Cramér's theorem:** Let $(X_i)_{i\ge 1}$ be an {{< knowl id="iid-sequence" section="probability" text="i.i.d. sequence" >}} of real-valued {{< knowl id="random-variable" section="probability" text="random variables" >}}. Assume the {{< knowl id="moment-generating-function" section="probability" text="moment generating function" >}} $M(\theta)=\mathbb{E}[e^{\theta X_1}]$ is finite for all $\theta$ in some open interval containing $0$, and let $\Lambda(\theta)=\log M(\theta)$ be the {{< knowl id="log-moment-generating-function" text="log moment generating function" >}}. Define the empirical mean $\overline X_n=\frac{1}{n}\sum_{i=1}^n X_i$. Then $(\overline X_n)$ satisfies a {{< knowl id="large-deviation-principle" text="large deviation principle" >}} on $\mathbb{R}$ with speed $n$ and {{< knowl id="good-rate-function" text="good rate function" >}}
\[
I(x)=\sup_{\theta\in\mathbb{R}}\bigl\{\theta x-\Lambda(\theta)\bigr\}.
\]

The rate function $I$ is the {{< knowl id="cramer-transform" text="Cramér transform" >}}, i.e. the {{< knowl id="legendre-fenchel-transform" section="convex-analysis" text="Legendre–Fenchel transform" >}} ({{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel conjugate" >}}) of $\Lambda$.
