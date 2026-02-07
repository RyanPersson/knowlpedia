---
title: "Essential supremum"
description: "Least upper bound of a measurable function after ignoring a null set."
---

An **essential supremum** of a {{< knowl id="measurable-function" text="measurable function" >}} $f:X\to\overline{\mathbb{R}}$ on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ is the number
\[
\operatorname*{ess\,sup}_{x\in X} f(x)
:= \inf\Bigl\{M\in\mathbb{R} : f(x)\le M \text{ for }\mu\text{-almost every }x\in X\Bigr\}.
\]
Equivalently, $\operatorname*{ess\,sup} f$ is the {{< knowl id="infimum" section="real-analysis" text="infimum" >}} of all real numbers $M$ that are an upper bound for $f$ outside a {{< knowl id="null-set" text="null set" >}}.

Unlike the pointwise {{< knowl id="supremum" section="real-analysis" text="supremum" >}}, the essential supremum is unchanged if $f$ is modified on a null set; in particular it depends only on the {{< knowl id="ae-equality" text="a.e. equivalence class" >}} of $f$. This notion is used to define the $p=\infty$ case of the {{< knowl id="lp-norm" text="$L^p$ norm" >}}.

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, for $f(x)=x$ one has $\operatorname*{ess\,sup} f=1$.
- On the same space, if $f(0)=1$ and $f(x)=0$ for $x\in(0,1]$, then $\sup f=1$ but $\operatorname*{ess\,sup} f=0$ since the exceptional point $\{0\}$ is a {{< knowl id="null-set" text="null set" >}}.
