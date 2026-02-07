---
title: "Cyclotomic polynomial"
description: "The polynomial Φ_n(x) whose roots are the primitive n-th roots of unity; it factors x^n−1 and is irreducible over Q."
---

Fix an integer \(n\ge 1\). In an {{< knowl id="algebraic-closure" text="algebraic closure" >}} of a field of characteristic \(0\) (e.g. inside \(\mathbb{C}\)), an element \(\zeta\) is a {{< knowl id="primitive-root-of-unity" text="primitive n-th root of unity" >}} if \(\zeta^n=1\) and \(\zeta^d\ne 1\) for every proper divisor \(d\mid n\). The **\(n\)-th cyclotomic polynomial** is
\[
\Phi_n(x) \;:=\; \prod_{\substack{1\le k\le n\\ \gcd(k,n)=1}} (x-\zeta_n^{\,k}),
\]
where \(\zeta_n\) is any fixed primitive \(n\)-th root of unity. This definition is independent of the choice of \(\zeta_n\), and \(\Phi_n(x)\in\mathbb{Z}[x]\) is monic.

A key structural identity is the factorization
\[
x^n-1 \;=\; \prod_{d\mid n}\Phi_d(x),
\]
which can be taken as an equivalent recursive definition of \(\Phi_n\) in \(\mathbb{Z}[x]\). Over \(\mathbb{Q}\), \(\Phi_n(x)\) is irreducible, so it is the minimal polynomial of \(\zeta_n\) and
\[
[\mathbb{Q}(\zeta_n):\mathbb{Q}]=\deg \Phi_n=\varphi(n),
\]
linking cyclotomic polynomials to the {{< knowl id="cyclotomic-extension" text="cyclotomic extension" >}} \(\mathbb{Q}(\zeta_n)\) and the {{< knowl id="splitting-field" text="splitting field" >}} of \(x^n-1\).

### Examples
1. \(\Phi_1(x)=x-1\), \(\Phi_2(x)=x+1\), \(\Phi_3(x)=x^2+x+1\), \(\Phi_4(x)=x^2+1\).

2. For an odd prime \(p\),
\[
\Phi_p(x)=1+x+x^2+\cdots+x^{p-1}.
\]

3. Using \(x^6-1=\prod_{d\mid 6}\Phi_d(x)\) and the known \(\Phi_1,\Phi_2,\Phi_3\), one gets
\[
\Phi_6(x)=\frac{x^6-1}{(x-1)(x+1)(x^2+x+1)}=x^2-x+1.
\]
