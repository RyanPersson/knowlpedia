---
title: "Limit at a point"
description: "The epsilon-delta definition of the limit of a function as x approaches a."
---

A **limit at a point** for a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:D\to\mathbb R$ (with $D\subseteq\mathbb R$) at a point $a\in\mathbb R$ is a number $L\in\mathbb R$ such that: for every $\varepsilon>0$ there exists $\delta>0$ with the property that whenever $x\in D$ and $0<|x-a|<\delta$, one has $|f(x)-L|<\varepsilon$. Typically one assumes that $a$ is a {{< knowl id="limit-point" section="topology" text="limit point" >}} of $D$.

The inequalities use the {{< knowl id="absolute-value" text="absolute value" >}} to measure distance on the real line. One-sided variants are captured by the {{< knowl id="one-sided-limit" text="one-sided limit" >}}.

**Examples:**
- If $f(x)=x^2$, then $\lim_{x\to 2} f(x)=4$.
- If $g(x)=\begin{cases}1,&x>0\\-1,&x<0\end{cases}$ on $D=\mathbb R\setminus\{0\}$, then $\lim_{x\to 0} g(x)$ does not exist.
