+++
id = "lie-groups/tfae-solvability-lie-algebra"
title = "Equivalent characterizations of solvability for Lie algebras"
kind = "knowl"
summary = "Solvability can be detected via the derived series, triangular representations, or Cartan’s trace criterion."
aliases = ["tfae-solvability-lie-algebra", "Equivalent characterizations of solvability for Lie algebras"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/tfae-solvability-lie-algebra.md"
+++

### Theorem (TFAE: solvability)
Let $\mathfrak g$ be a finite-dimensional Lie algebra over an algebraically closed field of characteristic $0$ (e.g. $\mathbb C$). The following are equivalent.

1. **Derived series terminates:** the [[lie-groups/derived-series-lie-algebra|derived series]] $\mathfrak g^{(0)}=\mathfrak g$, $\mathfrak g^{(k+1)}=[\mathfrak g^{(k)},\mathfrak g^{(k)}]$ satisfies $\mathfrak g^{(N)}=0$ for some $N$. Equivalently, $\mathfrak g$ is [[lie-groups/solvable-lie-algebra|solvable]].

2. **Upper-triangular matrix model:** there exists a faithful finite-dimensional representation (guaranteed in general by [[lie-groups/ados-theorem|Ado’s theorem]]) such that the image of $\mathfrak g$ is conjugate into the Lie algebra of upper triangular matrices in $\mathfrak{gl}(n)$; compare [[lie-groups/example-upper-triangular|upper triangular examples]]. In particular, $\mathfrak g$ is isomorphic to a Lie subalgebra of an upper triangular matrix Lie algebra.

3. **Lie’s theorem behavior in representations:** for every finite-dimensional representation $\rho:\mathfrak g\to\mathfrak{gl}(V)$, there exists a complete flag of $\mathfrak g$-invariant subspaces
   $$
   0=V_0\subset V_1\subset \cdots \subset V_{\dim V}=V
   $$

   with $\dim V_i=i$. Equivalently, all operators in $\rho(\mathfrak g)$ can be simultaneously upper-triangularized. (This is the content of Lie’s theorem applied to solvable Lie algebras.)

4. **Cartan’s trace criterion:** $\mathfrak g$ satisfies the trace-vanishing condition equivalent to solvability given by [[lie-groups/cartans-criterion-solvability|Cartan’s criterion for solvability]].

### Context
Condition (1) is the intrinsic definition; (2) and (3) explain why solvable Lie algebras behave like “triangular” objects in linear algebra, while (4) is useful when $\mathfrak g$ is given abstractly but $\mathrm{ad}$ is accessible. Solvability is weaker than nilpotency, and [[lie-groups/nilpotent-implies-solvable-lemma|nilpotent Lie algebras are always solvable]].
