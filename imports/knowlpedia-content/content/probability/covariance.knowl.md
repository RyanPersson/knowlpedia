+++
id = "probability/covariance"
title = "Covariance"
kind = "knowl"
summary = "Expectation of a centered product measuring joint linear variability of two random variables"
aliases = ["covariance"]
domains = ["probability"]
legacy_source_path = "probability/covariance.md"
+++

A **covariance** is the quantity $\operatorname{Cov}(X,Y)=\mathbb{E}\!\left[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])\right]=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]$ associated to two [[probability/random-variable|random variables]] $X$ and $Y$ with finite second moments.

Covariance is built from [[probability/expectation|expectation]] on a [[probability/probability-space|probability space]] and generalizes [[probability/variance|variance]], since $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$. If $X$ and $Y$ are [[probability/independence-random-variables|independent]] and have finite second moments, then $\operatorname{Cov}(X,Y)=0$ (but the converse need not hold).

**Examples:**
- If $X=\mathbf{1}_A$ and $Y=\mathbf{1}_B$ are indicator [[probability/random-variable|random variables]] of events $A,B$, then $\operatorname{Cov}(X,Y)=\mathbb{P}(A\cap B)-\mathbb{P}(A)\mathbb{P}(B)$ in terms of [[probability/event-probability|event probabilities]].
- If $Y=aX+b$ for constants $a,b$ and $X$ has finite second moment, then $\operatorname{Cov}(X,Y)=a\,\operatorname{Var}(X)$.
- If $X$ and $Y$ are independent standard normal [[probability/random-variable|random variables]], then $\operatorname{Cov}(X,Y)=0$.
