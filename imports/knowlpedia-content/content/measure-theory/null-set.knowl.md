+++
id = "measure-theory/null-set"
title = "Null set"
kind = "knowl"
summary = "A measurable set of measure zero."
aliases = ["null-set", "Null set"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/null-set.md"
+++

A **null set** in a measure space $(X,\Sigma,\mu)$ is a [[measure-theory/measurable-set|measurable set]] $N\in\Sigma$ such that $\mu(N)=0$.

Null sets are negligible for many purposes: statements that fail only on a null set are said to hold [[measure-theory/almost-everywhere|almost everywhere]]. Many constructions treat functions that differ only on a null set as essentially the same.

**Examples:**
- The [[shared-foundations/empty-set|empty set]] is always a null set.
- In $\mathbb R$ with [[measure-theory/lebesgue-measure|Lebesgue measure]], any singleton $\{x\}$ is a null set.
- In $\mathbb R$ with Lebesgue measure, every countable subset of $\mathbb R$ is a null set.
