---
title: "Splitting Field: Existence and Uniqueness"
description: "Every polynomial has a splitting field, unique up to K-isomorphism."
---

**Theorem.**  
Let \(K\) be a field and \(f(x)\in K[x]\) a nonzero polynomial. There exists a field extension \(L/K\) such that \(f\) factors in \(L[x]\) as a product of linear factors and \(L\) is generated over \(K\) by the roots of \(f\). Such an \(L\) is a {{< knowl id="splitting-field" text="splitting field" >}} of \(f\) over \(K\).

Moreover, if \(L\) and \(L'\) are splitting fields of \(f\) over \(K\), then there is a \(K\)-isomorphism \(L \cong_K L'\) (not canonical). See also {{< knowl id="splitting-field-uniqueness" text="uniqueness of splitting fields" >}}.

**Examples.**
1. Over \(K=\mathbb{Q}\), \(f=x^2-2\) has splitting field \(L=\mathbb{Q}(\sqrt2)\).
2. Over \(\mathbb{Q}\), \(f=x^3-2\) has splitting field \(L=\mathbb{Q}(\sqrt[3]{2},\omega)\) where \(\omega\) is a primitive cube root of unity.
3. Over \(\mathbb{F}_2\), \(f=x^2+x+1\) is irreducible and its splitting field is \(\mathbb{F}_4\).

**Related.** {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial rings" >}}, {{< knowl id="field-extension" text="field extensions" >}}, {{< knowl id="normality-splitting-field" text="normality via splitting fields" >}}.
