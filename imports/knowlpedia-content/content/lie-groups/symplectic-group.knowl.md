+++
id = "lie-groups/symplectic-group"
title = "Symplectic group"
kind = "knowl"
summary = "The Lie group of linear transformations preserving a nondegenerate alternating form on ."
aliases = ["symplectic-group", "Symplectic group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/symplectic-group.md"
+++

### Definition
Let $J$ be the standard symplectic matrix
$$
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix},
$$

so the bilinear form $\omega(u,v)=u^T J v$ on $\mathbb R^{2n}$ is nondegenerate and skew-symmetric. The **real symplectic group** is
$$
\mathrm{Sp}(2n,\mathbb R)=\{A\in GL(2n,\mathbb R)\mid A^T J A = J\}.
$$
This is a closed subgroup of the [[lie-groups/general-linear-group|general linear group]], hence a Lie subgroup by the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]].

More generally, for any field $\mathbb F$ of characteristic $\neq 2$, one defines $\mathrm{Sp}(2n,\mathbb F)$ as the group preserving a fixed nondegenerate alternating form; different choices are conjugate in $GL(2n,\mathbb F)$.

### Lie algebra
The Lie algebra of $\mathrm{Sp}(2n,\mathbb R)$ is the [[lie-groups/symplectic-lie-algebra|symplectic Lie algebra $\\mathfrak{sp}(2n,\\mathbb R)$]], obtained by differentiating the defining equation $A^TJA=J$ at the identity.

### Context
$\mathrm{Sp}(2n,\mathbb R)$ is the basic symmetry group of linear symplectic geometry and Hamiltonian mechanics: it preserves the standard symplectic form and hence the canonical Poisson structure on $\mathbb R^{2n}$. In representation theory, its complexification corresponds to the simple Lie algebra of type $C_n$ (compare [[lie-groups/root-system|root systems]] and [[lie-groups/dynkin-diagram|Dynkin diagrams]]).
