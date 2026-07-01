+++
id = "lie-groups/example-heisenberg-algebra"
title = "Example: the Heisenberg Lie algebra"
kind = "knowl"
summary = "A 3D nilpotent Lie algebra with basis and bracket ."
aliases = ["example-heisenberg-algebra", "Example: the Heisenberg Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-heisenberg-algebra.md"
+++

Let $\mathfrak h_3$ be the 3-dimensional real Lie algebra with basis $\{X,Y,Z\}$ and brackets
\[
[X,Y]=Z,\qquad [X,Z]=[Y,Z]=0.
\]
This is the simplest non-abelian nilpotent example (see [[lie-groups/nilpotent-lie-algebra|nilpotent Lie algebra]]).

## Concrete matrix model
Inside $\mathfrak{gl}_3(\mathbb R)$, set
\[
X = E_{12},\quad Y = E_{23},\quad Z = E_{13},
\]
where $E_{ij}$ has a $1$ in the $(i,j)$ entry and $0$ otherwise. Using the commutator bracket,
\[
[E_{12},E_{23}] = E_{12}E_{23}-E_{23}E_{12} = E_{13}-0 = E_{13},
\]
and one checks $[E_{12},E_{13}]=[E_{23},E_{13}]=0$. Hence this realizes $\mathfrak h_3$ as strictly upper triangular $3\times 3$ matrices (compare [[lie-groups/example-strictly-upper-triangular|strictly upper triangular examples]]).

## Derived subalgebra and center
The [[lie-groups/derived-subalgebra|derived subalgebra]] is
\[
[\mathfrak h_3,\mathfrak h_3] = \mathrm{span}\{Z\}.
\]
Moreover $Z$ commutes with everything, so the [[lie-groups/center-of-a-lie-algebra|center]] is
\[
Z(\mathfrak h_3)=\mathrm{span}\{Z\}.
\]
Thus $\mathfrak h_3/[\mathfrak h_3,\mathfrak h_3]\cong \mathbb R^2$ is abelian.

## Lower central and derived series (explicit)
The [[lie-groups/lower-central-series-lie-algebra|lower central series]] is
\[
\mathfrak h_3=\gamma_1 \supset \gamma_2=[\gamma_1,\gamma_1]=\mathrm{span}\{Z\} \supset \gamma_3=[\mathfrak h_3,\gamma_2]=0,
\]
so $\mathfrak h_3$ is nilpotent of class $2$.

The [[lie-groups/derived-series-lie-algebra|derived series]] is
\[
\mathfrak h_3^{(1)}=[\mathfrak h_3,\mathfrak h_3]=\mathrm{span}\{Z\},\qquad
\mathfrak h_3^{(2)}=[\mathrm{span}\{Z\},\mathrm{span}\{Z\}]=0,
\]
so $\mathfrak h_3$ is solvable (compare [[lie-groups/solvable-lie-algebra|solvable Lie algebra]]).

**Context.** Exponentiating $\mathfrak h_3$ yields the [[lie-groups/heisenberg-group|Heisenberg group]], a central extension of $\mathbb R^2$ by $\mathbb R$ that is fundamental in geometry and representation theory.
