+++
id = "real-analysis/limit-at-infinity"
title = "Limit at infinity"
kind = "knowl"
summary = "The epsilon-M definition of the limit of a function as x goes to plus or minus infinity."
aliases = ["limit-at-infinity", "Limit at infinity"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-at-infinity.md"
+++

A **limit at infinity** for a [[shared-foundations/function|function]] $f:D\to\mathbb R$ is a number $L\in\mathbb R$ such that: for every $\varepsilon>0$ there exists $M\in\mathbb R$ with the property that whenever $x\in D$ and $x>M$, one has $|f(x)-L|<\varepsilon$. One writes $\lim_{x\to\infty} f(x)=L$. Similarly, $\lim_{x\to-\infty} f(x)=L$ means that for every $\varepsilon>0$ there exists $M$ such that $x<M$ implies $|f(x)-L|<\varepsilon$.

This is an asymptotic version of the [[real-analysis/limit-at-a-point|limit at a point]] definition, with “$x$ close to $a$” replaced by “$x$ large in magnitude.” It is commonly used to describe end behavior on unbounded [[real-analysis/interval|intervals]].

**Examples:**
- $\lim_{x\to\infty}\tfrac1x=0$.
- $\lim_{x\to\infty}\tfrac{2x+1}{x}=2$.
