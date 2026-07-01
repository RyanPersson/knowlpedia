+++
id = "lie-groups/symplectic-lie-algebra"
title = "Symplectic Lie algebra"
kind = "knowl"
summary = "The Lie algebra of the symplectic group: matrices satisfying with commutator bracket."
aliases = ["symplectic-lie-algebra", "Symplectic Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/symplectic-lie-algebra.md"
+++

### Definition
Fix the standard symplectic matrix
$$
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}.
$$

The **symplectic Lie algebra** over a field $\mathbb F$ of characteristic $\neq 2$ is
$$
\mathfrak{sp}(2n,\mathbb F)=\{X\in M_{2n}(\mathbb F)\mid X^T J + JX = 0\},
$$

with Lie bracket given by the commutator $[X,Y]=XY-YX$ (see [[fiber-bundles/lie-bracket|the Lie bracket]]). It is the Lie algebra of the [[lie-groups/symplectic-group|symplectic group $\\mathrm{Sp}(2n,\\mathbb F)$]] in the sense of [[lie-groups/lie-algebra-of-a-lie-group|the Lie algebra of a Lie group]].

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
Over an algebraically closed field of characteristic $0$, $\mathfrak{sp}(2n)$ is a [[lie-groups/simple-lie-algebra|simple Lie algebra]] (type $C_n$). A choice of [[lie-groups/cartan-subalgebra|Cartan subalgebra]] leads to the usual root space description (see [[lie-groups/root-space-decomposition|root space decomposition]]); the associated reflections generate the [[lie-groups/weyl-group|Weyl group]]. Nondegeneracy of the [[lie-groups/killing-form|Killing form]] is a key semisimplicity test (compare [[lie-groups/killing-form-nondegenerate-iff-semisimple|Killing form nondegeneracy and semisimplicity]]).
