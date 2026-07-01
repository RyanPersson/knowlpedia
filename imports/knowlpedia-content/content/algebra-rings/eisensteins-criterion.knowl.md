+++
id = "algebra-rings/eisensteins-criterion"
title = "Eisenstein's criterion"
kind = "knowl"
summary = "A sufficient condition (via a prime element) for a polynomial to be irreducible."
aliases = ["eisensteins-criterion", "Eisenstein's criterion"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/eisensteins-criterion.md"
+++

**Eisenstein's criterion**: Let \(R\) be a [[algebra-rings/ufd|UFD]] and let \(p\in R\) be a [[algebra-rings/prime-element|prime element]]. Consider \(f(x)=a_nx^n+\cdots+a_0\in R[x]\) in the [[algebra-rings/polynomial-ring|polynomial ring]] \(R[x]\). If
- \(p\mid a_i\) for all \(i<n\),
- \(p\nmid a_n\), and
- \(p^2\nmid a_0\),
then \(f\) is [[algebra-rings/irreducible-polynomial|irreducible]] in \(\mathrm{Frac}(R)[x]\), where \(\mathrm{Frac}(R)\) is the [[algebra-rings/fraction-field|fraction field]] of \(R\). Consequently, \(f\) is irreducible in \(R[x]\).
