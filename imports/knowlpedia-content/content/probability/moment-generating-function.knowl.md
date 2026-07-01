+++
id = "probability/moment-generating-function"
title = "Moment generating function"
kind = "knowl"
summary = "Function of a real parameter defined by the expected exponential of t times a random variable"
aliases = ["moment-generating-function", "Moment generating function"]
domains = ["probability"]
legacy_source_path = "probability/moment-generating-function.md"
+++

A **moment generating function** is the [[shared-foundations/function|function]] $M_X(t)=\mathbb{E}[e^{tX}]$ of a real parameter $t$ defined for a [[probability/random-variable|random variable]] $X$ on all values of $t$ for which the expectation is finite (often an interval containing $0$).

If $M_X(t)$ is finite on an open interval around $0$, then $M_X^{(k)}(0)=\mathbb{E}[X^k]$, linking it directly to [[probability/moment|moments]]. The closely related [[probability/cumulant-generating-function|cumulant generating function]] is $\log M_X(t)$ (when defined), and the [[probability/characteristic-function-probability|characteristic function]] can be used when the mgf does not exist.

**Examples:**
- If $X\sim N(\mu,\sigma^2)$, then $M_X(t)=\exp\!\left(\mu t+\tfrac{1}{2}\sigma^2 t^2\right)$ for all real $t$.
- If $X\sim\mathrm{Bernoulli}(p)$, then $M_X(t)=(1-p)+p\,e^{t}$ for all real $t$.
- If $X\sim\mathrm{Exp}(\lambda)$ with $\lambda>0$, then $M_X(t)=\frac{\lambda}{\lambda-t}$ for $t<\lambda$.
