+++
id = "lie-groups/ideal-lie-algebra"
title = "Ideal in a Lie algebra"
kind = "knowl"
summary = "A Lie subalgebra stable under bracketing with the whole algebra."
aliases = ["ideal-lie-algebra", "Ideal in a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/ideal-lie-algebra.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]].

**Definition (Ideal).**
A linear subspace $\mathfrak i\subseteq \mathfrak g$ is an **ideal** if it is a [[lie-groups/lie-subalgebra|Lie subalgebra]] and
\[
[\mathfrak g,\mathfrak i]\subseteq \mathfrak i.
\]
Equivalently, $\mathfrak i$ is stable under the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint action]]: for every $x\in\mathfrak g$, the endomorphism $\mathrm{ad}_x$ maps $\mathfrak i$ into itself.

**Basic consequences.**

- If $\phi:\mathfrak g\to\mathfrak h$ is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]], then $\ker\phi$ is an ideal.
- If $\mathfrak i$ is an ideal, the quotient vector space $\mathfrak g/\mathfrak i$ carries a natural [[lie-groups/quotient-lie-algebra|quotient Lie algebra]] structure.

**Examples.**
The [[lie-groups/center-of-a-lie-algebra|center]] $Z(\mathfrak g)$ is an ideal, and the [[lie-groups/derived-subalgebra|derived subalgebra]] $[\mathfrak g,\mathfrak g]$ is an ideal (see [[lie-groups/derived-subalgebra-is-ideal-lemma|the ideal lemma]]).

**Context.**
Ideals play the role of normal subgroups in Lie theory and are central in structure results such as the [[lie-groups/levi-decomposition-theorem|Levi decomposition]].
