---
title: "Derived subalgebra is an ideal"
description: "For any Lie algebra , the commutator subalgebra is an ideal of ."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

## Lemma
The {{< knowl id="derived-subalgebra" text="derived subalgebra" >}} $[\mathfrak g,\mathfrak g]$ is an {{< knowl id="ideal-lie-algebra" text="ideal" >}} in $\mathfrak g$; equivalently,
\[
[\mathfrak g,\,[\mathfrak g,\mathfrak g]] \subseteq [\mathfrak g,\mathfrak g].
\]

## Proof
Take $x\in\mathfrak g$ and an element of $[\mathfrak g,\mathfrak g]$ of the form $[y,z]$. Using the Jacobi identity for the {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}},
\[
[x,[y,z]] = [[x,y],z] + [y,[x,z]].
\]
Each term on the right is a commutator of two elements of $\mathfrak g$, hence lies in $[\mathfrak g,\mathfrak g]$. By linearity, $[x,w]\in[\mathfrak g,\mathfrak g]$ for all $w\in[\mathfrak g,\mathfrak g]$, proving the claim.

**Context.** This lemma ensures that iterating $[\cdot,\cdot]$ produces characteristic ideals (e.g. the {{< knowl id="derived-series-lie-algebra" text="derived series" >}}), making solvability a robust isomorphism-invariant notion.
