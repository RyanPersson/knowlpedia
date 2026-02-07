---
title: "Jordan decomposition lemma"
description: "A bounded variation function can be written as a difference of two increasing functions."
---

**Jordan decomposition lemma:** Let $a<b$ and let $g:[a,b]\to\mathbb{R}$ be a {{< knowl id="bounded-variation-function" text="bounded variation function" >}}. Then there exist {{< knowl id="monotone-function" text="increasing functions" >}} $g_1,g_2:[a,b]\to\mathbb{R}$ such that
$$
g = g_1 - g_2.
$$

Moreover, one can choose $g_1,g_2$ so that the {{< knowl id="total-variation" text="total variation" >}} satisfies
$$
V_a^b(g) = \bigl(g_1(b)-g_1(a)\bigr) + \bigl(g_2(b)-g_2(a)\bigr).
$$

This decomposition reduces many questions about bounded variation to the monotone case, and it is frequently used in the theory of the {{< knowl id="riemann-stieltjes-integral" text="Riemann–Stieltjes integral" >}}.
