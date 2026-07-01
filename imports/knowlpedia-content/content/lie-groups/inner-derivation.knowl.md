+++
id = "lie-groups/inner-derivation"
title = "Inner derivation"
kind = "knowl"
summary = "A derivation of the form ad_x(y) = [x,y]."
aliases = ["inner-derivation", "Inner derivation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/inner-derivation.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]]. Recall that a [[lie-groups/derivation-lie-algebra|derivation]] is a linear map $D:\mathfrak g\to\mathfrak g$ satisfying the Leibniz rule
\[
D([x,y])=[D(x),y]+[x,D(y)].
\]

**Definition (Inner derivation).**
For each $x\in\mathfrak g$, the map
\[
\mathrm{ad}_x:\mathfrak g\to\mathfrak g,\qquad \mathrm{ad}_x(y)=[x,y]
\]
is a derivation. A derivation is called **inner** if it equals $\mathrm{ad}_x$ for some $x\in\mathfrak g$.

The assignment $x\mapsto \mathrm{ad}_x$ is the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] $\mathrm{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g)$, and the space of inner derivations is $\mathrm{ad}(\mathfrak g)\subseteq \mathrm{Der}(\mathfrak g)$.

**Key relation to the center.**
The kernel of $\mathrm{ad}$ is exactly the [[lie-groups/center-of-a-lie-algebra|center]] (see [[lie-groups/kernel-of-ad-small-is-center-lemma|the kernel-of-ad lemma]]), so inner derivations detect noncentral directions.

**Context.**
Derivations modulo inner derivations measure “outer” symmetries of $\mathfrak g$ (compare [[lie-groups/outer-derivation|outer derivations]]), and exponentiating $\mathrm{ad}_x$ is the infinitesimal source of many [[lie-groups/lie-algebra-automorphism|automorphisms]].
