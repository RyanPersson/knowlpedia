---
title: "Equicontinuity and dense sets lemma"
description: "On a compact metric space, equicontinuity allows pointwise Cauchy behavior on a dense set to upgrade to uniform Cauchy behavior."
---

**Equicontinuity and dense sets lemma:** Let $K$ be a compact {{< knowl id="metric-space" section="topology" text="metric space" >}}, and let $D\subseteq K$ be {{< knowl id="dense-set" section="topology" text="dense" >}} in $K$. Let $(f_n)$ be an {{< knowl id="equicontinuity" text="equicontinuous" >}} sequence of functions $f_n:K\to\mathbb{R}$. If for every $x\in D$ the numerical sequence $(f_n(x))$ is Cauchy (equivalently, convergent), then $(f_n)$ is {{< knowl id="uniform-cauchy" text="uniformly Cauchy" >}} on $K$.

Consequently, by {{< knowl id="uniform-cauchy-iff-uniform-convergence" text="the uniform Cauchy criterion" >}}, the sequence $(f_n)$ converges {{< knowl id="uniform-convergence" text="uniformly" >}} on $K$ (since $\mathbb{R}$ is complete), a key step in many proofs of {{< knowl id="arzela-ascoli-theorem" text="Arzelà–Ascoli" >}}-type compactness results.
