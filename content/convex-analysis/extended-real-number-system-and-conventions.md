---
title: "Extended real number system and conventions"
description: "Conventions for inf/sup and extended-real-valued functions used in convex analysis"
---

The **extended real number system** is
$$
\overline{\mathbb{R}}:=\mathbb{R}\cup\{-\infty,\infty\}.
$$
In the notes, for convex analysis it is convenient to work mostly with the one-sided extension
$$
\mathbb{R}:=(-\infty,\infty]=\mathbb{R}\cup\{\infty\},
$$

so that expressions like $-\infty+\infty$ never arise.

**Infimum/supremum conventions (in $\overline{\mathbb{R}}$).**
- $-\infty$ is a lower bound of every subset; every nonempty set has a greatest lower bound.
- If a nonempty set is not bounded below, its infimum is $-\infty$.
- By convention, $\inf\emptyset=\infty$.
- $\infty$ is an upper bound of every subset; every nonempty set has a least upper bound.
- If a nonempty set is not bounded above, its supremum is $\infty$.
- By convention, $\sup\emptyset=-\infty$.

**Context.** Allowing the value $\infty$ lets one encode constraints by penalties (e.g., the {{< knowl id="indicator-function-of-a-set" text="indicator function" >}}) and avoid repeatedly restricting domains by hand.
