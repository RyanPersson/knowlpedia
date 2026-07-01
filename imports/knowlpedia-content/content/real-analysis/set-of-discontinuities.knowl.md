+++
id = "real-analysis/set-of-discontinuities"
title = "Set of discontinuities"
kind = "knowl"
summary = "The set of points where a function is discontinuous."
aliases = ["set-of-discontinuities", "Set of discontinuities"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/set-of-discontinuities.md"
+++

A **set of discontinuities** of a [[shared-foundations/function|function]] $f:E\to\mathbb R$, where $E\subseteq\mathbb R$, is the set
\[
D(f)=\{x\in E : f \text{ is not continuous at } x\}.
\]
Equivalently, $x\in D(f)$ exactly when $x$ is a [[real-analysis/discontinuity-point|discontinuity point]] of $f$.

This set is central in [[real-analysis/riemann-integrable-function|Riemann integrability]]; for bounded functions on an interval, integrability can be characterized in terms of how “small” $D(f)$ is (see the [[measure-theory/lebesgue-criterion-for-riemann-integrability|Lebesgue criterion for Riemann integrability]]).

**Examples:**
- If $f$ is continuous on $[a,b]$, then $D(f)$ is the [[shared-foundations/empty-set|empty set]].
- On $[a,b]$, let $f$ be the [[measure-theory/indicator-function|indicator function]] of $\mathbb Q\cap[a,b]$. Then $D(f)=[a,b]$.
