---
title: "Trace and Norm in Towers"
description: "Trace and norm compose multiplicatively/additively along a finite tower."
---

**Theorem (Tower formulas).**  
Let \(K \subseteq L \subseteq M\) be a tower of finite extensions. Then:

- (**Trace**) \(\mathrm{Tr}_{M/K} = \mathrm{Tr}_{L/K}\circ \mathrm{Tr}_{M/L}\) as maps \(M\to K\).
- (**Norm**) \(N_{M/K} = N_{L/K}\circ N_{M/L}\) as maps \(M^\times\to K^\times\).

These are the standard {{</* knowl id="trace-field" text="trace" */>}} and {{</* knowl id="norm-field" text="norm" */>}} compatibility relations, and they pair naturally with the {{</* knowl id="tower-law" text="tower law" */>}} for degrees.

**Examples.**
1. If \(K\subseteq L\subseteq M\) and \(\alpha\in M\), then \(\mathrm{Tr}_{M/K}(\alpha)=\mathrm{Tr}_{L/K}(\mathrm{Tr}_{M/L}(\alpha))\).
2. For finite fields \( \mathbb{F}_q \subseteq \mathbb{F}_{q^m} \subseteq \mathbb{F}_{q^{mn}}\), norms satisfy
   \(N_{\mathbb{F}_{q^{mn}}/\mathbb{F}_q} = N_{\mathbb{F}_{q^m}/\mathbb{F}_q}\circ N_{\mathbb{F}_{q^{mn}}/\mathbb{F}_{q^m}}\).
3. For quadratic towers \(K \subset L \subset M\) with both steps degree \(2\), norms multiply: \(N_{M/K}(\alpha)=N_{L/K}(N_{M/L}(\alpha))\).

**Related.** {{</* knowl id="discriminant-field" text="discriminant" */>}}, {{</* knowl id="trace-norm-towers" text="trace/norm tower law" */>}}.
