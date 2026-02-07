---
title: "Weights in the dual Cartan"
description: "Weights are elements of ; integrality conditions define weight lattices tied to maximal tori and characters."
---

### Definition (where weights live)
Let $\mathfrak g$ be a complex semisimple Lie algebra and $\mathfrak h\subset\mathfrak g$ a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}. A {{< knowl id="weight-of-a-representation" text="weight" >}} of a representation is, by definition, an element of the dual space $\mathfrak h^\ast$, i.e. a linear functional on $\mathfrak h$. The root system $\Delta$ of $\mathfrak g$ is also a subset of $\mathfrak h^\ast$ (see {{< knowl id="root-system" text="root systems" >}}), so weights and roots live in the same ambient vector space and can be compared geometrically.

### Integral and dominant weights (standard semisimple setup)
Fix a set of {{< knowl id="simple-root" text="simple roots" >}} and corresponding coroots $H_\alpha\in\mathfrak h$ (defined so that $\beta(H_\alpha)$ are the Cartan integers). The **integral weight lattice** is
$$
P=\{\lambda\in\mathfrak h^\ast\mid \lambda(H_\alpha)\in\mathbb Z\ \text{for all simple roots }\alpha\}.
$$

A weight is **dominant** if $\lambda(H_\alpha)\ge 0$ for all simple roots. Highest-weight classification says finite-dimensional irreducibles are parametrized by dominant integral weights (compare {{< knowl id="highest-weight-theorem" text="highest-weight classification" >}}).

### Link with compact groups and maximal tori
If $G$ is a compact connected Lie group with maximal torus $T$ (see {{< knowl id="maximal-torus-theorem" text="the maximal torus theorem" >}}), then characters $T\to U(1)$ differentiate to linear functionals on $\mathfrak t=\mathrm{Lie}(T)$, producing an integral lattice in $\mathfrak t^\ast$. After complexification, this lattice matches the integral weights in $\mathfrak h^\ast$ for the complexified Lie algebra. The {{< knowl id="weyl-group" text="Weyl group" >}} acts on these lattices and preserves integrality.
