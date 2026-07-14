---
title: "Sequential characterization of closure"
description: "In a metric space, a point is in the closure of a set exactly when some sequence from the set converges to it."
---

**Sequential characterization of closure (metric spaces)**:  
Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}, let $A\subseteq X$, and let $x\in X$. Then $x$ lies in the {{< knowl id="closure" text="closure" >}} of $A$ if and only if there exists a {{< knowl id="convergent-sequence" text="convergent sequence" >}} $(a_n)$ with $a_n\in A$ for all $n$ and $a_n\to x$.

Equivalently (in metric spaces), $x\in\overline{A}$ if and only if every {{< knowl id="open-ball" text="open ball" >}} centered at $x$ intersects $A$. This sequential description pairs with the {{< knowl id="sequential-characterization-of-closed-sets" text="sequential characterization of closed sets" >}} to translate closure/closedness questions into statements about sequences.

**Proof sketch** *(metric space case)*:  
If $x\in\overline{A}$, then for each $n$ the ball $B(x,1/n)$ meets $A$; choose $a_n\in A\cap B(x,1/n)$ to obtain $a_n\to x$.  
Conversely, if $a_n\in A$ and $a_n\to x$, then every ball around $x$ contains all sufficiently large $a_n$, so it must intersect $A$, hence $x\in\overline{A}$.

**Examples:**
- In $\mathbb{R}$, the point $0$ lies in the closure of $(0,1)$ because $a_n=1/n\in(0,1)$ and $a_n\to 0$.
- If $A=\{1/n : n\in\mathbb{N}\}\subseteq\mathbb{R}$, then $0\in\overline{A}$ via the sequence $1/n$, while every point $x>0$ not of the form $1/n$ fails to be a limit of a sequence in $A$ and is not in $\overline{A}$.
