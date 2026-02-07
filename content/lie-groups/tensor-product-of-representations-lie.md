---
title: "Tensor product of representations"
description: "The diagonal action on : for Lie algebras acts by Leibniz, for Lie groups by tensoring operators."
---

### Definition (Lie groups)
Let $G$ be a Lie group and let $\pi_V:G\to GL(V)$ and $\pi_W:G\to GL(W)$ be {{< knowl id="representation-of-a-lie-group" text="representations of $G$" >}}. The **tensor product representation** is
$$
\pi_{V\otimes W}(g)=\pi_V(g)\otimes \pi_W(g)\in GL(V\otimes W),
$$

defined by $(\pi_V(g)\otimes \pi_W(g))(v\otimes w)=\pi_V(g)v\otimes \pi_W(g)w$ and extended linearly.

### Definition (Lie algebras)
Let $\mathfrak g$ be a Lie algebra and let $\rho_V:\mathfrak g\to \mathfrak{gl}(V)$ and $\rho_W:\mathfrak g\to \mathfrak{gl}(W)$ be {{< knowl id="representation-of-a-lie-algebra" text="representations of $\\mathfrak g$" >}}. The **tensor product representation** $\rho_{V\otimes W}:\mathfrak g\to \mathfrak{gl}(V\otimes W)$ is given by
$$
\rho_{V\otimes W}(X)=\rho_V(X)\otimes \mathrm{Id}_W \;+\; \mathrm{Id}_V\otimes \rho_W(X),
$$
i.e.
$$
X\cdot (v\otimes w)=(X\cdot v)\otimes w + v\otimes (X\cdot w).
$$

A direct computation using the commutator bracket on $\mathfrak{gl}(V\otimes W)$ shows $\rho_{V\otimes W}$ is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}.

### Weight behavior (motivation)
If $\mathfrak g$ is semisimple and $\mathfrak h$ is a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}, then tensor products interact cleanly with the {{< knowl id="weight-space" text="weight space decomposition" >}}: if $v\in V_\lambda$ and $w\in W_\mu$, then
$$
v\otimes w \in (V\otimes W)_{\lambda+\mu}.
$$

Thus the set of {{< knowl id="weight-of-a-representation" text="weights" >}} of $V\otimes W$ is contained in the Minkowski sum of the weight sets of $V$ and $W$. This is one of the basic mechanisms behind Clebsch–Gordan type decompositions and highest-weight calculations (compare {{< knowl id="highest-weight-representation" text="highest-weight representations" >}}).
