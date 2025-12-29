---
title: "Taylor polynomial"
description: "The polynomial formed from the first k derivatives of f at a point a."
---

Let $f$ be a real- (or complex-) valued function defined on an {{< knowl id="interval" text="interval" >}} containing $a\in\mathbb{R}$, and assume that $f^{(j)}(a)$ exists for $0\le j\le k$ (see {{< knowl id="higher-derivatives" text="higher derivatives" >}}). The **Taylor polynomial of degree $k$ of $f$ at $a$** is
$$
T_k f(x;a) := \sum_{j=0}^k \frac{f^{(j)}(a)}{j!}(x-a)^j.
$$

Taylor polynomials provide the canonical local polynomial approximation to $f$ near $a$. Taylor's theorem quantifies the error via a {{< knowl id="remainder-term-in-taylors-theorem" text="remainder term" >}}.

**Examples:**
- For $f(x)=e^x$, $T_2 f(x;0)=1+x+\frac{x^2}{2}$.
- For $f(x)=\sin x$, $T_3 f(x;0)=x-\frac{x^3}{3!}$.
- For $f(x)=\frac{1}{1-x}$, the Taylor polynomial at $0$ is $T_k f(x;0)=\sum_{j=0}^k x^j$.
