+++
id = "topology/nowhere-dense-set"
title = "Nowhere dense set"
kind = "knowl"
summary = "A set whose closure has empty interior"
aliases = ["nowhere-dense-set", "Nowhere dense set"]
domains = ["topology"]
legacy_source_path = "topology/nowhere-dense-set.md"
+++

A **nowhere dense set** in a [[topology/topological-space|topological space]] $X$ is a [[shared-foundations/subset|subset]] $A\subseteq X$ such that the [[topology/interior|interior]] of its [[topology/closure|closure]] is [[shared-foundations/empty-set|empty]], i.e. $\operatorname{int}(\overline{A})=\varnothing$.

Equivalently, $A$ is nowhere dense if $\overline{A}$ contains no nonempty [[topology/open-set|open set]]. Nowhere dense sets are the basic building blocks of [[topology/meager-set|meager sets]] in the [[topology/baire-space|Baire category]] viewpoint.

**Examples:**
- The set of integers $\mathbb{Z}\subseteq \mathbb{R}$ (with the usual topology) is nowhere dense: it is [[topology/closed-set|closed]] and has empty interior.
- The set $\{1/n : n\in\mathbb{N}\}\subseteq \mathbb{R}$ is nowhere dense: its closure is $\{1/n:n\in\mathbb{N}\}\cup\{0\}$, which has empty interior.
