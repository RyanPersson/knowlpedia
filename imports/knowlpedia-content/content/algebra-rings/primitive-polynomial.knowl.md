+++
id = "algebra-rings/primitive-polynomial"
title = "Primitive polynomial"
kind = "knowl"
summary = "A polynomial whose coefficients generate the unit ideal (content 1)."
aliases = ["primitive-polynomial", "Primitive polynomial"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/primitive-polynomial.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]] and let $f\in R[x]$ be nonzero. The polynomial $f$ is **primitive** if its [[algebra-rings/content-polynomial|content]] is the whole ring, i.e. $c(f)=R$ (equivalently, the coefficients generate the unit ideal).

Primitivity formalizes “no nontrivial common factor in the coefficients.” It is the hypothesis in [[algebra-rings/gauss-lemma|Gauss’s lemma]], which links irreducibility in $R[x]$ to irreducibility over the fraction field. In a field, every nonzero polynomial is primitive because any nonzero coefficient is a [[algebra-rings/unit|unit]].

**Examples:**
- In $\mathbb{Z}[x]$, $2x+3$ is primitive since $(2,3)=\mathbb{Z}$.
- In $\mathbb{Z}[x]$, $x^2-5x+10$ is primitive.
- In $\mathbb{Z}[x]$, $6x+9$ is not primitive since its content is $(3)$.
