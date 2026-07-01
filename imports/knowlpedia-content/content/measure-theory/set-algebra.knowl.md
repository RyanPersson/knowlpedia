+++
id = "measure-theory/set-algebra"
title = "Set algebra"
kind = "knowl"
summary = "A collection of subsets closed under complements and finite unions."
aliases = ["set-algebra", "Set algebra"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/set-algebra.md"
+++

A **set algebra** on a set $X$ is a nonempty collection $\mathcal A \subseteq \mathcal P(X)$ such that if $A\in\mathcal A$ then $X\setminus A\in\mathcal A$, and if $A,B\in\mathcal A$ then $A\cup B\in\mathcal A$.

Here $\mathcal P(X)$ is the [[shared-foundations/power-set|power set]] of the [[shared-foundations/set|set]] $X$. Closure under complements and finite unions implies closure under finite [[shared-foundations/intersection|intersections]] and finite [[shared-foundations/set-difference|set differences]]. A set algebra is the typical domain for a [[measure-theory/premeasure|premeasure]], and every [[measure-theory/sigma-algebra|sigma-algebra]] is a set algebra.

**Examples:**
- For any $X$, the full collection $\mathcal P(X)$ is a set algebra.
- The family of subsets of $\mathbb R$ that are finite unions of half-open [[real-analysis/interval|intervals]] of the form $[a,b)$ is a set algebra.
- On an infinite set $X$, the collection of all finite subsets of $X$ together with all cofinite subsets of $X$ (those whose complement is finite) is a set algebra.
