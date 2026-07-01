+++
id = "measure-theory/ae-equality"
title = "Almost-everywhere equality"
kind = "knowl"
summary = "Two functions are a.e. equal if they differ only on a null set."
aliases = ["ae-equality", "Almost-everywhere equality"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/ae-equality.md"
+++

An **almost-everywhere equality** (or **a.e. equality**) on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is the relation on functions $f,g:X\to \overline{\mathbb R}$ defined by
\[
f=g \text{ a.e.} \quad \Longleftrightarrow \quad \mu(\{x\in X: f(x)\neq g(x)\})=0.
\]
Equivalently, the set where $f$ and $g$ disagree is a [[measure-theory/null-set|null set]].

This formalizes equality [[measure-theory/almost-everywhere|almost everywhere]] and gives an [[shared-foundations/equivalence-relation|equivalence relation]] on (for instance) the collection of [[measure-theory/measurable-function|measurable functions]]. Many constructions in integration theory and spaces such as [[measure-theory/lp-space|Lp spaces]] treat functions as identical whenever they are a.e. equal.

**Examples:**
- On $\mathbb R$ equipped with the [[measure-theory/borel-sigma-algebra|Borel sigma-algebra]] and [[measure-theory/lebesgue-measure|Lebesgue measure]], the functions $f=0$ and $g=\mathbf{1}_{\{0\}}$ are a.e. equal.
- If $E\subseteq X$ is a null set and $f$ is measurable, then $f$ and the function obtained by redefining $f$ arbitrarily on $E$ are a.e. equal.
