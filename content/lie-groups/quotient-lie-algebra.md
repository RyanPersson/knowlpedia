---
title: "Quotient Lie algebra"
description: "If i is an ideal in g, then g/i inherits a canonical Lie bracket."
---

Let $\mathfrak g$ be a Lie algebra (see {{< knowl id="lie-algebra" text="Lie algebra" >}}) and let $\mathfrak i\subseteq \mathfrak g$ be an ideal (see {{< knowl id="ideal-lie-algebra" text="ideal" >}}). The **quotient Lie algebra** $\mathfrak g/\mathfrak i$ is the vector space quotient equipped with the bracket
\[
[x+\mathfrak i,\; y+\mathfrak i]\;:=\;[x,y]+\mathfrak i.
\]
This is well-defined precisely because $\mathfrak i$ is an ideal: changing representatives adds elements of $\mathfrak i$, and brackets with elements of $\mathfrak i$ stay in $\mathfrak i$.

The projection map $\pi:\mathfrak g\to \mathfrak g/\mathfrak i$ is a Lie algebra homomorphism (see {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}) with kernel $\mathfrak i$. It satisfies the universal property: any Lie algebra homomorphism $f:\mathfrak g\to \mathfrak h$ with $\mathfrak i\subseteq \ker(f)$ factors uniquely through $\pi$.

Quotients appear constantly in structure theory. For example, the {{< knowl id="derived-subalgebra" text="derived subalgebra" >}} $[\mathfrak g,\mathfrak g]$ is an ideal (see {{< knowl id="derived-subalgebra-is-ideal-lemma" text="derived subalgebra is an ideal" >}}), so the abelianization $\mathfrak g/[\mathfrak g,\mathfrak g]$ is a quotient Lie algebra. On the group side, quotients by normal subgroups (see {{< knowl id="quotient-lie-group" text="quotient Lie group" >}}) differentiate to quotient Lie algebras under mild hypotheses (see {{< knowl id="differential-is-lie-algebra-homomorphism" text="differential is a Lie algebra homomorphism" >}}).
