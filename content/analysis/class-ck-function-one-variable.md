---
title: "Class C^k function (one-variable)"
description: "A function with continuous derivatives up to order k."
---

Let $I\subseteq\mathbb{R}$ be an interval and let $k\in\mathbb{N}\cup\{0\}$. A function $f:I\to\mathbb{R}$ (or $\mathbb{C}$) is of **class $C^k$** on $I$ if:
- $f^{(j)}$ exists on $I$ for every integer $j$ with $0\le j\le k$ (where $f^{(0)}:=f$), and
- each derivative $f^{(j)}$ is continuous on $I$.

The class $C^k$ encodes smoothness needed for Taylor's theorem, inverse/implicit function statements (in higher dimensions), and many approximation results.

**Examples:**
- Polynomials are $C^k$ on $\mathbb{R}$ for every $k$.
- $f(x)=|x|$ is $C^0$ on $\mathbb{R}$ but not $C^1$ on $\mathbb{R}$ (since $f'$ fails to exist at $0$).
- $f(x)=\sqrt{x}$ is $C^1$ on $(0,\infty)$ but not $C^1$ on $[0,\infty)$.
