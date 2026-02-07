---
title: "Going-up theorem"
description: "Along an integral extension, prime ideals can be lifted to extend prime chains."
---

Let $A\subseteq B$ be an {{< knowl id="integral-extension" text="integral extension" >}} of {{< knowl id="commutative-ring" section="algebra-rings" text="commutative rings" >}}. The {{< knowl id="lying-over-theorem" text="lying-over theorem" >}} ensures that primes of $A$ occur as contractions of primes of $B$; going-up strengthens this by lifting *inclusions* of primes.

**Theorem (Going up).**  
Assume $A\subseteq B$ is an {{< knowl id="integral-extension" text="integral extension" >}}. Let $\mathfrak p\subseteq \mathfrak p'$ be prime ideals of $A$, and let $\mathfrak q\in \operatorname{Spec}(B)$ satisfy $\mathfrak q\cap A=\mathfrak p$. Then there exists a prime ideal $\mathfrak q'\subseteq B$ such that
\[
\mathfrak q\subseteq \mathfrak q'
\qquad\text{and}\qquad
\mathfrak q'\cap A=\mathfrak p'.
\]
More generally, for any chain of prime ideals $\mathfrak p_0\subseteq \cdots \subseteq \mathfrak p_n$ in $A$ and any prime $\mathfrak q_0$ of $B$ lying over $\mathfrak p_0$, there is a chain $\mathfrak q_0\subseteq \cdots \subseteq \mathfrak q_n$ in $B$ with $\mathfrak q_i\cap A=\mathfrak p_i$ for all $i$.

In terms of the {{< knowl id="prime-spectrum" text="prime spectrum" >}}, going-up says the contraction map $\operatorname{Spec}(B)\to \operatorname{Spec}(A)$ has the property that prime inclusions downstairs can be realized upstairs, provided one starts with a prime lying over the smaller one.

### Examples
1. **A chain in $\mathbb Z$ lifted to $\mathbb Z[i]$.**  
   The extension $\mathbb Z\subset \mathbb Z[i]$ is integral. Consider the chain $(0)\subset (5)$ in $\mathbb Z$. The prime $(0)\subset \mathbb Z[i]$ lies over $(0)$. Going-up produces a prime $\mathfrak q'\subset \mathbb Z[i]$ with $(0)\subset \mathfrak q'$ and $\mathfrak q'\cap \mathbb Z=(5)$; one choice is $\mathfrak q'=(2+i)$.

2. **From $k[t^2]$ to $k[t]$.**  
   With $A=k[t^2]\subset B=k[t]$ integral, the chain $(0)\subset (t^2)$ in $A$ lifts starting from $(0)\subset B$: going-up gives the chain $(0)\subset (t)$ in $B$, where $(t)\cap A=(t^2)$.

3. **Adjoining a square root of $x$.**  
   Let $A=k[x]\subset B=k[x,y]/(y^2-x)$, which is integral. The chain $(0)\subset (x)$ in $A$ lifts starting from the prime $(0)\subset B$ to the chain $(0)\subset (x,y)$ in $B$, since $(x,y)\cap A=(x)$.
