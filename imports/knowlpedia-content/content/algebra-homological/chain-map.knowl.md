+++
id = "algebra-homological/chain-map"
title = "Chain map"
kind = "knowl"
summary = "A degreewise module homomorphism between chain complexes commuting with differentials."
aliases = ["chain-map", "Chain map"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/chain-map.md"
+++

Let \((C_\bullet,d^C)\) and \((D_\bullet,d^D)\) be [[algebra-homological/chain-complex|chain complexes]] of \(R\)-modules.
A **chain map** \(f:C_\bullet\to D_\bullet\) is a family of \(R\)-linear maps
\[
f_n: C_n \longrightarrow D_n \qquad (n\in\mathbb Z)
\]
such that for every \(n\),
\[
d^D_n\circ f_n = f_{n-1}\circ d^C_n.
\]
Equivalently, the squares commute:
\[
\begin{array}{ccc}
C_n & \xrightarrow{d^C_n} & C_{n-1}\\
\downarrow f_n && \downarrow f_{n-1}\\
D_n & \xrightarrow{d^D_n} & D_{n-1}.
\end{array}
\]

A chain map induces maps on homology:
\[
H_n(f): H_n(C_\bullet)\to H_n(D_\bullet),
\]
see [[algebra-homological/homology-module|homology module]].

## Cross-links
- Two chain maps may be equivalent “up to homotopy”: [[algebra-homological/chain-homotopy|chain homotopy]].
- Chain maps are morphisms in the category of complexes; more generally in an [[algebra-category-theory/abelian-category|abelian category]].
- In degree 0, chain maps recover ordinary [[algebra-modules/algebra-homomorphism|module homomorphisms]].

## Examples
1. **A module homomorphism as a chain map.**
   If \(M,N\) are modules viewed as complexes concentrated in degree \(0\) (see [[algebra-homological/chain-complex|chain complex]] examples), then a chain map \(M\to N\) is exactly an \(R\)-linear map \(M\to N\).

2. **Inclusion of a subcomplex.**
   If \(C_\bullet\subseteq D_\bullet\) degreewise and \(d^D\) restricts to \(C_\bullet\), then the inclusions \(i_n:C_n\hookrightarrow D_n\) form a chain map \(i:C_\bullet\to D_\bullet\).

3. **Multiplication on a fixed complex.**
   Let \(C_\bullet\) be any chain complex of \(R\)-modules and fix \(r\in R\). Define \(f_n:C_n\to C_n\) by \(f_n(c)=rc\). Since the differentials are \(R\)-linear, \(d_n(rc)=r\,d_n(c)\), so \(f=(f_n)\) is a chain endomorphism \(C_\bullet\to C_\bullet\).
