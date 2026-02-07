---
title: "Rate function"
description: "A lower semicontinuous function that governs exponential decay rates in large deviations."
---

A **rate function** on a topological space $E$ is a function $I:E\to[0,\infty]$ that is **lower semicontinuous**, meaning that for every $\alpha\in\mathbb R$ the sublevel set
$$
\{x\in E:\ I(x)\le \alpha\}
$$

is closed in $E$, and such that $I$ is not identically $+\infty$.

Rate functions quantify the exponential scale of rare-event probabilities in a {{< knowl id="large-deviation-principle" text="large deviation principle" >}}: heuristically, $\mu_n(A)\approx \exp(-a_n \inf_{x\in A} I(x))$ for large $n$ and speed $a_n$. A particularly well-behaved class is given by {{< knowl id="good-rate-function" text="good rate functions" >}}, whose sublevel sets are compact.

**Examples:**
- On $E=\mathbb R$, the function $I(x)=\frac{x^2}{2}$ is a rate function (it is continuous, hence lower semicontinuous).
- For a closed set $C\subseteq E$, the indicator-type function
  $$
  I(x)=\begin{cases}
  0,& x\in C,\\
  +\infty,& x\notin C,
  \end{cases}
  $$

  is a rate function; it forces mass to concentrate on $C$ at the exponential scale.
