---
title: "Limit at infinity"
description: "The epsilon-M definition of the limit of a function as x goes to plus or minus infinity."
---

A **limit at infinity** for a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:D\to\mathbb R$ is a number $L\in\mathbb R$ such that: for every $\varepsilon>0$ there exists $M\in\mathbb R$ with the property that whenever $x\in D$ and $x>M$, one has $|f(x)-L|<\varepsilon$. One writes $\lim_{x\to\infty} f(x)=L$. Similarly, $\lim_{x\to-\infty} f(x)=L$ means that for every $\varepsilon>0$ there exists $M$ such that $x<M$ implies $|f(x)-L|<\varepsilon$.

This is an asymptotic version of the {{< knowl id="limit-at-a-point" text="limit at a point" >}} definition, with “$x$ close to $a$” replaced by “$x$ large in magnitude.” It is commonly used to describe end behavior on unbounded {{< knowl id="interval" text="intervals" >}}.

**Examples:**
- $\lim_{x\to\infty}\tfrac1x=0$.
- $\lim_{x\to\infty}\tfrac{2x+1}{x}=2$.
