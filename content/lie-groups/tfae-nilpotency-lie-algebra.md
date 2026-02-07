---
title: "Equivalent characterizations of nilpotency for Lie algebras"
description: "Nilpotency can be tested via the lower central series, Engel’s condition on adjoints, or strict upper-triangular models."
---

### Theorem (TFAE: nilpotency)
Let $\mathfrak g$ be a finite-dimensional Lie algebra over a field of characteristic $0$. The following are equivalent.

1. **Lower central series terminates:** the {{< knowl id="lower-central-series-lie-algebra" text="lower central series" >}} $\mathfrak g_1=\mathfrak g$, $\mathfrak g_{k+1}=[\mathfrak g,\mathfrak g_k]$ satisfies $\mathfrak g_N=0$ for some $N$. Equivalently, $\mathfrak g$ is {{< knowl id="nilpotent-lie-algebra" text="nilpotent" >}}.

2. **Engel condition on adjoints:** for every $X\in\mathfrak g$, the endomorphism $\mathrm{ad}_X:\mathfrak g\to\mathfrak g$ in the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} is nilpotent.

3. **Strict upper-triangular realization:** there exists an injective Lie algebra homomorphism
   $$
   \mathfrak g \hookrightarrow \mathfrak{gl}(N,\mathbb F)
   $$
   whose image consists of strictly upper triangular matrices (hence all images are nilpotent endomorphisms). This can be viewed as a refinement of {{< knowl id="ados-theorem" text="Ado’s theorem" >}} specialized to the nilpotent case.

4. **Central series by ideals:** there exists a chain of ideals
   $$
   \mathfrak g=\mathfrak g^{(0)}\supset \mathfrak g^{(1)}\supset \cdots \supset \mathfrak g^{(N)}=0
   $$

   such that $[\mathfrak g,\mathfrak g^{(i)}]\subseteq \mathfrak g^{(i+1)}$ for all $i$.

### Context
Condition (2) is the Lie-algebraic form of “all infinitesimal conjugations are nilpotent,” while (3) connects nilpotent Lie algebras to concrete matrix models such as {{< knowl id="example-strictly-upper-triangular" text="strictly upper-triangular examples" >}}. Nilpotency is stronger than solvability; in fact {{< knowl id="nilpotent-implies-solvable-lemma" text="nilpotent implies solvable" >}}.
