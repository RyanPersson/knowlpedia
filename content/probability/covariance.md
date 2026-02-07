---
title: "Covariance"
description: "Expectation of a centered product measuring joint linear variability of two random variables"
---

A **covariance** is the quantity $\operatorname{Cov}(X,Y)=\mathbb{E}\!\left[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])\right]=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]$ associated to two {{< knowl id="random-variable" text="random variables" >}} $X$ and $Y$ with finite second moments.  

Covariance is built from {{< knowl id="expectation" text="expectation" >}} on a {{< knowl id="probability-space" text="probability space" >}} and generalizes {{< knowl id="variance" text="variance" >}}, since $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$. If $X$ and $Y$ are {{< knowl id="independence-random-variables" text="independent" >}} and have finite second moments, then $\operatorname{Cov}(X,Y)=0$ (but the converse need not hold).  

**Examples:**
- If $X=\mathbf{1}_A$ and $Y=\mathbf{1}_B$ are indicator {{< knowl id="random-variable" text="random variables" >}} of events $A,B$, then $\operatorname{Cov}(X,Y)=\mathbb{P}(A\cap B)-\mathbb{P}(A)\mathbb{P}(B)$ in terms of {{< knowl id="event-probability" text="event probabilities" >}}.
- If $Y=aX+b$ for constants $a,b$ and $X$ has finite second moment, then $\operatorname{Cov}(X,Y)=a\,\operatorname{Var}(X)$.
- If $X$ and $Y$ are independent standard normal {{< knowl id="random-variable" text="random variables" >}}, then $\operatorname{Cov}(X,Y)=0$.
