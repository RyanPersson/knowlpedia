+++
id = "real-analysis/jordan-decomposition-lemma"
title = "Jordan decomposition lemma"
kind = "knowl"
summary = "A bounded variation function can be written as a difference of two increasing functions."
aliases = ["jordan-decomposition-lemma", "Jordan decomposition lemma"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/jordan-decomposition-lemma.md"
+++

**Jordan decomposition lemma:** Let $a<b$ and let $g:[a,b]\to\mathbb{R}$ be a [[real-analysis/bounded-variation-function|bounded variation function]]. Then there exist [[real-analysis/monotone-function|increasing functions]] $g_1,g_2:[a,b]\to\mathbb{R}$ such that
$$
g = g_1 - g_2.
$$

Moreover, one can choose $g_1,g_2$ so that the [[real-analysis/total-variation|total variation]] satisfies
$$
V_a^b(g) = \bigl(g_1(b)-g_1(a)\bigr) + \bigl(g_2(b)-g_2(a)\bigr).
$$

This decomposition reduces many questions about bounded variation to the monotone case, and it is frequently used in the theory of the [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes integral]].
