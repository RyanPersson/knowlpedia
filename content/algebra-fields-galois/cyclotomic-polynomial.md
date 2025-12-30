---
title: "Cyclotomic polynomial"
description: "The monic polynomial Φ_n(x) whose roots are the primitive n-th roots of unity."
---

**Definition.** For \(n\ge 1\), the **cyclotomic polynomial** \(\Phi_n(x)\in\mathbb{Z}[x]\) is defined by
\[
\Phi_n(x)=\prod_{\zeta}(x-\zeta),
\]
where the product runs over all {{< knowl id="primitive-root-of-unity" text="primitive n-th roots of unity" >}} \(\zeta\) in a fixed algebraic closure.

A fundamental factorization identity is
\[
x^n-1 \;=\; \prod_{d\mid n}\Phi_d(x).
\]
Over \(\mathbb{Q}\), \(\Phi_n(x)\) is {{< knowl id="irreducible-polynomial" text="irreducible" >}}, and its degree is \(\varphi(n)\) (Euler totient).

**See also.** {{< knowl id="cyclotomic-extension" text="cyclotomic extension" >}}, {{< knowl id="splitting-field" text="splitting field" >}}.

**Examples.**
1. \(\Phi_1(x)=x-1\), \(\Phi_2(x)=x+1\).
2. \(\Phi_3(x)=x^2+x+1\), since \(x^3-1=(x-1)(x^2+x+1)\).
3. \(\Phi_4(x)=x^2+1\), since \(x^4-1=(x-1)(x+1)(x^2+1)\).
