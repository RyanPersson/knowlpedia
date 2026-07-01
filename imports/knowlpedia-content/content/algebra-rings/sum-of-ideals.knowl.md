+++
id = "algebra-rings/sum-of-ideals"
title = "Sum of ideals"
kind = "knowl"
summary = "The ideal consisting of all sums of an element from each of two ideals."
aliases = ["sum-of-ideals", "Sum of ideals"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/sum-of-ideals.md"
+++

Given ideals $I,J$ in a [[algebra-rings/ring|ring]] $R$, their **sum** is
\[
I+J=\{\,i+j : i\in I,\ j\in J\,\}.
\]
It is the smallest [[algebra-rings/ideal|ideal]] of $R$ containing both $I$ and $J$.

The sum interacts with quotients via the [[algebra-rings/second-isomorphism-theorem-rings|second isomorphism theorem]] and measures “comaximality” when $I+J=R$. In $\mathbb Z$, sums of ideals encode the [[algebra-rings/gcd|gcd]].

**Examples:**
- In $\mathbb Z$, $(m)+(n)=(\gcd(m,n))$.
- In $k[x,y]$, $(x)+(y)=(x,y)$.
- If $I\subseteq J$, then $I+J=J$.
