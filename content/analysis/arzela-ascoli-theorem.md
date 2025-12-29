---
title: "Arzelà–Ascoli Theorem"
description: "On a compact metric space, equicontinuity and pointwise boundedness characterize relative compactness in C(K)"
---

Let $(K,d)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and consider $C(K,\mathbb{R})$ with the {{< knowl id="sup-norm" text="sup metric" >}}
$
d_\infty(f,g)=\sup_{x\in K}|f(x)-g(x)|.
$

A subset $\mathcal{F}\subseteq C(K,\mathbb{R})$ is **{{< knowl id="relatively-compact-set" text="relatively compact" >}}** if its {{< knowl id="closure" text="closure" >}} in $(C(K,\mathbb{R}),d_\infty)$ is compact.

**Arzelà–Ascoli Theorem (real-valued, compact metric domain)**: For $\mathcal{F}\subseteq C(K,\mathbb{R})$, the following are equivalent:
- $\mathcal{F}$ is relatively compact in $(C(K,\mathbb{R}),d_\infty)$.
- $\mathcal{F}$ is {{< knowl id="equicontinuous-family" text="equicontinuous" >}} on $K$ and {{< knowl id="pointwise-bounded-family" text="pointwise bounded" >}} on $K$.

Equivalently (sequential form): $\mathcal{F}$ is relatively compact if and only if every sequence in $\mathcal{F}$ has a {{< knowl id="uniform-convergence" text="uniformly convergent" >}} {{< knowl id="subsequence" text="subsequence" >}} (with respect to $d_\infty$).

This theorem is the main compactness criterion for families of {{< knowl id="continuous-function" text="continuous functions" >}} and is central in existence proofs and approximation theory.

**Proof sketch**:
($\Rightarrow$) If $\overline{\mathcal{F}}$ is compact, then any sequence in $\mathcal{F}$ has a uniformly convergent subsequence. Pointwise boundedness follows because uniform convergence implies pointwise boundedness of a {{< knowl id="convergent-sequence" text="convergent" >}} subsequence and compactness gives {{< knowl id="uniformly-bounded-family" text="uniform boundedness" >}} over the compact set. Equicontinuity follows by contradiction: if not equicontinuous, there exist $\varepsilon_0>0$, functions $f_n\in\mathcal{F}$, and points $x_n,y_n\in K$ with $d(x_n,y_n)\to 0$ but $|f_n(x_n)-f_n(y_n)|\ge \varepsilon_0$. Extract a uniformly convergent subsequence $f_{n_k}\to f$ and convergent subsequences $x_{n_k}\to x$, $y_{n_k}\to x$ (compactness of $K$). Then uniform convergence and continuity of $f$ force $|f_{n_k}(x_{n_k})-f_{n_k}(y_{n_k})|\to 0$, contradicting $\varepsilon_0$.

($\Leftarrow$) Assume $\mathcal{F}$ is equicontinuous and pointwise bounded. Choose a countable {{< knowl id="dense-set" text="dense" >}} subset $D=\{x_1,x_2,\dots\}\subseteq K$. By pointwise boundedness and {{< knowl id="bolzano-weierstrass-theorem" text="Bolzano–Weierstrass" >}} in $\mathbb{R}$, from any sequence $(f_n)$ in $\mathcal{F}$ one can extract a subsequence that converges at $x_1$; then extract a further subsequence that converges at $x_2$; continue and take a diagonal subsequence $(g_n)$ that converges at every $x_j\in D$. Equicontinuity then upgrades convergence on the dense set $D$ to uniform convergence on $K$ (using compactness of $K$ to pass from local equicontinuity to global control). The uniform limit is continuous, so the subsequence converges in $C(K,\mathbb{R})$. Hence every sequence has a uniformly convergent subsequence, so $\mathcal{F}$ is relatively compact.
