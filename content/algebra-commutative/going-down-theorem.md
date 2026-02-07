---
title: "Going-down theorem"
description: "For certain integral extensions (e.g. with integrally closed base), prime chains descend inside a fixed prime upstairs."
---

For an {{< knowl id="integral-extension" text="integral extension" >}} $A\subseteq B$, the {{< knowl id="going-up-theorem" text="going-up theorem" >}} says prime inclusions downstairs can be lifted to prime inclusions upstairs. The going-down phenomenon is the opposite direction: once you have fixed a prime upstairs lying over a larger prime downstairs, you can *descend* to primes lying over smaller primes.

**Theorem (Going down).**  
Let $A\subseteq B$ be an {{< knowl id="integral-extension" text="integral extension" >}} of integral domains. Assume that $A$ is an {{< knowl id="integrally-closed-domain" text="integrally closed domain" >}}. Let $\mathfrak p\subseteq \mathfrak p'$ be prime ideals of $A$, and let $\mathfrak q'\in \operatorname{Spec}(B)$ satisfy $\mathfrak q'\cap A=\mathfrak p'$. Then there exists a prime ideal $\mathfrak q\subseteq B$ such that
\[
\mathfrak q\subseteq \mathfrak q'
\qquad\text{and}\qquad
\mathfrak q\cap A=\mathfrak p.
\]
Equivalently, any chain of primes in $A$ can be realized as the contraction of a chain inside $\operatorname{Spec}(B)$ that ends at a prescribed prime lying over the top prime in the chain.

The integrally closed hypothesis is essential: for general integral extensions, going-down can fail, even though {{< knowl id="lying-over-theorem" text="lying over" >}} and {{< knowl id="going-up-theorem" text="going up" >}} always hold.

### Examples
1. **A Dedekind-domain example.**  
   The domain $\mathbb Z$ is {{< knowl id="integrally-closed-domain" text="integrally closed" >}}, and $\mathbb Z\subset\mathbb Z[i]$ is integral. Take the chain $(0)\subset (5)$ in $\mathbb Z$ and the prime $\mathfrak q'=(2+i)\subset \mathbb Z[i]$ lying over $(5)$. Going-down provides a prime $\mathfrak q\subset (2+i)$ with $\mathfrak q\cap\mathbb Z=(0)$; necessarily $\mathfrak q=(0)$.

2. **From $k[t^2]$ to $k[t]$.**  
   Let $A=k[t^2]$ and $B=k[t]$ for a {{< knowl id="field" section="algebra-rings" text="field" >}} $k$. Since $A\cong k[s]$ is a PID, it is {{< knowl id="integrally-closed-domain" text="integrally closed" >}}, and $A\subset B$ is integral. For the chain $(0)\subset (t^2)$ in $A$ and the prime $(t)\subset B$ lying over $(t^2)$, going-down yields $(0)\subset (t)$ inside $B$.

3. **A quadratic integral extension of a PID.**  
   Let $A=k[x]$ and $B=k[x,y]/(y^2-x)$. The ring $A$ is a PID, hence {{< knowl id="integrally-closed-domain" text="integrally closed" >}}, and $B$ is integral over $A$. For the chain $(0)\subset (x)$ in $A$ and the prime $(x,y)\subset B$ lying over $(x)$, going-down produces a prime inside $(x,y)$ contracting to $(0)$; again this is $(0)$.
