---
title: "Weight of a representation"
description: "A functional occurring as a simultaneous eigenvalue for the action of a Cartan subalgebra."
---

### Definition
Let $\mathfrak g$ be a finite-dimensional complex semisimple Lie algebra (see {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebras" >}}) and let $\mathfrak h\subset \mathfrak g$ be a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}. For a representation $\rho:\mathfrak g\to \mathfrak{gl}(V)$, a linear functional $\lambda\in \mathfrak h^\ast$ is called a **weight** of $V$ if the corresponding {{< knowl id="weight-space" text="weight space" >}}
$$
V_\lambda=\{v\in V\mid \rho(H)v=\lambda(H)v\ \text{for all }H\in\mathfrak h\}
$$
is nonzero.

Equivalently, $\lambda$ is a weight if there exists $0\neq v\in V$ such that every $H\in\mathfrak h$ acts on $v$ by the scalar $\lambda(H)$ (so $v$ is a simultaneous eigenvector for the commuting family $\rho(\mathfrak h)$).

### Context
Weights organize the representation theory of semisimple Lie algebras: the set of weights (with multiplicities $\dim V_\lambda$) encodes much of $V$, and irreducible representations are classified by their {{< knowl id="highest-weight" text="highest weight" >}} (see {{< knowl id="highest-weight-theorem" text="the highest-weight theorem" >}}). The ambient space where weights live is explained in {{< knowl id="weights-in-dual-cartan" text="weights in the dual Cartan" >}}.
