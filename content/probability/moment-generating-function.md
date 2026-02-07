---
title: "Moment generating function"
description: "Function of a real parameter defined by the expected exponential of t times a random variable"
---

A **moment generating function** is the {{< knowl id="function" section="shared-foundations" text="function" >}} $M_X(t)=\mathbb{E}[e^{tX}]$ of a real parameter $t$ defined for a {{< knowl id="random-variable" text="random variable" >}} $X$ on all values of $t$ for which the expectation is finite (often an interval containing $0$).  

If $M_X(t)$ is finite on an open interval around $0$, then $M_X^{(k)}(0)=\mathbb{E}[X^k]$, linking it directly to {{< knowl id="moment" text="moments" >}}. The closely related {{< knowl id="cumulant-generating-function" text="cumulant generating function" >}} is $\log M_X(t)$ (when defined), and the {{< knowl id="characteristic-function-probability" text="characteristic function" >}} can be used when the mgf does not exist.  

**Examples:**
- If $X\sim N(\mu,\sigma^2)$, then $M_X(t)=\exp\!\left(\mu t+\tfrac{1}{2}\sigma^2 t^2\right)$ for all real $t$.
- If $X\sim\mathrm{Bernoulli}(p)$, then $M_X(t)=(1-p)+p\,e^{t}$ for all real $t$.
- If $X\sim\mathrm{Exp}(\lambda)$ with $\lambda>0$, then $M_X(t)=\frac{\lambda}{\lambda-t}$ for $t<\lambda$.
