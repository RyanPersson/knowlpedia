+++
id = "measure-theory/almost-everywhere"
title = "Almost everywhere"
kind = "knowl"
summary = "Holding except on a set of measure zero."
aliases = ["almost-everywhere", "Almost everywhere"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/almost-everywhere.md"
+++

A property $P(x)$ is said to hold **almost everywhere** (with respect to a measure $\mu$ on $X$) if there exists a [[measure-theory/null-set|null set]] $N\subseteq X$ such that $P(x)$ holds for all $x\in X\setminus N$.

This notion depends on the underlying [[measure-theory/measure-space|measure space]] and is weaker than pointwise validity: changing a function on a null set does not affect almost-everywhere statements. It is also closely tied to the [[shared-foundations/symmetric-difference|symmetric difference]] of sets.

**Examples:**
- Two functions $f,g:X\to\mathbb R$ are equal almost everywhere if $\{x\in X: f(x)\ne g(x)\}$ is a null set.
- For measurable sets $A,B\in\Sigma$, the indicator functions $\mathbf 1_A$ and $\mathbf 1_B$ are equal almost everywhere exactly when $A\triangle B$ is a null set.
