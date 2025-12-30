---
title: "Eisenstein's criterion"
description: "A sufficient condition (via a prime element) for a polynomial to be irreducible."
---

**Eisenstein's criterion**: Let \(R\) be a {{< knowl id="ufd" text="UFD" >}} and let \(p\in R\) be a {{< knowl id="prime-element" text="prime element" >}}. Consider \(f(x)=a_nx^n+\cdots+a_0\in R[x]\) in the {{< knowl id="polynomial-ring" text="polynomial ring" >}} \(R[x]\). If
- \(p\mid a_i\) for all \(i<n\),
- \(p\nmid a_n\), and
- \(p^2\nmid a_0\),
then \(f\) is {{< knowl id="irreducible-polynomial" text="irreducible" >}} in \(\mathrm{Frac}(R)[x]\), where \(\mathrm{Frac}(R)\) is the {{< knowl id="fraction-field" text="fraction field" >}} of \(R\). Consequently, \(f\) is irreducible in \(R[x]\).

**Proof sketch**: If \(f=gh\) with positive degrees, reduce coefficients modulo \(p\). The hypotheses force \(\bar f(x)=\bar a_n x^n\) in \((R/(p))[x]\), so one factor has zero constant term mod \(p\). Tracking constant terms then forces \(p^2\mid a_0\), contradicting the assumption.