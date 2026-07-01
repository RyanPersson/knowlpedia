+++
id = "probability/pinsker-inequality"
title = "Pinsker's inequality"
kind = "knowl"
summary = "An inequality bounding total variation distance by the square root of Kullback–Leibler divergence."
aliases = ["pinsker-inequality", "Pinsker's inequality"]
domains = ["probability"]
legacy_source_path = "probability/pinsker-inequality.md"
+++

**Pinsker's inequality:** Let $P$ and $Q$ be [[probability/probability-measure|probability measures]] on the same $(\Omega,\mathcal F)$. Then their [[probability/total-variation-distance|total variation distance]] satisfies
$$
d_{\mathrm{TV}}(P,Q)\;\le\;\sqrt{\frac12\,D(P\|Q)},
$$

where $D(P\|Q)$ is the [[probability/relative-entropy-kl-divergence|Kullback–Leibler divergence]] computed with natural logarithms (if another log base is used, the constant changes accordingly). The inequality is understood to hold trivially when $D(P\|Q)=+\infty$.

Pinsker's inequality formalizes that small relative entropy forces two laws to be close in a strong, event-wise sense. Together with [[probability/gibbs-inequality-kl|Gibbs' inequality]], it highlights KL divergence as a nonnegative discrepancy measure that quantitatively controls $d_{\mathrm{TV}}$.
