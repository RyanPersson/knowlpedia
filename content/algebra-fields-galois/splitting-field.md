---
title: "Splitting field"
description: "The smallest extension of K over which a polynomial f ∈ K[x] factors completely into linear factors."
---

**Definition.** Let \(f(x)\in K[x]\) be a nonzero polynomial. A **splitting field** of \(f\) over \(K\) is a field extension \(L/K\) such that:

1. \(f\) factors in \(L[x]\) as a product of linear factors, and  
2. \(L\) is generated over \(K\) by the roots of \(f\) (equivalently, \(L\) is minimal with property (1)).

Splitting fields are unique up to \(K\)-isomorphism (see {{< knowl id="splitting-field-existence-uniqueness" text="existence and uniqueness of splitting fields" >}}).

**See also.** {{< knowl id="normal-extension" text="normal extension" >}}, {{< knowl id="galois-extension" text="Galois extension" >}}, {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial ring" >}}.

**Examples.**
1. For \(f(x)=x^2-2\in\mathbb{Q}[x]\), the splitting field is \(\mathbb{Q}(\sqrt2)\).
2. For \(f(x)=x^3-2\in\mathbb{Q}[x]\), the splitting field is \(\mathbb{Q}(\sqrt[3]{2},\zeta_3)\), where \(\zeta_3\) is a primitive cube root of unity.
3. For \(f(x)=x^2+1\in\mathbb{R}[x]\), the splitting field over \(\mathbb{R}\) is \(\mathbb{C}\).
