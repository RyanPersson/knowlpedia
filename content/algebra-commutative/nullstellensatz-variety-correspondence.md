---
title: "Nullstellensatz: varieties and radical ideals"
description: "Over an algebraically closed field, Zariski-closed subsets of affine space correspond to radical ideals in a polynomial ring."
---

Let $k$ be an algebraically closed {{< knowl id="field" section="algebra-rings" text="field" >}} and let $A=k[x_1,\dots,x_n]$. For an ideal $I\subseteq A$, define its zero set
\[
V(I)=\{a\in k^n : f(a)=0 \text{ for all } f\in I\}.
\]
For a subset $X\subseteq k^n$, define the ideal of functions vanishing on $X$ by
\[
I(X)=\{f\in A : f(a)=0 \text{ for all } a\in X\}.
\]
The sets $V(I)$ are exactly the closed sets of the {{< knowl id="zariski-topology" text="Zariski topology" >}} on $k^n$.

**Theorem (Nullstellensatz, variety–ideal correspondence).**  
With $k$ and $A$ as above, the following hold:
1. For every ideal $I\subseteq A$, one has
   \[
   I\bigl(V(I)\bigr)=\sqrt{I},
   \]
   the radical of $I$.
2. For every Zariski-closed set $X\subseteq k^n$, one has
   \[
   V\bigl(I(X)\bigr)=X.
   \]

Consequently, the assignments $I\mapsto V(I)$ and $X\mapsto I(X)$ restrict to mutually inverse, inclusion-reversing bijections between:
- radical ideals of $A$, and
- Zariski-closed subsets of $k^n$.

A useful special case is the "weak" form: maximal ideals of $A$ are exactly the ideals $(x_1-a_1,\dots,x_n-a_n)$ for points $a=(a_1,\dots,a_n)\in k^n$. In other words, the {{< knowl id="maximal-spectrum" text="maximal spectrum" >}} $\operatorname{MaxSpec}(A)$ can be identified with $k^n$, and the corresponding {{< knowl id="residue-field" text="residue field" >}} at such a maximal ideal is (canonically) $k$.

### Examples
1. **A non-radical ideal with the same zero set as its radical.**  
   In $k[x]$, let $I=(x^2)$. Then $V(I)=\{0\}$, but
   \[
   I\bigl(V(I)\bigr)=(x)=\sqrt{(x^2)}.
   \]
   This illustrates that taking $V(-)$ forgets nilpotent structure, and the theorem recovers exactly the radical.

2. **A point.**  
   In $k[x,y]$, let $I=(x,y)$. Then $V(I)=\{(0,0)\}$. Conversely, for the closed set $X=\{(0,0)\}$ one has $I(X)=(x,y)$, a maximal ideal, matching the identification of {{< knowl id="maximal-spectrum" text="maximal ideals" >}} with points.

3. **A reducible algebraic set.**  
   In $k[x,y]$, let $I=(xy)$. Then $V(I)$ is the union of the two coordinate axes. The ideal of this union is
   \[
   I\bigl(V(I)\bigr)=(x)\cap (y)=\sqrt{(xy)},
   \]
   reflecting that $V(I)$ has two irreducible components.
