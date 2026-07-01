+++
id = "real-analysis/equicontinuity-dense-set-lemma"
title = "Equicontinuity and dense sets lemma"
kind = "knowl"
summary = "On a compact metric space, equicontinuity allows pointwise Cauchy behavior on a dense set to upgrade to uniform Cauchy behavior."
aliases = ["equicontinuity-dense-set-lemma", "Equicontinuity and dense sets lemma"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/equicontinuity-dense-set-lemma.md"
+++

**Equicontinuity and dense sets lemma:** Let $K$ be a compact [[topology/metric-space|metric space]], and let $D\subseteq K$ be [[topology/dense-set|dense]] in $K$. Let $(f_n)$ be an [[real-analysis/equicontinuity|equicontinuous]] sequence of functions $f_n:K\to\mathbb{R}$. If for every $x\in D$ the numerical sequence $(f_n(x))$ is Cauchy (equivalently, convergent), then $(f_n)$ is [[real-analysis/uniform-cauchy|uniformly Cauchy]] on $K$.

Consequently, by [[real-analysis/uniform-cauchy-iff-uniform-convergence|the uniform Cauchy criterion]], the sequence $(f_n)$ converges [[real-analysis/uniform-convergence|uniformly]] on $K$ (since $\mathbb{R}$ is complete), a key step in many proofs of [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli]]-type compactness results.
