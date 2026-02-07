---
title: "Solvable Lie algebra"
description: "A Lie algebra whose derived series eventually becomes zero; the Lie-algebra analogue of solvable groups."
---

Let $\mathfrak g$ be a Lie algebra. Define its derived series (see {{< knowl id="derived-series-lie-algebra" text="derived series" >}}) by
\[
\mathfrak g^{(0)}=\mathfrak g,\qquad \mathfrak g^{(k+1)}=[\mathfrak g^{(k)},\mathfrak g^{(k)}],
\]
where $[\cdot,\cdot]$ denotes the {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}} and each derived algebra is an ideal (compare {{< knowl id="derived-subalgebra" text="derived subalgebra" >}} and {{< knowl id="derived-subalgebra-is-ideal-lemma" text="it is an ideal" >}}).

The Lie algebra $\mathfrak g$ is **solvable** if there exists $n$ such that
\[
\mathfrak g^{(n)}=0.
\]
Equivalently, iterated commutators eventually vanish. This notion is central in the structure theory of general Lie algebras: the maximal solvable ideal is the radical, and the {{< knowl id="levi-decomposition-theorem" text="Levi decomposition" >}} splits any finite-dimensional Lie algebra (in characteristic $0$) into a semisimple part and a solvable part.

There are several important tests and relations:

- Cartan’s criterion gives a practical characterization in many settings (see {{< knowl id="cartans-criterion-solvability" text="Cartan’s criterion for solvability" >}} and {{< knowl id="tfae-solvability-lie-algebra" text="equivalent conditions for solvability" >}}).
- Every {{< knowl id="nilpotent-lie-algebra" text="nilpotent Lie algebra" >}} is solvable (see {{< knowl id="nilpotent-implies-solvable-lemma" text="nilpotent implies solvable" >}}), but not conversely.
