---
title: "Categorical product"
description: "An object A×B equipped with projections, universal among cones to A and B."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and let \(A,B\) be {{< knowl id="object" text="objects" >}} of \(\mathcal C\).

A **(binary) categorical product** of \(A\) and \(B\) is a triple \((A\times B,\pi_1,\pi_2)\) consisting of an object \(A\times B\) and morphisms
\[
\pi_1:A\times B\to A,\qquad \pi_2:A\times B\to B
\]
such that for every object \(X\) and every pair of morphisms \(f:X\to A\), \(g:X\to B\), there exists a **unique** morphism
\[
\langle f,g\rangle : X\to A\times B
\]
making the equations
\[
\pi_1\circ \langle f,g\rangle = f,\qquad \pi_2\circ \langle f,g\rangle = g
\]
hold (see {{< knowl id="composition-category" text="composition" >}}).

In diagram form:
\[
\begin{CD}
& X @>\langle f,g\rangle>> A\times B \\
@V f VV @VV \pi_1 V \\
A &&
\end{CD}
\qquad
\begin{CD}
& X @>\langle f,g\rangle>> A\times B \\
@V g VV @VV \pi_2 V \\
B &&
\end{CD}
\]

A product is unique up to unique {{< knowl id="isomorphism-category" text="isomorphism" >}}: if \((P,\pi_1,\pi_2)\) and \((P',\pi_1',\pi_2')\) are both products of \(A,B\), there is a unique isomorphism \(P\cong P'\) compatible with projections.

This is a special case of a {{< knowl id="limit" text="limit" >}} (the limit of the discrete diagram \(A\;\;B\)).

## Examples
1. **\(\mathbf{Set}\)**.  
   The categorical product is the usual {{< knowl id="cartesian-product" section="shared-foundations" text="cartesian product" >}} \(A\times B\) of sets, with projections \(\pi_1(a,b)=a\), \(\pi_2(a,b)=b\).

2. **\(\mathbf{Grp}\)**.  
   For groups \(G,H\), the product is the direct product \(G\times H\) with coordinate projections, characterized by: giving a homomorphism \(X\to G\times H\) is equivalent to giving a pair of homomorphisms \(X\to G\) and \(X\to H\).

3. **\(\mathbf{Top}\)** (and similarly \(\mathbf{Ab}\), \(R\)-Mod).  
   The product of spaces \(X,Y\) is the set-theoretic product \(X\times Y\) equipped with the product topology; the projections are continuous and satisfy the same universal property.
