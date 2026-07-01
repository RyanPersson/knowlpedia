+++
id = "lie-groups/killing-form-ad-invariant-lemma"
title = "Ad-invariance of the Killing form"
kind = "knowl"
summary = "The Killing form satisfies B([x,y],z)=B(x,[y,z])."
aliases = ["killing-form-ad-invariant-lemma", "Ad-invariance of the Killing form"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/killing-form-ad-invariant-lemma.md"
+++

Let $\mathfrak g$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic $0$, and let $B$ be its [[lie-groups/killing-form|Killing form]]:
\[
B(x,y)=\mathrm{tr}(\mathrm{ad}_x\mathrm{ad}_y).
\]

**Lemma (ad-invariance).**
For all $x,y,z\in\mathfrak g$,
\[
B([x,y],z)=B(x,[y,z]).
\]
Equivalently, $B(\mathrm{ad}_y x,z)+B(x,\mathrm{ad}_y z)=0$, i.e. each $\mathrm{ad}_y$ is skew-adjoint with respect to $B$.


**Context.**
Ad-invariance is the structural feature that makes the Killing form useful in studying ideals and decompositions; it is crucial in the proof that [[lie-groups/killing-form-nondegenerate-iff-semisimple|nondegeneracy of B is equivalent to semisimplicity]].
