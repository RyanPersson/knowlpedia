+++
id = "algebra-representation-theory/schur-corollary"
title = "Schur corollary: central elements act by scalars"
kind = "knowl"
summary = "In an irreducible representation over an algebraically closed field, every central group element (and more generally every central group-algebra element) acts as a scalar."
aliases = ["schur-corollary", "Schur corollary: central elements act by scalars"]
domains = ["algebra-representation-theory"]
legacy_source_path = "algebra-representation-theory/schur-corollary.md"
+++

Let $G$ be a group, let $k$ be an algebraically closed field (e.g. $k=\mathbb C$), and let
\[
\rho: G \to \mathrm{GL}(V)
\]
be a finite-dimensional [[algebra-representation-theory/irreducible-representation|irreducible representation]].

## Corollary of [[algebra-representation-theory/schurs-lemma|Schur's lemma]]
If $z$ lies in the [[algebra-groups/center-of-group|center]] $Z(G)$, then $\rho(z)$ is a scalar operator:
\[
\rho(z) \;=\; \lambda_z\,\mathrm{Id}_V \quad \text{for some }\lambda_z\in k.
\]

More generally, if $a$ lies in the center $Z(k[G])$ of the [[algebra-representation-theory/group-algebra|group algebra]], then the $k$-linear operator “action by $a$” on $V$ commutes with $\rho(G)$ and hence is also scalar on $V$.

### Consequence: abelian groups have only $1$-dimensional irreps
If $G$ is [[algebra-groups/abelian-group|abelian]], then every $g\in G$ is central, so every $\rho(g)$ is scalar. If $\dim(V)>1$, every line in $V$ would be $G$-stable, contradicting irreducibility. Hence any irreducible representation of an abelian group over $k$ has $\dim(V)=1$.

## Examples

1. **$C_n$.**
   Since $C_n$ is abelian, every irreducible complex representation is $1$-dimensional. Concretely, if $C_n=\langle g\rangle$ and $\zeta=e^{2\pi i/n}$, the irreducibles are the characters
   \[
   \chi_j(g)=\zeta^j \qquad (j=0,1,\dots,n-1).
   \]

2. **$D_8$ (order $8$).**
   For the dihedral group of the square, the center is $Z(D_8)=\{1,r^2\}$ where $r$ is rotation by $90^\circ$. In the $2$-dimensional “geometric” irreducible representation on $\mathbb C^2$, $r^2$ acts as rotation by $180^\circ$, i.e.
   \[
   \rho(r^2) = -I,
   \]
   a scalar operator. In every $1$-dimensional representation, $\rho(r^2)=+1$ (also a scalar, necessarily).

3. **$S_3$.**
   $Z(S_3)=\{e\}$ is trivial, so the corollary imposes no nontrivial scalar constraints—consistent with the existence of a $2$-dimensional irreducible representation.
