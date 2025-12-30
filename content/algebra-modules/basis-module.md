---
title: "Basis of a free module"
description: "A set of elements giving unique finite linear combinations in a free module."
---

Let $F$ be a free $R$-module (see {{</* knowl id="free-module" text="free module" */>}}). A **basis** of $F$ is a subset $B\subseteq F$ such that every $x\in F$ can be written uniquely as a finite sum
\[
x=\sum_{b\in B} r_b\, b
\]
with coefficients $r_b\in R$, where all but finitely many $r_b$ are zero. Uniqueness is equivalent to the familiar notions of {{</* knowl id="linear-independence" text="linear independence" */>}} and spanning (compare {{</* knowl id="linear-combination" text="linear combinations" */>}} in linear algebra).

Bases generalize the concept of a basis in a {{</* knowl id="vector-space" text="vector space" */>}}, but over rings bases can fail to exist even for finitely generated modules.

**Examples:**
- The standard vectors $e_1,\dots,e_n$ form a basis of $R^n$.
- $\{1\}$ is a basis of the free $R$-module $R$.
- (Nonexample) The $\mathbb Z$-module $\mathbb Z/2\mathbb Z$ has no basis, so it is not free.
