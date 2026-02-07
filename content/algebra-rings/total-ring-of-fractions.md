---
title: "Total ring of fractions"
description: "Localization of a commutative ring obtained by inverting all regular elements (non-zero-divisors)."
---

Let \(R\) be a {{< knowl id="commutative-ring" text="commutative ring" >}} (with \(1\)). Let \(S\subseteq R\) be the multiplicative set of {{< knowl id="regular-element" text="regular elements" >}} (equivalently: elements that are not a {{< knowl id="zero-divisor" text="zero-divisor" >}}). The **total ring of fractions** of \(R\) is the localization
\[
Q(R):=S^{-1}R.
\]
The canonical map \(R\to Q(R)\) sends every \(s\in S\) to a {{< knowl id="unit" text="unit" >}} in \(Q(R)\), and \(Q(R)\) is universal with this property among commutative rings receiving a map from \(R\).

If \(R\) is an integral domain, then \(S=R\setminus\{0\}\) and \(Q(R)\cong\) the {{< knowl id="fraction-field" text="fraction field" >}} of \(R\).