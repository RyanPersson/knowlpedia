+++
id = "shared-foundations/function"
title = "Function"
kind = "knowl"
summary = "A relation that assigns each input exactly one output"
aliases = ["function"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/function.md"
+++

A **function** is a [[shared-foundations/relation|relation]] $f\subseteq A\times B$ between [[shared-foundations/set|sets]] $A$ and $B$ such that for every $a\in A$ there exists a unique $b\in B$ with $(a,b)\in f$; we write this $b$ as $f(a)$ and denote the function by $f:A\to B$.

The set $A$ is called the [[shared-foundations/domain|domain]] and the set $B$ the [[shared-foundations/codomain|codomain]]. Functions allow you to form [[shared-foundations/image|images]] and [[shared-foundations/preimage|preimages]] of subsets and to build new functions via [[shared-foundations/composition|composition]].

**Examples:**
- The squaring map $f:\mathbb{N}\to\mathbb{N}$ given by $f(n)=n^2$ is a function on the [[shared-foundations/natural-numbers|natural numbers]].
- If $S$ is a [[shared-foundations/subset|subset]] of a set $A$, the inclusion map $i:S\to A$ defined by $i(s)=s$ is a function.
