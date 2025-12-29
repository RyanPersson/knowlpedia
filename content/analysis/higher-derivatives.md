---
title: "Higher derivatives"
description: "Iterated derivatives f^(n) obtained by differentiating repeatedly."
---

Let $f:I\to\mathbb{R}$ (or $\mathbb{C}$) on an interval $I\subseteq\mathbb{R}$. If $f$ is differentiable on $I$, one can form $f'$. If $f'$ is differentiable, one defines the **second derivative**
$$f'' := (f')'.$$
Inductively, if $f^{(n-1)}$ is differentiable, the **$n$th derivative** is
$$f^{(n)} := (f^{(n-1)})'.$$

Higher derivatives quantify higher-order local behavior and appear in Taylor expansions and smoothness classes.

**Examples:**
- If $f(x)=x^m$, then $f^{(n)}(x)=m(m-1)\cdots(m-n+1)\,x^{m-n}$ for $n\le m$, and $f^{(n)}\equiv 0$ for $n>m$.
- If $f(x)=e^x$, then $f^{(n)}(x)=e^x$ for all $n$.
- If $f(x)=|x|$, then $f'$ exists on $\mathbb{R}\setminus\{0\}$ but $f''$ does not exist as a function on any interval containing $0$.
