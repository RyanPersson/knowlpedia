---
title: "Equivalent characterizations of semisimplicity for Lie algebras"
description: "Semisimplicity is equivalent to nondegeneracy of the Killing form and to decomposition into simple ideals."
---

### Theorem (TFAE: semisimplicity)
Let $\mathfrak g$ be a finite-dimensional Lie algebra over a field of characteristic $0$ (in particular over $\mathbb R$ or $\mathbb C$). The following are equivalent.

1. **No nonzero solvable ideals:** $\mathfrak g$ is {{< knowl id="semisimple-lie-algebra" text="semisimple" >}}, i.e. it has no nonzero solvable ideal (equivalently, its radical is $0$).

2. **Nondegenerate Killing form:** the {{< knowl id="killing-form" text="Killing form" >}} $\kappa(X,Y)=\mathrm{tr}(\mathrm{ad}_X\mathrm{ad}_Y)$ is nondegenerate; compare {{< knowl id="killing-form-nondegenerate-iff-semisimple" text="nondegeneracy of the Killing form" >}}.

3. **Direct sum of simple ideals:** $\mathfrak g$ is a (finite) {{< knowl id="direct-sum-of-lie-algebras" text="direct sum" >}} of {{< knowl id="simple-lie-algebra" text="simple Lie algebras" >}}; see {{< knowl id="semisimple-direct-sum-simple" text="semisimple equals direct sum of simple ideals" >}}.

4. **Adjoint representation is completely reducible:** the representation $\mathrm{ad}:\mathfrak g\to \mathfrak{gl}(\mathfrak g)$ is {{< knowl id="completely-reducible-representation-lie" text="completely reducible" >}}.

5. **Cartan-type trace criterion:** $\mathfrak g$ satisfies a trace criterion equivalent to semisimplicity as in {{< knowl id="cartans-criterion-semisimplicity" text="Cartan’s criterion for semisimplicity" >}}.

### Context
These equivalences are used interchangeably in practice: (2) is often the fastest computational test, while (3) is the structural starting point for classification (compare {{< knowl id="classification-simple-lie-algebras" text="classification of simple Lie algebras" >}}). Complete reducibility of representations (see {{< knowl id="weyls-theorem-complete-reducibility" text="Weyl’s theorem" >}}) is a major consequence of semisimplicity.
