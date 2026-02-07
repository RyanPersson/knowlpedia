---
title: "Subspace test"
description: "A nonempty subset is a subspace iff it is closed under addition and scalar multiplication"
---

**Proposition (Subspace test).**
Let $X$ be a vector space over $K$, and let $Y\subset X$ be nonempty. Then $Y$ is a {{< knowl id="linear-subspace" text="linear subspace" >}} of $X$ if and only if:

1. $Y+Y\subset Y$ (closure under addition), and
2. $\alpha Y\subset Y$ for all $\alpha\in K$ (closure under scalar multiplication).

**Proof sketch.**
- If $Y$ is a subspace, both closures are immediate from the definition.
- Conversely, assume (1)–(2) and pick $y_0\in Y$ (nonemptiness). Then $0=0\cdot y_0\in Y$, so $Y$ contains the zero vector. Also, for any $y\in Y$, $-y=(-1)y\in Y$, so additive inverses exist. Together with (1), this yields the defining subspace properties.
