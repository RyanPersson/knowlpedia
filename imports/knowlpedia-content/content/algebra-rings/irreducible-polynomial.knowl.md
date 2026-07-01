+++
id = "algebra-rings/irreducible-polynomial"
title = "Irreducible polynomial"
kind = "knowl"
summary = "A nonconstant polynomial that cannot be factored into lower-degree nonunits."
aliases = ["irreducible-polynomial", "Irreducible polynomial"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/irreducible-polynomial.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]]. A polynomial $f\in R[x]$ is **irreducible** if $f$ is nonzero, not a [[algebra-rings/unit|unit]], has positive degree, and whenever $f=gh$ with $g,h\in R[x]$, then either $g$ or $h$ is a unit.

Over a field, irreducible polynomials generate maximal ideals in $R[x]$ and define finite field extensions. Practical tests include [[algebra-rings/eisensteins-criterion|Eisenstein’s criterion]], and [[algebra-rings/primitive-polynomial|primitive]] hypotheses are often used to compare factorization in $R[x]$ and in $\mathrm{Frac}(R)[x]$.

**Examples:**
- In $\mathbb{R}[x]$, the polynomial $x^2+1$ is irreducible.
- In $\mathbb{Q}[x]$, $x^3-2$ is irreducible (Eisenstein at $2$).
- In any $R[x]$, $x^2-1=(x-1)(x+1)$ is reducible.
