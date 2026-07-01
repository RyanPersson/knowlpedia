+++
id = "algebra-rings/fraction-field"
title = "Fraction field"
kind = "knowl"
summary = "The field obtained from an integral domain by adjoining inverses to all nonzero elements."
aliases = ["fraction-field", "Fraction field"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/fraction-field.md"
+++

Let \(R\) be an [[algebra-rings/integral-domain|integral domain]]. The **fraction field** \(\mathrm{Frac}(R)\) is the set of equivalence classes of pairs \((a,b)\in R\times R\) with \(b\neq 0\), under
\[
(a,b)\sim(c,d)\quad\Longleftrightarrow\quad ad=bc.
\]
Write the class of \((a,b)\) as \(a/b\). Addition and multiplication are defined by
\[
\frac{a}{b}+\frac{c}{d}=\frac{ad+bc}{bd},\qquad \frac{a}{b}\cdot\frac{c}{d}=\frac{ac}{bd},
\]
and these operations make \(\mathrm{Frac}(R)\) a [[algebra-rings/field|field]]. The map \(R\hookrightarrow \mathrm{Frac}(R)\), \(a\mapsto a/1\), is an injective ring map.

**Universal property.** If \(K\) is a field and \(\iota:R\to K\) is a [[algebra-rings/ring-monomorphism|ring monomorphism]], then there exists a unique field homomorphism \(\tilde\iota:\mathrm{Frac}(R)\to K\) with \(\tilde\iota(a/1)=\iota(a)\) for all \(a\in R\).

For domains, \(\mathrm{Frac}(R)\) agrees with the [[algebra-rings/total-ring-of-fractions|total ring of fractions]] (since every nonzero element is a non-zero-divisor).
