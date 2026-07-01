+++
id = "shared-foundations/injective-function"
title = "Injective function"
kind = "knowl"
summary = "A function that never takes the same value on two different inputs"
aliases = ["injective-function", "Injective function"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/injective-function.md"
+++

An **injective function** is a [[shared-foundations/function|function]] $f:A\to B$ such that whenever $f(a_1)=f(a_2)$, it follows that $a_1=a_2$.

Injectivity means distinct elements of the [[shared-foundations/domain|domain]] remain distinct after applying $f$. In terms of [[shared-foundations/cardinality|cardinality]], an injective function from $A$ to $B$ is evidence that $A$ is “no larger than” $B$.

**Examples:**
- The inclusion map $i:S\to A$ of a [[shared-foundations/subset|subset]] is injective, since $i(s)=i(s')$ implies $s=s'$.
- The function $f:\mathbb{Z}\to\mathbb{Z}$ given by $f(n)=2n$ is injective, but it is not surjective onto $\mathbb{Z}$.
