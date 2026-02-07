---
title: "Correlation coefficient"
description: "Normalized covariance giving a scale-free measure of linear association between two random variables"
---

A **correlation coefficient** is the normalized covariance $\rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}$ for {{< knowl id="random-variable" text="random variables" >}} $X$ and $Y$ with $0<\operatorname{Var}(X),\operatorname{Var}(Y)<\infty$.  

It is a dimensionless rescaling of {{< knowl id="covariance" text="covariance" >}} and satisfies $-1\le \rho(X,Y)\le 1$, with the sign indicating the direction of linear association. Correlation $\rho(X,Y)=0$ means $X$ and $Y$ are uncorrelated, which is implied by {{< knowl id="independence-random-variables" text="independence" >}} but is generally weaker.  

**Examples:**
- If $Y=aX+b$ with $a\neq 0$ and $\operatorname{Var}(X)>0$, then $\rho(X,Y)=1$ when $a>0$ and $\rho(X,Y)=-1$ when $a<0$.
- If $X\sim N(0,1)$ and $Z\sim N(0,1)$ are independent and $Y=X+Z$, then $\rho(X,Y)=\frac{1}{\sqrt{2}}$.
- If $X$ and $Y$ are independent with finite, nonzero variances, then $\rho(X,Y)=0$.
