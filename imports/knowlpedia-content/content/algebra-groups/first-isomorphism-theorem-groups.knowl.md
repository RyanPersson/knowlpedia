+++
id = "algebra-groups/first-isomorphism-theorem-groups"
title = "First Isomorphism Theorem (Groups)"
kind = "knowl"
summary = "A homomorphism factors through the quotient by its kernel, giving G/ker(f) ≅ im(f)"
aliases = ["first-isomorphism-theorem-groups", "First Isomorphism Theorem (Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/first-isomorphism-theorem-groups.md"
+++

**First Isomorphism Theorem (Groups).**
Let $G$ and $H$ be [[algebra-groups/group|groups]], and let $f: G \to H$ be a [[algebra-groups/group-homomorphism|group homomorphism]]. Let $K = \ker(f)$ be the [[algebra-groups/kernel-group|kernel]] of $f$ and let $I = \operatorname{im}(f)$ be the [[algebra-groups/image-group|image]] of $f$, i.e.
$$
K = \{g \in G : f(g) = e_H\}, \qquad I = \{f(g) : g \in G\}.
$$

Then $K$ is a [[algebra-groups/normal-subgroup|normal subgroup]] of $G$ (see [[algebra-groups/kernels-are-normal|kernels are normal subgroups]]), and the induced map
$$
\bar f: G/K \to I, \qquad \bar f(gK) = f(g),
$$

is a well-defined [[algebra-groups/group-isomorphism|isomorphism]]. In particular, if $f$ is surjective then $G/K \cong H$.

This result is the basic "quotient = image" principle and is the prototype for the [[algebra-groups/second-isomorphism-theorem-groups|second]] and [[algebra-groups/third-isomorphism-theorem-groups|third isomorphism theorems]]. It is often packaged as an [[algebra-groups/exact-sequence-groups|exact sequence]] $1 \to K \to G \to I \to 1$.
