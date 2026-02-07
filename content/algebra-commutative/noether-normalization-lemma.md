---
title: "Noether normalization lemma"
description: "A finitely generated algebra over a field is integral over a polynomial subalgebra."
---

Noether normalization is the foundational structural theorem for finitely generated algebras over a field: after choosing suitable “coordinates,” the algebra becomes an {{< knowl id="integral-extension" text="integral extension" >}} of a polynomial ring. It is one of the key inputs behind dimension theory (via {{< knowl id="krull-dimension" text="Krull dimension" >}}) and the algebra–geometry dictionary (via the {{< knowl id="nullstellensatz-variety-correspondence" text="Nullstellensatz correspondence" >}}).

## Statement

Let $k$ be a {{< knowl id="field" section="algebra-rings" text="field" >}}, and let $A$ be a finitely generated $k$-algebra. Then there exist elements
\[
y_1,\dots,y_d \in A
\]
that are algebraically independent over $k$ such that $A$ is integral over the $k$-subalgebra $k[y_1,\dots,y_d]$.

Equivalently, there exists an injective $k$-algebra homomorphism
\[
k[t_1,\dots,t_d]\hookrightarrow A
\]
whose image is a polynomial subalgebra, and such that $A$ is a finitely generated module over $k[t_1,\dots,t_d]$ (i.e. $A$ is module-finite over that subring). In the language of {{< knowl id="integral-element" text="integral elements" >}}, this says every element of $A$ is integral over the subring $k[y_1,\dots,y_d]$.

Moreover, one can choose $d=\dim(A)$ in the sense of {{< knowl id="krull-dimension" text="Krull dimension" >}}.

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

This lemma is frequently combined with {{< knowl id="prime-avoidance-lemma" text="prime avoidance" >}} (to choose “good” linear combinations) and with localization techniques such as {{< knowl id="localization-ring" text="localization" >}} when passing to local statements.
