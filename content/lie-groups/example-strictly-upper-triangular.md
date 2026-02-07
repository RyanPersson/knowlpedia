---
title: "Example: strictly upper triangular matrices"
description: "Strictly upper triangular matrices form a nilpotent Lie algebra under commutator; commutators move entries further above the diagonal."
---

Let $\mathfrak n_n\subset \mathfrak{gl}_n(\mathbb R)$ be the vector space of strictly upper triangular matrices (zeros on and below the diagonal), with Lie bracket the commutator $[A,B]=AB-BA$.

This is a standard example of a {{< knowl id="nilpotent-lie-algebra" text="nilpotent Lie algebra" >}}.

## Concrete bracket computation in the matrix-unit basis
For $i<j$, let $E_{ij}$ be the matrix unit. A direct multiplication gives
\[
E_{ij}E_{kl}=\delta_{jk}E_{il},
\]
so
\[
[E_{ij},E_{kl}] = E_{ij}E_{kl}-E_{kl}E_{ij}
= \delta_{jk}E_{il}-\delta_{li}E_{kj}.
\]
In particular, if $i<j$ and $k<l$, then $[E_{ij},E_{kl}]$ is either $0$ or another strictly upper triangular matrix unit.

## Lower central series (explicit nilpotency mechanism)
Define the “height” of $E_{ij}$ as $j-i\ge 1$. From the formula above, any nonzero commutator of strictly upper triangular matrices increases height: the product $E_{ij}E_{jk}=E_{ik}$ has height $(k-i)=(j-i)+(k-j)$.

Consequently, iterated commutators eventually vanish: the {{< knowl id="lower-central-series-lie-algebra" text="lower central series" >}}
\[
\gamma_1=\mathfrak n_n,\qquad \gamma_{r+1}=[\mathfrak n_n,\gamma_r]
\]
satisfies $\gamma_{n}=0$. Thus $\mathfrak n_n$ is nilpotent of class at most $n-1$, hence solvable (compare {{< knowl id="nilpotent-implies-solvable-lemma" text="nilpotent implies solvable" >}} and {{< knowl id="derived-series-lie-algebra" text="derived series" >}}).

## Small case $n=3$ (fully explicit)
A general element is
\[
\begin{pmatrix}
0 & a & b\\
0 & 0 & c\\
0 & 0 & 0
\end{pmatrix}
= aE_{12}+bE_{13}+cE_{23}.
\]
Using $[E_{12},E_{23}]=E_{13}$ and other brackets $0$, we get
\[
[\mathfrak n_3,\mathfrak n_3]=\mathrm{span}\{E_{13}\},
\qquad
[\mathfrak n_3,[\mathfrak n_3,\mathfrak n_3]]=0,
\]
which matches the {{< knowl id="example-heisenberg-algebra" text="Heisenberg algebra" >}} pattern.
