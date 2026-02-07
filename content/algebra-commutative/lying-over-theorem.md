---
title: "Lying-over theorem"
description: "In an integral extension, every prime ideal downstairs is the contraction of some prime ideal upstairs."
---

Let $A\subseteq B$ be an extension of {{< knowl id="commutative-ring" section="algebra-rings" text="commutative rings" >}}. The extension is an {{< knowl id="integral-extension" text="integral extension" >}} if every element of $B$ is integral over $A$.

**Theorem (Lying over).**  
Assume $A\subseteq B$ is an {{< knowl id="integral-extension" text="integral extension" >}}. Then for every prime ideal $\mathfrak p\subseteq A$ there exists a prime ideal $\mathfrak q\subseteq B$ such that
\[
\mathfrak q\cap A=\mathfrak p.
\]
Equivalently, the natural map of {{< knowl id="prime-spectrum" text="prime spectra" >}}
\[
\operatorname{Spec}(B)\longrightarrow \operatorname{Spec}(A),\qquad \mathfrak q\mapsto \mathfrak q\cap A
\]
is surjective. In particular, every maximal ideal of $A$ is the contraction of some maximal ideal of $B$, so the induced map on {{< knowl id="maximal-spectrum" text="maximal spectra" >}} is also surjective.

Lying-over is frequently used as the existence input for {{< knowl id="going-up-theorem" text="going up" >}} and, under extra hypotheses, for {{< knowl id="going-down-theorem" text="going down" >}}.

### Examples
1. **Gaussian integers over the integers.**  
   The inclusion $\mathbb Z\subset \mathbb Z[i]$ is integral (since $i$ satisfies $T^2+1=0$). For the prime ideal $(5)\subset\mathbb Z$, lying-over guarantees a prime $\mathfrak q\subset \mathbb Z[i]$ with $\mathfrak q\cap\mathbb Z=(5)$. Concretely, one can take $\mathfrak q=(2+i)$ (or $\mathfrak q=(2-i)$), both lying over $(5)$.

2. **A simple subring of a polynomial ring.**  
   Let $k$ be a {{< knowl id="field" section="algebra-rings" text="field" >}} and set $A=k[t^2]\subset B=k[t]$. The element $t$ is integral over $A$ (it satisfies $T^2-t^2=0$), so $A\subset B$ is integral. The prime ideal $(t^2)\subset A$ is the contraction of the prime ideal $(t)\subset B$.

3. **Adjoining a square root.**  
   Let $A=k[x]$ and $B=k[x,y]/(y^2-x)$. The image of $y$ is integral over $A$ (it satisfies $T^2-x=0$), hence $A\subset B$ is integral. The prime ideal $(x)\subset A$ is the contraction of the prime ideal $(x,y)\subset B$.
