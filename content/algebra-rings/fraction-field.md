---
title: "Fraction field"
description: "The field obtained from an integral domain by adjoining inverses to all nonzero elements."
---

Let \(R\) be an {{< knowl id="integral-domain" text="integral domain" >}}. The **fraction field** \(\mathrm{Frac}(R)\) is the set of equivalence classes of pairs \((a,b)\in R\times R\) with \(b\neq 0\), under
\[
(a,b)\sim(c,d)\quad\Longleftrightarrow\quad ad=bc.
\]
Write the class of \((a,b)\) as \(a/b\). Addition and multiplication are defined by
\[
\frac{a}{b}+\frac{c}{d}=\frac{ad+bc}{bd},\qquad \frac{a}{b}\cdot\frac{c}{d}=\frac{ac}{bd},
\]
and these operations make \(\mathrm{Frac}(R)\) a {{< knowl id="field" text="field" >}}. The map \(R\hookrightarrow \mathrm{Frac}(R)\), \(a\mapsto a/1\), is an injective ring map.

**Universal property.** If \(K\) is a field and \(\iota:R\to K\) is a {{< knowl id="ring-monomorphism" text="ring monomorphism" >}}, then there exists a unique field homomorphism \(\tilde\iota:\mathrm{Frac}(R)\to K\) with \(\tilde\iota(a/1)=\iota(a)\) for all \(a\in R\).

For domains, \(\mathrm{Frac}(R)\) agrees with the {{< knowl id="total-ring-of-fractions" text="total ring of fractions" >}} (since every nonzero element is a non-zero-divisor).