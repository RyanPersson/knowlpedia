---
title: "Ideal in a Lie algebra"
description: "A Lie subalgebra stable under bracketing with the whole algebra."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

**Definition (Ideal).**  
A linear subspace $\mathfrak i\subseteq \mathfrak g$ is an **ideal** if it is a {{< knowl id="lie-subalgebra" text="Lie subalgebra" >}} and
\[
[\mathfrak g,\mathfrak i]\subseteq \mathfrak i.
\]
Equivalently, $\mathfrak i$ is stable under the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint action" >}}: for every $x\in\mathfrak g$, the endomorphism $\mathrm{ad}_x$ maps $\mathfrak i$ into itself.

**Basic consequences.**

- If $\phi:\mathfrak g\to\mathfrak h$ is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}, then $\ker\phi$ is an ideal.
- If $\mathfrak i$ is an ideal, the quotient vector space $\mathfrak g/\mathfrak i$ carries a natural {{< knowl id="quotient-lie-algebra" text="quotient Lie algebra" >}} structure.

**Examples.**  
The {{< knowl id="center-of-a-lie-algebra" text="center" >}} $Z(\mathfrak g)$ is an ideal, and the {{< knowl id="derived-subalgebra" text="derived subalgebra" >}} $[\mathfrak g,\mathfrak g]$ is an ideal (see {{< knowl id="derived-subalgebra-is-ideal-lemma" text="the ideal lemma" >}}).

**Context.**  
Ideals play the role of normal subgroups in Lie theory and are central in structure results such as the {{< knowl id="levi-decomposition-theorem" text="Levi decomposition" >}}.
