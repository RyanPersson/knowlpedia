---
title: "Irreducible representation of a Lie group"
description: "A group representation with no nontrivial invariant subspaces."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} and let $\pi:G\to \mathrm{GL}(V)$ be a (finite-dimensional) {{< knowl id="representation-of-a-lie-group" text="representation" >}}.

**Definition (Irreducible).**  
The representation $(\pi,V)$ is **irreducible** if the only $G$-invariant subspaces of $V$ are $\{0\}$ and $V$, i.e. there is no proper nonzero subspace $W\subset V$ with $\pi(g)W\subseteq W$ for all $g\in G$.

**Link with the Lie algebra (connected case).**  
Assume $G$ is connected and let $d\pi:\mathfrak g\to \mathfrak{gl}(V)$ be the differential representation (compare {{< knowl id="differential-is-lie-algebra-homomorphism" text="differentiation is a Lie algebra homomorphism" >}}). Then a subspace $W\subset V$ is $G$-invariant if and only if it is invariant under $d\pi(\mathfrak g)$. Consequently, for connected $G$, irreducibility of $\pi$ is equivalent to irreducibility of the induced {{< knowl id="irreducible-representation-lie-algebra" text="Lie algebra representation" >}} $(d\pi,V)$.

**Context.**  
For compact connected groups, irreducible unitary representations are classified by highest weights (see {{< knowl id="highest-weight-theorem" text="highest-weight theorem" >}} and {{< knowl id="peter-weyl-theorem" text="Peter–Weyl" >}}).
