---
title: "Exponential tightness"
description: "A compact-containment condition ensuring probabilities outside compacts decay exponentially fast."
---

A sequence of probability measures $(\mu_n)_{n\ge1}$ on a topological space $E$ is **exponentially tight at speed** $(a_n)_{n\ge1}$ with $a_n\to\infty$ if for every $M>0$ there exists a compact set $K_M\subseteq E$ such that
$$
\limsup_{n\to\infty}\frac{1}{a_n}\log \mu_n(K_M^{\,c}) \le -M.
$$

Exponential tightness is a strengthened form of ordinary tightness for {{< knowl id="probability-measure" section="probability" text="probability measures" >}}: it not only forces most mass into compacts, but does so with exponentially small tails at the LDP speed. It is frequently paired with a {{< knowl id="rate-function" text="rate function" >}} to obtain or upgrade a {{< knowl id="large-deviation-principle" text="large deviation principle" >}}, and it is a standard hypothesis in results like the {{< knowl id="gartner-ellis-theorem" text="Gärtner–Ellis theorem" >}}.

**Examples:**
- If $X$ has a finite {{< knowl id="moment-generating-function" section="probability" text="moment generating function" >}} in a neighborhood of $0$, then the laws of $\bar X_n=\frac1n\sum_{i=1}^n X_i$ are typically exponentially tight at speed $n$ on $\mathbb R$ (exponential moment bounds imply exponentially small tails).
- If $E$ itself is compact, then any sequence $(\mu_n)$ is exponentially tight at any speed, since one can take $K_M=E$ for all $M$.
