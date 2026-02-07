---
title: "Shannon entropy"
description: "A measure of uncertainty of a discrete random variable, defined from its probability mass function."
---

A **Shannon entropy** is a number $H(X)$ associated to a discrete {{< knowl id="random-variable" text="random variable" >}} $X$ with probability mass function $p(x)=\mathbb{P}(X=x)$, defined by
\[
H(X) \;=\; -\sum_x p(x)\,\log p(x),
\]
with the convention $0\log 0=0$. (Unless stated otherwise, $\log$ denotes the natural logarithm; changing the base rescales $H$ by a constant factor.)

Equivalently, $H(X)$ is the {{< knowl id="expectation" text="expectation" >}} of $-\log p(X)$ under the distribution of $X$. Shannon entropy is closely related to {{< knowl id="relative-entropy-kl-divergence" text="relative entropy (KL divergence)" >}} and is a central quantity in information theory.

**Examples:**
- If $X\sim\mathrm{Bernoulli}(p)$, then $H(X)=-p\log p-(1-p)\log(1-p)$.
- If $X$ is uniform on $\{1,2,3,4,5,6\}$, then $H(X)=\log 6$.
