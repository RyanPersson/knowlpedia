---
title: "Degree bounds for splitting fields"
description: "The splitting field of a separable degree-n polynomial has degree at most n! over the base field."
---

Let \(K\) be a {{< knowl id="field" section="algebra-rings" text="field" >}} and let \(f(x)\in K[x]\) be a separable polynomial of degree \(n\) (equivalently, \(f\) has distinct roots in an {{< knowl id="algebraic-closure" text="algebraic closure" >}}; see {{< knowl id="separable-distinct-roots" text="separable ⇔ distinct roots" >}}). Let \(L\) be the {{< knowl id="splitting-field" text="splitting field" >}} of \(f\) over \(K\). Then \(L/K\) is finite, normal, and separable, hence {{< knowl id="galois-extension" text="Galois" >}} (see {{< knowl id="separable-normal-galois" text="separable + normal = Galois" >}}).

**Theorem (factorial bound).** If \(f\) is separable of degree \(n\), then
\[
[L:K] \le n!.
\]

One conceptual proof: separability gives \(n\) distinct roots in \(L\), and the {{< knowl id="galois-group" text="Galois group" >}} \(\mathrm{Gal}(L/K)\) acts faithfully on this set of roots, yielding an injective homomorphism \(\mathrm{Gal}(L/K)\hookrightarrow S_n\). Using {{< knowl id="galois-degree-equals-group-order" text="degree = group order" >}} for finite Galois extensions gives \([L:K]=|\mathrm{Gal}(L/K)|\le |S_n|=n!\).

A useful refinement: if \(f=\prod_i f_i\) with \(f_i\) separable and \(\deg(f_i)=d_i\), then writing \(L_i\) for the splitting field of \(f_i\), one has
\[
[L:K] \le \prod_i [L_i:K] \le \prod_i (d_i)!,
\]
since \(L\) is contained in the compositum of the \(L_i\).

### Examples

1. **Sharp bound for a cubic.**  
   Over \(\mathbb{Q}\), \(f=x^3-2\) is separable of degree \(3\). Its splitting field is \(\mathbb{Q}(\sqrt[3]{2},\zeta_3)\), and \([L:\mathbb{Q}]=6=3!\).

2. **A quartic with smaller degree than \(4!\).**  
   For \(f=x^4-2\in \mathbb{Q}[x]\), the splitting field is \(\mathbb{Q}(2^{1/4}, i)\), which has degree \(8\), far below \(24\).

3. **Product of quadratics.**  
   For \(f=(x^2-2)(x^2-3)\in \mathbb{Q}[x]\), the splitting field is \(\mathbb{Q}(\sqrt2,\sqrt3)\) and \([L:\mathbb{Q}]=4\), matching the refined bound \((2!)(2!)=4\).
