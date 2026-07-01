+++
id = "algebra-rings/total-ring-of-fractions"
title = "Total ring of fractions"
kind = "knowl"
summary = "Localization of a commutative ring obtained by inverting all regular elements (non-zero-divisors)."
aliases = ["total-ring-of-fractions", "Total ring of fractions"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/total-ring-of-fractions.md"
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]] (with \(1\)). Let \(S\subseteq R\) be the multiplicative set of [[algebra-rings/regular-element|regular elements]] (equivalently: elements that are not a [[algebra-rings/zero-divisor|zero-divisor]]). The **total ring of fractions** of \(R\) is the localization
\[
Q(R):=S^{-1}R.
\]
The canonical map \(R\to Q(R)\) sends every \(s\in S\) to a [[algebra-rings/unit|unit]] in \(Q(R)\), and \(Q(R)\) is universal with this property among commutative rings receiving a map from \(R\).

If \(R\) is an integral domain, then \(S=R\setminus\{0\}\) and \(Q(R)\cong\) the [[algebra-rings/fraction-field|fraction field]] of \(R\).
