---
title: "Almost-everywhere equality"
description: "Two functions are a.e. equal if they differ only on a null set."
---

An **almost-everywhere equality** (or **a.e. equality**) on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ is the relation on functions $f,g:X\to \overline{\mathbb R}$ defined by
\[
f=g \text{ a.e.} \quad \Longleftrightarrow \quad \mu(\{x\in X: f(x)\neq g(x)\})=0.
\]
Equivalently, the set where $f$ and $g$ disagree is a {{< knowl id="null-set" text="null set" >}}.

This formalizes equality {{< knowl id="almost-everywhere" text="almost everywhere" >}} and gives an {{< knowl id="equivalence-relation" section="shared-foundations" text="equivalence relation" >}} on (for instance) the collection of {{< knowl id="measurable-function" text="measurable functions" >}}. Many constructions in integration theory and spaces such as {{< knowl id="lp-space" text="Lp spaces" >}} treat functions as identical whenever they are a.e. equal.

**Examples:**
- On $\mathbb R$ equipped with the {{< knowl id="borel-sigma-algebra" text="Borel sigma-algebra" >}} and {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}}, the functions $f=0$ and $g=\mathbf{1}_{\{0\}}$ are a.e. equal.
- If $E\subseteq X$ is a null set and $f$ is measurable, then $f$ and the function obtained by redefining $f$ arbitrarily on $E$ are a.e. equal.
