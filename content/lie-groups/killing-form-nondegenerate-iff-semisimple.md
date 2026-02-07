---
title: "Killing form nondegeneracy criterion"
description: "A finite-dimensional Lie algebra is semisimple iff its Killing form is nondegenerate."
---

Let $\mathfrak g$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}} over a field of characteristic $0$, and let $B$ be its {{< knowl id="killing-form" text="Killing form" >}}.

**Theorem (Cartan criterion via Killing form).**  
$\mathfrak g$ is {{< knowl id="semisimple-lie-algebra" text="semisimple" >}} if and only if the Killing form $B$ is nondegenerate.

**Comments on the proof.**

- If $\mathfrak g$ is semisimple, then the adjoint representation is faithful modulo the center (see {{< knowl id="kernel-of-ad-small-is-center-lemma" text="ker(ad)=center" >}} and {{< knowl id="simple-lie-algebra-trivial-center" text="trivial center for simple algebras" >}}), and complete reducibility arguments show that the invariant form $B$ must be nondegenerate.
- Conversely, if $B$ is nondegenerate, then any solvable ideal forces degeneracy: the {{< knowl id="levi-decomposition-theorem" text="radical" >}} (maximal {{< knowl id="solvable-lie-algebra" text="solvable" >}} ideal) lies in the radical of $B$, so nondegeneracy implies the radical is zero, hence $\mathfrak g$ is semisimple.

**Context.**  
This theorem is often presented alongside {{< knowl id="cartans-criterion-semisimplicity" text="Cartan’s criterion" >}} and is a key structural tool in the study of semisimple algebras and their representations.
