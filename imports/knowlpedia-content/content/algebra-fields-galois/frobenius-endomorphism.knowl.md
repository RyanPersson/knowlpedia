+++
id = "algebra-fields-galois/frobenius-endomorphism"
title = "Frobenius endomorphism"
kind = "knowl"
summary = "In characteristic p, the map x ↦ x^p is a ring endomorphism; on finite fields it is an automorphism."
aliases = ["frobenius-endomorphism", "Frobenius endomorphism"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/frobenius-endomorphism.md"
+++

Let \(F\) be a [[algebra-rings/field|field]] of [[algebra-rings/characteristic|characteristic]] \(p>0\). The **Frobenius endomorphism** of \(F\) is the map
\[
\mathrm{Fr}_F: F\to F,\qquad x\mapsto x^p.
\]
It is a ring endomorphism because in characteristic \(p\) one has \((x+y)^p=x^p+y^p\) (all intermediate binomial coefficients are divisible by \(p\)), and \((xy)^p=x^p y^p\).

If \(F\) is a [[algebra-fields-galois/finite-field|finite field]], then \(\mathrm{Fr}_F\) is bijective (hence a [[algebra-fields-galois/field-automorphism|field automorphism]]); indeed, any injective map \(F\to F\) is automatically surjective because \(F\) is finite. More generally, in characteristic \(p\) the Frobenius is an automorphism precisely when \(F\) is [[algebra-fields-galois/perfect-field|perfect]].

For \(F=\mathbb{F}_{q^n}\) over \(\mathbb{F}_q\), the \(q\)-power Frobenius \(x\mapsto x^q\) generates the [[algebra-fields-galois/galois-group|Galois group]] of the extension (see [[algebra-fields-galois/finite-field-galois-group-cyclic|finite-field Galois group is cyclic]]), and the fixed field of \(x\mapsto x^q\) is \(\mathbb{F}_q\) (compare [[algebra-fields-galois/fixed-field|fixed field]]).

### Examples
1. **Prime field.** On \(\mathbb{F}_p\), Frobenius is the identity map since \(a^p=a\) for all \(a\in\mathbb{F}_p\).

2. **\(\mathbb{F}_4\).** In \(\mathbb{F}_4=\mathbb{F}_2(\alpha)\) with \(\alpha^2=\alpha+1\), the Frobenius is \(x\mapsto x^2\). It satisfies \(\alpha\mapsto \alpha^2=\alpha+1\) and \(\alpha+1\mapsto (\alpha+1)^2=\alpha\), so it is a nontrivial automorphism of order \(2\).

3. **A non-surjective Frobenius (imperfect field).** Let \(F=\mathbb{F}_p(t)\), the rational function field. Then Frobenius sends \(t\mapsto t^p\), so \(t\) is not a \(p\)th power in \(F\); hence Frobenius is not surjective and not an automorphism.
