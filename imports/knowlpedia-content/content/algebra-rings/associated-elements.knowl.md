+++
id = "algebra-rings/associated-elements"
title = "Associated elements"
kind = "knowl"
summary = "Two elements that differ by multiplication by a unit."
aliases = ["associated-elements", "Associated elements"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/associated-elements.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]]. Elements $a,b\in R$ are **associates** if there exists a [[algebra-rings/unit|unit]] $u\in R^\times$ such that $a=ub$.

Being associates is an equivalence relation capturing “the same divisor up to invertible scaling.” Uniqueness statements for [[algebra-rings/gcd|gcds]], [[algebra-rings/prime-element|prime elements]], and factorizations are typically only up to associates.

**Examples:**
- In $\mathbb{Z}$, $2$ and $-2$ are associates (multiply by the unit $-1$).
- In $k[x]$ with $k$ a field, $f$ and $cf$ are associates for any nonzero scalar $c\in k$.
- In $\mathbb{Z}$, $2$ and $4$ are not associates since the only units are $\pm 1$.
