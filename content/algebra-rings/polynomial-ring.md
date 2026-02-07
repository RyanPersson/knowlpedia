---
title: "Polynomial ring"
description: "The ring R[x] of polynomials in an indeterminate x with coefficients in R."
---

Let $R$ be a {{< knowl id="commutative-ring" text="commutative ring" >}} with $1$. The **polynomial ring** $R[x]$ consists of finite sums $\sum_{i=0}^n a_i x^i$ with coefficients $a_i\in R$, with addition termwise and multiplication determined by distributivity and $x^i x^j=x^{i+j}$.

Polynomial rings provide the basic algebraic enlargement of a {{< knowl id="ring" text="ring" >}} by adjoining an indeterminate, and they interact strongly with divisibility and factorization (e.g. via {{< knowl id="irreducible-polynomial" text="irreducible polynomials" >}}). The coefficient data of a polynomial is often packaged by its {{< knowl id="content-polynomial" text="content" >}}.

**Examples:**
- $\mathbb{Z}[x]$ is the ring of integer-coefficient polynomials.
- If $k$ is a field, then $k[x,y]$ can be viewed as $(k[x])[y]$, polynomials in $y$ with coefficients in $k[x]$.
- The polynomial $f(x)=2x^2-3x+1\in \mathbb{Z}[x]$ has degree $2$ and leading coefficient $2$.