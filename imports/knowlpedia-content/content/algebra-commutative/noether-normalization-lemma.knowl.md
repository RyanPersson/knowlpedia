+++
id = "algebra-commutative/noether-normalization-lemma"
title = "Noether normalization lemma"
kind = "knowl"
summary = "A finitely generated algebra over a field is integral over a polynomial subalgebra."
aliases = ["noether-normalization-lemma", "Noether normalization lemma"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/noether-normalization-lemma.md"
+++

Noether normalization is the foundational structural theorem for finitely generated algebras over a field: after choosing suitable “coordinates,” the algebra becomes an [[algebra-commutative/integral-extension|integral extension]] of a polynomial ring. It is one of the key inputs behind dimension theory (via [[algebra-commutative/krull-dimension|Krull dimension]]) and the algebra–geometry dictionary (via the [[algebra-commutative/nullstellensatz-variety-correspondence|Nullstellensatz correspondence]]).

## Statement

Let $k$ be a [[algebra-rings/field|field]], and let $A$ be a finitely generated $k$-algebra. Then there exist elements
\[
y_1,\dots,y_d \in A
\]
that are algebraically independent over $k$ such that $A$ is integral over the $k$-subalgebra $k[y_1,\dots,y_d]$.

Equivalently, there exists an injective $k$-algebra homomorphism
\[
k[t_1,\dots,t_d]\hookrightarrow A
\]
whose image is a polynomial subalgebra, and such that $A$ is a finitely generated module over $k[t_1,\dots,t_d]$ (i.e. $A$ is module-finite over that subring). In the language of [[algebra-commutative/integral-element|integral elements]], this says every element of $A$ is integral over the subring $k[y_1,\dots,y_d]$.

Moreover, one can choose $d=\dim(A)$ in the sense of [[algebra-commutative/krull-dimension|Krull dimension]].

## Examples

1. **Polynomial rings normalize themselves.**
   If $A=k[x_1,\dots,x_n]$, take $y_i=x_i$ and $d=n$. Then $A=k[y_1,\dots,y_n]$, so $A$ is integral over the chosen polynomial subalgebra in the strongest possible way (equality).

2. **A plane curve coordinate ring.**
   Let
   \[
   A = k[x,y]/(y^2-x^3-x).
   \]
   Let $\bar x,\bar y$ be the residue classes of $x,y$ in $A$. Then $\bar y$ satisfies a monic polynomial over $k[\bar x]$:
   \[
   \bar y^2 - \bar x^3 - \bar x = 0.
   \]
   Hence $\bar y$ is integral over $k[\bar x]$, and $A$ is integral over the polynomial subalgebra $k[\bar x]\cong k[t]$ (so here $d=1$).

3. **A reducible example: $k[x,y]/(xy)$.**
   Let
   \[
   A = k[x,y]/(xy).
   \]
   Set $u=\bar x+\bar y\in A$ (bars denote residue classes). Then $\bar x$ satisfies the monic equation
   \[
   T^2-uT=0
   \]
   in $A[T]$ (since $\bar x^2-u\bar x=\bar x(\bar x-(\bar x+\bar y))=-\bar x\bar y=0$), so $\bar x$ is integral over $k[u]$. Similarly, $\bar y$ is integral over $k[u]$. Therefore $A$ is integral over the polynomial subalgebra $k[u]\cong k[t]$.

This lemma is frequently combined with [[algebra-commutative/prime-avoidance-lemma|prime avoidance]] (to choose “good” linear combinations) and with localization techniques such as [[algebra-commutative/localization-ring|localization]] when passing to local statements.
