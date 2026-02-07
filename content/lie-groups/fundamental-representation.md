---
title: "Fundamental representation"
description: "An irreducible highest-weight representation whose highest weight is a fundamental weight."
---

Let $\mathfrak g$ be a complex semisimple {{< knowl id="lie-algebra" text="Lie algebra" >}} with a fixed {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}} $\mathfrak h$ and a choice of positive roots (see {{< knowl id="positive-root" text="positive roots" >}}). Let $\{\alpha_1,\dots,\alpha_r\}$ be the set of {{< knowl id="simple-root" text="simple roots" >}}, and let $\{\omega_1,\dots,\omega_r\}\subset \mathfrak h^*$ be the corresponding **fundamental weights**, characterized by
\[
\langle \omega_i,\alpha_j^\vee\rangle=\delta_{ij},
\]
where $\alpha_j^\vee$ are the simple coroots.

**Definition (Fundamental representation).**  
A **fundamental representation** of $\mathfrak g$ is a finite-dimensional irreducible {{< knowl id="highest-weight-representation" text="highest-weight representation" >}} whose {{< knowl id="highest-weight" text="highest weight" >}} is one of the fundamental weights $\omega_i$.

**Example (type $A_{n-1}$).**  
For $\mathfrak{sl}_n(\mathbb C)$ (see {{< knowl id="special-linear-lie-algebra" text="special linear Lie algebra" >}}), the fundamental representations are the exterior powers of the defining representation:
\[
\Lambda^k(\mathbb C^n),\qquad 1\le k\le n-1.
\]
With the standard choice of $\mathfrak h$ as diagonal trace-zero matrices, the highest weight of $\Lambda^k(\mathbb C^n)$ is $\omega_k$ (in the usual convention where weights record the eigenvalues of $\mathfrak h$ on weight vectors; compare {{< knowl id="weight-of-a-representation" text="weights" >}} and {{< knowl id="weight-space" text="weight spaces" >}}). In particular, $\Lambda^1(\mathbb C^n)=\mathbb C^n$ has highest weight $\omega_1$, while $\Lambda^{n-1}(\mathbb C^n)\cong (\mathbb C^n)^*$ has highest weight $\omega_{n-1}$.

**Context.**  
Fundamental representations correspond to the nodes of the {{< knowl id="dynkin-diagram" text="Dynkin diagram" >}} and generate the representation ring in many settings; the classification of all irreducibles proceeds via the {{< knowl id="highest-weight-theorem" text="highest-weight theorem" >}}.
