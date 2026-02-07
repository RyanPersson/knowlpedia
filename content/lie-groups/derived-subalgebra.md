---
title: "Derived subalgebra"
description: "The Lie subalgebra spanned by commutators; it measures how far is from abelian."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

The **derived subalgebra** (or commutator subalgebra) of $\mathfrak g$ is
\[
[\mathfrak g,\mathfrak g] := \mathrm{span}\{[x,y] : x,y\in \mathfrak g\}\subseteq \mathfrak g.
\]
It is a Lie subalgebra, and in fact an {{< knowl id="ideal-lie-algebra" text="ideal" >}}; the ideal property is recorded explicitly in {{< knowl id="derived-subalgebra-is-ideal-lemma" text="the lemma that $[\mathfrak g,\mathfrak g]$ is an ideal" >}}.

## Basic consequences
- $\mathfrak g$ is {{< knowl id="abelian-lie-algebra" text="abelian" >}} iff $[\mathfrak g,\mathfrak g]=0$.
- The quotient $\mathfrak g/[\mathfrak g,\mathfrak g]$ is the **abelianization** of $\mathfrak g$ (a special case of {{< knowl id="quotient-lie-algebra" text="quotient Lie algebra" >}}).
- $\mathfrak g$ is called **perfect** if $[\mathfrak g,\mathfrak g]=\mathfrak g$; for example, any {{< knowl id="simple-lie-algebra" text="simple Lie algebra" >}} is perfect.

## Context
The derived subalgebra is the first step in the {{< knowl id="derived-series-lie-algebra" text="derived series" >}}, which detects solvability and organizes many structure theorems such as the {{< knowl id="levi-decomposition-theorem" text="Levi decomposition" >}}.
