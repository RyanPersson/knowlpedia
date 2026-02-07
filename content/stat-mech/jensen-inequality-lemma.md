---
title: "Jensen's inequality (lemma)"
description: "For a convex function φ, one has φ(E[X]) ≤ E[φ(X)] whenever the expectations exist."
---

## Definitions and notation

- {{< knowl id="probability-measure" section="probability" text="Probability measure" >}} and {{< knowl id="expectation" section="probability" text="expectation" >}}.
- {{< knowl id="convex-function-via-epigraph" section="convex-analysis" text="Convex function" >}}.

## Statement

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $X:\Omega\to I$ be a random variable taking values in a convex set $I\subseteq \mathbb R^d$. Let $\varphi:I\to\mathbb R$ be convex.

Assume $X$ is integrable and $\varphi(X)$ is integrable, i.e.
- $\mathbb E[\|X\|] < \infty$ and
- $\mathbb E[|\varphi(X)|] < \infty$.

Then
$$
\varphi(\mathbb E[X]) \le \mathbb E[\varphi(X)].
$$

If $\varphi$ is concave, the inequality is reversed:
$$
\varphi(\mathbb E[X]) \ge \mathbb E[\varphi(X)].
$$

## Key hypotheses and conclusions

**Hypotheses**
- $X$ is a random variable with values in a convex set $I$.
- $\varphi$ is convex on $I$.
- The expectations $\mathbb E[X]$ and $\mathbb E[\varphi(X)]$ exist (finite).

**Conclusions**
- Convexity pulls outside expectations: $\varphi(\mathbb E[X]) \le \mathbb E[\varphi(X)]$.
- If $\varphi$ is strictly convex (and mild regularity/“non-degenerate support” assumptions hold), equality forces $X$ to be almost surely constant.

