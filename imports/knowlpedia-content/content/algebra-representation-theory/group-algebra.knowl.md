+++
id = "algebra-representation-theory/group-algebra"
title = "Group algebra"
kind = "knowl"
summary = "The associative algebra k[G] whose basis is a group G and whose multiplication extends the group law bilinearly."
aliases = ["group-algebra", "Group algebra"]
domains = ["algebra-representation-theory"]
legacy_source_path = "algebra-representation-theory/group-algebra.md"
+++

Let \(G\) be a finite group and \(k\) a field. The **group algebra** \(k[G]\) (also written \(kG\)) is the \(k\)-[[linear-algebra/vector-space|vector space]] with basis \(\{\,\delta_g : g\in G\,\}\) and multiplication determined by
\[
\delta_g\cdot \delta_h = \delta_{gh}\quad (g,h\in G),
\]
extended \(k\)-bilinearly. Thus every element has a unique expression
\[
x=\sum_{g\in G} a_g\,\delta_g\qquad (a_g\in k),
\]
and multiplication is
\[
\left(\sum_{g} a_g\delta_g\right)\left(\sum_{h} b_h\delta_h\right)=\sum_{g,h} a_g b_h\,\delta_{gh}.
\]
The identity element of \(k[G]\) is \(\delta_e\), where \(e\) is the identity of \(G\).

## Representations as modules

A (finite-dimensional) [[algebra-representation-theory/group-representation|group representation]] \(\rho:G\to \mathrm{GL}(V)\) on a \(k\)-vector space \(V\) extends uniquely to a \(k\)-algebra homomorphism
\[
\widetilde{\rho}:k[G]\to \mathrm{End}_k(V),\qquad
\widetilde{\rho}\!\left(\sum_g a_g\delta_g\right)=\sum_g a_g\,\rho(g).
\]
Equivalently, giving a representation of \(G\) is the same as giving a left \(k[G]\)-module structure on \(V\) (i.e. an action \(k[G]\times V\to V\) that is \(k\)-bilinear and associative). In this correspondence:
- [[algebra-representation-theory/subrepresentation|subrepresentations]] are exactly \(k[G]\)-submodules,
- [[algebra-representation-theory/irreducible-representation|irreducible representations]] are exactly [[algebra-modules/simple-module|simple modules]] over \(k[G]\),
- complete reducibility is a statement about \(k[G]\) being semisimple (cf. [[algebra-representation-theory/maschkes-theorem|Maschke’s theorem]] and [[algebra-modules/semisimple-module|semisimple modules]]).

## Examples

### Example 1: Cyclic groups \(C_n\)
Let \(G=C_n=\langle t\mid t^n=e\rangle\). Then
\[
k[C_n]\cong k[t]/(t^n-1),
\]
via \(\delta_{t^m}\mapsto t^m\). This realizes \(k[C_n]\) as a commutative \(k\)-algebra.

### Example 2: The order-2 group \(C_2=\{e,s\}\)
Here \(k[C_2]=k\delta_e\oplus k\delta_s\) with \(\delta_s^2=\delta_e\). So
\[
k[C_2]\cong k[s]/(s^2-1).
\]
If \(\mathrm{char}(k)\neq 2\), the elements
\[
e_\pm=\tfrac12(\delta_e\pm \delta_s)
\]
satisfy \(e_\pm^2=e_\pm\) and \(e_+e_-=0\), giving a decomposition \(k[C_2]\cong k\times k\). (This is a concrete instance of semisimplicity in characteristic not dividing \(|G|\).)

### Example 3: \(S_3\) and class sums
For \(G=S_3\), \(k[S_3]\) is \(6\)-dimensional with basis \(\{\delta_\sigma:\sigma\in S_3\}\).
The center \(Z(k[S_3])\) is spanned by sums over [[algebra-groups/conjugacy-class|conjugacy classes]]:
\[
z_1=\delta_e,\qquad
z_2=\sum_{\text{transpositions }\tau}\delta_\tau,\qquad
z_3=\sum_{\text{3-cycles }\gamma}\delta_\gamma.
\]
These “class sums” act as scalars in any irreducible representation (compare [[algebra-representation-theory/schurs-lemma|Schur’s lemma]]).
