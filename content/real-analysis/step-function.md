---
title: "Step function"
description: "A function that is constant on each subinterval of some partition."
---

A **step function** on $[a,b]$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $s:[a,b]\to\mathbb R$ for which there exists a {{< knowl id="partition-of-an-interval" text="partition" >}} $P=\{x_0,\dots,x_n\}$ and constants $c_1,\dots,c_n$ such that
\[
s(x)=c_i \quad \text{for all } x\in(x_{i-1},x_i),\ i=1,\dots,n.
\]
The values of $s$ at the partition points $x_i$ can be chosen arbitrarily without changing this property.

Step functions are basic building blocks in the theory of the {{< knowl id="riemann-integral" text="Riemann integral" >}}; in particular, they are {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} and play a role analogous to a {{< knowl id="simple-function" section="measure-theory" text="simple function" >}} in measure theory.

**Examples:**
- Any constant function $s(x)=c$ on $[a,b]$ is a step function (take $P=\{a,b\}$).
- On $[-1,1]$, the function $s(x)=0$ for $x<0$ and $s(x)=1$ for $x>0$ is a step function (take $P=\{-1,0,1\}$).
