---
title: "Set of discontinuities"
description: "The set of points where a function is discontinuous."
---

A **set of discontinuities** of a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:E\to\mathbb R$, where $E\subseteq\mathbb R$, is the set
\[
D(f)=\{x\in E : f \text{ is not continuous at } x\}.
\]
Equivalently, $x\in D(f)$ exactly when $x$ is a {{< knowl id="discontinuity-point" text="discontinuity point" >}} of $f$.

This set is central in {{< knowl id="riemann-integrable-function" text="Riemann integrability" >}}; for bounded functions on an interval, integrability can be characterized in terms of how “small” $D(f)$ is (see the {{< knowl id="lebesgue-criterion-for-riemann-integrability" section="measure-theory" text="Lebesgue criterion for Riemann integrability" >}}).

**Examples:**
- If $f$ is continuous on $[a,b]$, then $D(f)$ is the {{< knowl id="empty-set" section="shared-foundations" text="empty set" >}}.
- On $[a,b]$, let $f$ be the {{< knowl id="indicator-function" section="measure-theory" text="indicator function" >}} of $\mathbb Q\cap[a,b]$. Then $D(f)=[a,b]$.
