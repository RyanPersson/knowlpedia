+++
id = "shared-foundations/relation"
title = "Relation"
kind = "knowl"
summary = "A set of ordered pairs encoding which elements are related."
aliases = ["relation"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/relation.md"
+++

A **relation** from a set $A$ to a set $B$ is a set $R$ with
$$
R\subseteq A\times B,
$$

where $A\times B$ is the [[shared-foundations/cartesian-product|Cartesian product]]. If $(a,b)\in R$, one often writes $a\,R\,b$.

A relation **on** a set $A$ means a relation from $A$ to itself, i.e. a subset of $A\times A$. Special kinds of relations include [[shared-foundations/equivalence-relation|equivalence relations]], which encode “having the same type” in a precise sense.

**Examples:**
- The “less than or equal to” relation on $\mathbb{Z}$ is $R=\{(m,n)\in\mathbb{Z}\times\mathbb{Z}: m\le n\}$.
- For any set $A$, the equality relation on $A$ is $\{(a,a): a\in A\}\subseteq A\times A$.
