---
title: "Pinsker's inequality"
description: "An inequality bounding total variation distance by the square root of Kullback–Leibler divergence."
---

**Pinsker's inequality:** Let $P$ and $Q$ be {{< knowl id="probability-measure" text="probability measures" >}} on the same $(\Omega,\mathcal F)$. Then their {{< knowl id="total-variation-distance" text="total variation distance" >}} satisfies
$$
d_{\mathrm{TV}}(P,Q)\;\le\;\sqrt{\frac12\,D(P\|Q)},
$$

where $D(P\|Q)$ is the {{< knowl id="relative-entropy-kl-divergence" text="Kullback–Leibler divergence" >}} computed with natural logarithms (if another log base is used, the constant changes accordingly). The inequality is understood to hold trivially when $D(P\|Q)=+\infty$.

Pinsker's inequality formalizes that small relative entropy forces two laws to be close in a strong, event-wise sense. Together with {{< knowl id="gibbs-inequality-kl" text="Gibbs' inequality" >}}, it highlights KL divergence as a nonnegative discrepancy measure that quantitatively controls $d_{\mathrm{TV}}$.
