---
title: "Primitive polynomial"
description: "A polynomial whose coefficients generate the unit ideal (content 1)."
---

Let $R$ be an {{< knowl id="integral-domain" text="integral domain" >}} and let $f\in R[x]$ be nonzero. The polynomial $f$ is **primitive** if its {{< knowl id="content-polynomial" text="content" >}} is the whole ring, i.e. $c(f)=R$ (equivalently, the coefficients generate the unit ideal).

Primitivity formalizes “no nontrivial common factor in the coefficients.” It is the hypothesis in {{< knowl id="gauss-lemma" text="Gauss’s lemma" >}}, which links irreducibility in $R[x]$ to irreducibility over the fraction field. In a field, every nonzero polynomial is primitive because any nonzero coefficient is a {{< knowl id="unit" text="unit" >}}.

**Examples:**
- In $\mathbb{Z}[x]$, $2x+3$ is primitive since $(2,3)=\mathbb{Z}$.
- In $\mathbb{Z}[x]$, $x^2-5x+10$ is primitive.
- In $\mathbb{Z}[x]$, $6x+9$ is not primitive since its content is $(3)$.