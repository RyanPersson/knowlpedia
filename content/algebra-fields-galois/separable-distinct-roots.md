---
title: "Separable ⇔ Distinct Roots"
description: "An algebraic element (or polynomial) is separable exactly when its minimal polynomial has no repeated roots."
---

**Theorem.**  
Let \(K\) be a field and \(f\in K[x]\) be irreducible. The following are equivalent:

1. \(f\) has **distinct** roots in an algebraic closure of \(K\).
2. \(\gcd(f,f')=1\) in \(K[x]\), where \(f'\) is the formal derivative.
3. Any (equivalently, every) root \(\alpha\) of \(f\) is a {{< knowl id="separable-element" text="separable element" >}} over \(K\).

In particular, a finite extension \(L/K\) is {{< knowl id="separable-extension" text="separable" >}} iff every element of \(L\) is separable over \(K\).

**Examples.**
1. Over \(\mathbb{Q}\), \(f=x^3-2\) has derivative \(3x^2\), and \(\gcd(f,f')=1\), so \(f\) is separable (its three roots are distinct).
2. Over \(\mathbb{F}_p(t)\), \(f=x^{p}-t\) has derivative \(0\), hence is inseparable; it has a single root of multiplicity \(p\) in an algebraic closure.
3. Over \(\mathbb{F}_p\), \(f=x^{p}-x\) satisfies \(f'=-1\neq 0\), hence has no repeated roots and splits with \(p\) distinct roots (namely all elements of \(\mathbb{F}_p\)).

**Related.** {{< knowl id="irreducible-polynomial" section="algebra-rings" text="irreducible polynomials" >}}, {{< knowl id="inseparable-extension" text="inseparable extensions" >}}.
