---
title: "Integrator function (Riemann–Stieltjes)"
description: "The function α whose increments define the weights in Riemann–Stieltjes sums."
---

In the Riemann–Stieltjes integral $\int_a^b f\,d\alpha$, the function
$$\alpha:[a,b]\to\mathbb{R}$$
is called the **integrator** (or **integrator function**). For a partition $P:a=x_0<\cdots<x_n=b$, the weights are the increments
$$\Delta\alpha_i=\alpha(x_i)-\alpha(x_{i-1}).$$

Typically one assumes $\alpha$ is increasing (or more generally of bounded variation) to ensure good behavior of the integral and to guarantee that upper/lower sum definitions make sense.

**Examples:**
- For the usual Riemann integral, the integrator is $\alpha(x)=x$.
- If $\alpha(x)=x^2$ (increasing on $[0,\infty)$), then $\int_a^b f\,d\alpha$ weights subintervals according to changes in $x^2$.
- If $\alpha$ has jumps, the integral can encode discrete contributions (a classical motivation for Stieltjes integration).
