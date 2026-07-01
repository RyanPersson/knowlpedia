+++
id = "lie-groups/simple-lie-algebra-trivial-center"
title = "Center of a simple Lie algebra is trivial"
kind = "knowl"
summary = "A simple Lie algebra has zero center, since the center is always an ideal."
aliases = ["simple-lie-algebra-trivial-center", "Center of a simple Lie algebra is trivial"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/simple-lie-algebra-trivial-center.md"
+++

Let $\mathfrak g$ be a [[lie-groups/simple-lie-algebra|simple Lie algebra]]. Then its center is trivial:
\[
Z(\mathfrak g)=\{0\},
\]
where $Z(\mathfrak g)$ denotes the [[lie-groups/center-of-a-lie-algebra|center of a Lie algebra]].

**Reason.** The center $Z(\mathfrak g)=\{z\in\mathfrak g:[z,x]=0\ \forall x\in\mathfrak g\}$ is always an ideal: if $z$ commutes with everything, then so does $[x,z]=0$ for any $x$, and invariance under brackets is automatic (this is a special case of the general “invariance under adjoint action” viewpoint). Since $\mathfrak g$ is simple, $Z(\mathfrak g)$ must be either $0$ or all of $\mathfrak g$. If $Z(\mathfrak g)=\mathfrak g$, then $\mathfrak g$ is abelian, contradicting the definition of simple.

This fact is often used when comparing simplicity to semisimplicity (see [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]]) and when analyzing the kernel of adjoint representations (compare [[lie-groups/kernel-of-ad-is-center-lemma|kernel of ad is the center]]).
