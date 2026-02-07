---
title: "Operations on subsets of a vector space"
description: "Set addition, scalar multiplication, and difference inside a vector space"
---

Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $M,N\subset X$ be nonempty subsets, with $\alpha\in K$.

Define:

1. **Set sum**
   $$
   M+N:=\{m+n \mid m\in M,\ n\in N\}.
   $$
2. **Scalar multiple of a set**
   $$
   \alpha M := \{\alpha x \mid x\in M\}.
   $$
3. **Negation and difference**
   $$
   (-1)M=: -M,\qquad M-N := M+(-N).
   $$

These operations produce subsets of $X$, and one always has $M+N=N+M$.

These constructions are used throughout linear and convex analysis; for instance, sums of {{< knowl id="linear-subspace" text="subspaces" >}} are defined using $M+N$, and Minkowski sums of sets are central in convexity.

**Examples:**
- In $X=\mathbb{R}$, if $M=[0,1]$ and $N=[2,4]$, then $M+N=[2,5]$.
- In $X=\mathbb{R}^2$, if $M=\{(0,0)\}$ and $N$ is any set, then $M+N=N$.
- If $M$ is a linear subspace, then $-M=M$ and $M-M=M$.
