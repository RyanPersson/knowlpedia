---
title: "Characterization of direct sums"
description: "A sum is direct iff every element has a unique decomposition into components"
---

**Theorem.**
Let $M$ and $N$ be linear subspaces of a vector space $X$, and let $Y\subset X$. Then
$$
Y=M\oplus N
$$
if and only if every $y\in Y$ admits a **unique** representation
$$
y=a+b \quad\text{with } a\in M,\ b\in N.
$$

**Context.** This result explains why {{< knowl id="direct-sum-of-subspaces" text="direct sums" >}} behave like "coordinate decompositions" with respect to the two subspaces.

**Proof sketch.**
- ($\Rightarrow$) If $y=a+b=a'+b'$ with $a,a'\in M$ and $b,b'\in N$, then $a-a'=b'-b\in M\cap N=\{0\}$, so $a=a'$ and $b=b'$.
- ($\Leftarrow$) If every $y$ has a unique decomposition, then certainly $Y\subset M+N$ and $M+N\subset Y$ (by definition of $Y$), and uniqueness forces $M\cap N=\{0\}$ since $x=x+0=0+x$ implies $x=0$ for $x\in M\cap N$.
