+++
id = "lie-groups/killing-form-nondegenerate-iff-semisimple"
title = "Killing form nondegeneracy criterion"
kind = "knowl"
summary = "A finite-dimensional Lie algebra is semisimple iff its Killing form is nondegenerate."
aliases = ["killing-form-nondegenerate-iff-semisimple", "Killing form nondegeneracy criterion"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/killing-form-nondegenerate-iff-semisimple.md"
+++

Let $\mathfrak g$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic $0$, and let $B$ be its [[lie-groups/killing-form|Killing form]].

**Theorem (Cartan criterion via Killing form).**
$\mathfrak g$ is [[lie-groups/semisimple-lie-algebra|semisimple]] if and only if the Killing form $B$ is nondegenerate.

**Comments on the proof.**

- If $\mathfrak g$ is semisimple, then the adjoint representation is faithful modulo the center (see [[lie-groups/kernel-of-ad-small-is-center-lemma|ker(ad)=center]] and [[lie-groups/simple-lie-algebra-trivial-center|trivial center for simple algebras]]), and complete reducibility arguments show that the invariant form $B$ must be nondegenerate.
- Conversely, if $B$ is nondegenerate, then any solvable ideal forces degeneracy: the [[lie-groups/levi-decomposition-theorem|radical]] (maximal [[lie-groups/solvable-lie-algebra|solvable]] ideal) lies in the radical of $B$, so nondegeneracy implies the radical is zero, hence $\mathfrak g$ is semisimple.

**Context.**
This theorem is often presented alongside [[lie-groups/cartans-criterion-semisimplicity|Cartan’s criterion]] and is a key structural tool in the study of semisimple algebras and their representations.
