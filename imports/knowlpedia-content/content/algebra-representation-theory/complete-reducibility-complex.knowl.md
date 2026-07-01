+++
id = "algebra-representation-theory/complete-reducibility-complex"
title = "Complete reducibility over ℂ"
kind = "knowl"
summary = "Every finite-dimensional complex representation of a finite group splits as a direct sum of irreducibles."
aliases = ["complete-reducibility-complex", "Complete reducibility over ℂ"]
domains = ["algebra-representation-theory"]
legacy_source_path = "algebra-representation-theory/complete-reducibility-complex.md"
+++

Let $G$ be a finite group and let $V$ be a finite-dimensional [[algebra-representation-theory/group-representation|complex representation]] of $G$.

## Theorem (complete reducibility over $\mathbb C$)
$V$ is [[algebra-representation-theory/completely-reducible-representation|completely reducible]]: there exist [[algebra-representation-theory/irreducible-representation|irreducible]] subrepresentations $V_1,\dots,V_m$ such that
\[
V \;\cong\; V_1\oplus\cdots\oplus V_m.
\]

Equivalently: for every [[algebra-representation-theory/subrepresentation|subrepresentation]] $W\subseteq V$, there exists a $G$-stable complement $W'\subseteq V$ with
\[
V \;=\; W \oplus W'.
\]

## Standard mechanism (unitary averaging)
Choose any Hermitian [[linear-algebra/inner-product|inner product]] $\langle\cdot,\cdot\rangle$ on $V$ and average it over $G$:
\[
\langle v,w\rangle_G \;=\; \frac{1}{|G|}\sum_{g\in G}\langle g\cdot v,\, g\cdot w\rangle.
\]
Then $\langle\cdot,\cdot\rangle_G$ is $G$-invariant. If $W\subseteq V$ is $G$-stable, its [[linear-algebra/orthogonality|orthogonal]] complement $W^\perp$ with respect to $\langle\cdot,\cdot\rangle_G$ is also $G$-stable, giving $V=W\oplus W^\perp$.

This is a complex-analytic presentation of [[algebra-representation-theory/maschkes-theorem|Maschke's theorem]].

## Examples

1. **Permutation representation of $S_3$ on $\mathbb C^3$.**
   Let $S_3$ act by permuting coordinates of $V=\mathbb C^3$. The line
   \[
   U=\operatorname{span}\{(1,1,1)\}
   \]
   is $S_3$-stable (it is the trivial representation). The subspace
   \[
   W=\{(x_1,x_2,x_3)\in\mathbb C^3 : x_1+x_2+x_3=0\}
   \]
   is also $S_3$-stable and $V=U\oplus W$. Moreover, $W$ is the $2$-dimensional irreducible (standard) representation.

2. **Any representation of a cyclic group $C_n$.**
   If $C_n=\langle g\rangle$ and $\rho(g)^n=I$, then the minimal polynomial of $\rho(g)$ divides $x^n-1$, which has distinct roots over $\mathbb C$. Hence $\rho(g)$ is diagonalizable, and $V$ decomposes as a direct sum of eigenspaces. Each eigenspace is a $1$-dimensional subrepresentation on which $g$ acts by an $n$th root of unity (a character of $C_n$).

3. **The swap representation of $C_2$ on $\mathbb C^2$.**
   Let $C_2=\{1,s\}$ act on $V=\mathbb C^2$ by $s(x,y)=(y,x)$. Then
   \[
   V = \operatorname{span}\{(1,1)\}\;\oplus\;\operatorname{span}\{(1,-1)\}.
   \]
   The first summand is the trivial representation; the second is the sign representation (where $s$ acts as $-1$).
