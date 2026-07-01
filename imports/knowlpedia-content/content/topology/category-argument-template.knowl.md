+++
id = "topology/category-argument-template"
title = "Category Argument Template"
kind = "knowl"
summary = "A standard Baire category method for producing a dense or residual set by intersecting dense open sets."
aliases = ["category-argument-template", "Category Argument Template"]
domains = ["topology"]
legacy_source_path = "topology/category-argument-template.md"
+++

**Category argument template:** Let $X$ be a [[topology/baire-space|Baire space]] and let $U_1,U_2,\dots \subseteq X$ be sets that are each [[topology/open-set|open]] and [[topology/dense-set|dense]] in $X$. Then the intersection $\bigcap_{n=1}^\infty U_n$ is dense (in particular, nonempty) in $X$, and it is a [[topology/residual-set|residual set]] since its complement is a countable union of [[topology/nowhere-dense-set|nowhere dense sets]].

Conceptually, this packages the [[topology/baire-category-theorem|Baire category theorem]] into a reusable method: encode the $n$th requirement of a property as membership in a dense open set $U_n$, and then conclude that there are points satisfying all requirements at once (finite versions rely only on [[topology/intersection-of-dense-open-is-dense|intersection of dense open sets being dense]]).
