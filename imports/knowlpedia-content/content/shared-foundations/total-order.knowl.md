+++
id = "shared-foundations/total-order"
title = "Total order"
kind = "knowl"
summary = "A partial order in which any two elements are comparable."
aliases = ["total-order", "Total order"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/total-order.md"
+++

A **total order** on a [[shared-foundations/set|set]] $X$ is a [[shared-foundations/partial-order|partial order]] $\le$ on $X$ such that for all $a,b\in X$, either $a\le b$ or $b\le a$.

Total orders are also called linear orders. A [[shared-foundations/well-ordered-set|well-ordered set]] is a totally ordered set with the additional property that every nonempty subset has a least element.

**Examples:**
- The usual order $\le$ on $\mathbb{Z}$ (the [[shared-foundations/integers|integers]]) is a total order.
- (Lexicographic order) If $X$ and $Y$ are totally ordered, define an order on $X\times Y$ by $(x,y)\le_{\mathrm{lex}}(x',y')$ if either $x<x'$, or $x=x'$ and $y\le y'$ (where $x<x'$ means $x\le x'$ and $x\ne x'$). This gives a total order on the [[shared-foundations/cartesian-product|Cartesian product]] $X\times Y$.
