+++
id = "probability/moment"
title = "Moment"
kind = "knowl"
summary = "Expected power of a random variable, used to summarize features of its distribution"
aliases = ["moment"]
domains = ["probability"]
legacy_source_path = "probability/moment.md"
+++

A **moment** of order $k$ is an [[probability/expectation|expectation]] of a power of a [[probability/random-variable|random variable]] $X$, typically the raw moment $\mathbb{E}[X^k]$ or the central moment $\mathbb{E}\!\left[(X-\mathbb{E}[X])^k\right]$, whenever these expectations exist (equivalently, when $\mathbb{E}[|X|^k]<\infty$).

Moments summarize aspects of the [[probability/distribution-law|distribution]]; for instance the second central moment is the [[probability/variance|variance]] and the first raw moment is the mean $\mathbb{E}[X]$. When a [[probability/moment-generating-function|moment generating function]] exists in a neighborhood of zero, its derivatives recover the raw moments.

**Examples:**
- If $X\sim\mathrm{Bernoulli}(p)$, then $X^k=X$ for all integers $k\ge 1$, so $\mathbb{E}[X^k]=p$ and $\operatorname{Var}(X)=p(1-p)$.
- If $X\sim N(0,1)$, then $\mathbb{E}[X]=0$, $\mathbb{E}[X^2]=1$, and all odd moments are $0$.
- If $X\sim\mathrm{Exp}(\lambda)$ with $\lambda>0$, then $\mathbb{E}[X^k]=k!/\lambda^k$ for integers $k\ge 1$.
