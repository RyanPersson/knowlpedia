+++
id = "lie-groups/quotient-lie-algebra"
title = "Quotient Lie algebra"
kind = "knowl"
summary = "If i is an ideal in g, then g/i inherits a canonical Lie bracket."
aliases = ["quotient-lie-algebra", "Quotient Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/quotient-lie-algebra.md"
+++

Let $\mathfrak g$ be a Lie algebra (see [[lie-groups/lie-algebra|Lie algebra]]) and let $\mathfrak i\subseteq \mathfrak g$ be an ideal (see [[lie-groups/ideal-lie-algebra|ideal]]). The **quotient Lie algebra** $\mathfrak g/\mathfrak i$ is the vector space quotient equipped with the bracket
\[
[x+\mathfrak i,\; y+\mathfrak i]\;:=\;[x,y]+\mathfrak i.
\]
This is well-defined precisely because $\mathfrak i$ is an ideal: changing representatives adds elements of $\mathfrak i$, and brackets with elements of $\mathfrak i$ stay in $\mathfrak i$.

The projection map $\pi:\mathfrak g\to \mathfrak g/\mathfrak i$ is a Lie algebra homomorphism (see [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]) with kernel $\mathfrak i$. It satisfies the universal property: any Lie algebra homomorphism $f:\mathfrak g\to \mathfrak h$ with $\mathfrak i\subseteq \ker(f)$ factors uniquely through $\pi$.

Quotients appear constantly in structure theory. For example, the [[lie-groups/derived-subalgebra|derived subalgebra]] $[\mathfrak g,\mathfrak g]$ is an ideal (see [[lie-groups/derived-subalgebra-is-ideal-lemma|derived subalgebra is an ideal]]), so the abelianization $\mathfrak g/[\mathfrak g,\mathfrak g]$ is a quotient Lie algebra. On the group side, quotients by normal subgroups (see [[lie-groups/quotient-lie-group|quotient Lie group]]) differentiate to quotient Lie algebras under mild hypotheses (see [[lie-groups/differential-is-lie-algebra-homomorphism|differential is a Lie algebra homomorphism]]).
