---
title: "Symplectic Lie algebra"
description: "The Lie algebra of the symplectic group: matrices satisfying with commutator bracket."
---

### Definition
Fix the standard symplectic matrix
$$
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}.
$$

The **symplectic Lie algebra** over a field $\mathbb F$ of characteristic $\neq 2$ is
$$
\mathfrak{sp}(2n,\mathbb F)=\{X\in M_{2n}(\mathbb F)\mid X^T J + JX = 0\},
$$

with Lie bracket given by the commutator $[X,Y]=XY-YX$ (see {{< knowl id="lie-bracket" text="the Lie bracket" section="fiber-bundles">}}). It is the Lie algebra of the {{< knowl id="symplectic-group" text="symplectic group $\\mathrm{Sp}(2n,\\mathbb F)$" >}} in the sense of {{< knowl id="lie-algebra-of-a-lie-group" text="the Lie algebra of a Lie group" >}}.

### Useful block description
Writing a matrix in $n\times n$ blocks
$$
X=\begin{pmatrix}A&B\\C&D\end{pmatrix},
$$

the condition $X^T J + JX=0$ is equivalent to
$$
D=-A^T,\qquad B=B^T,\qquad C=C^T.
$$

In particular, over $\mathbb R$ or $\mathbb C$ one computes
$$
\dim \mathfrak{sp}(2n)=n^2+\frac{n(n+1)}{2}+\frac{n(n+1)}{2}=n(2n+1).
$$

### Structure and context
Over an algebraically closed field of characteristic $0$, $\mathfrak{sp}(2n)$ is a {{< knowl id="simple-lie-algebra" text="simple Lie algebra" >}} (type $C_n$). A choice of {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}} leads to the usual root space description (see {{< knowl id="root-space-decomposition" text="root space decomposition" >}}); the associated reflections generate the {{< knowl id="weyl-group" text="Weyl group" >}}. Nondegeneracy of the {{< knowl id="killing-form" text="Killing form" >}} is a key semisimplicity test (compare {{< knowl id="killing-form-nondegenerate-iff-semisimple" text="Killing form nondegeneracy and semisimplicity" >}}).
