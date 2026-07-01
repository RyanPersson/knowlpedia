+++
id = "real-analysis/step-function"
title = "Step function"
kind = "knowl"
summary = "A function that is constant on each subinterval of some partition."
aliases = ["step-function", "Step function"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/step-function.md"
+++

A **step function** on $[a,b]$ is a [[shared-foundations/function|function]] $s:[a,b]\to\mathbb R$ for which there exists a [[real-analysis/partition-of-an-interval|partition]] $P=\{x_0,\dots,x_n\}$ and constants $c_1,\dots,c_n$ such that
\[
s(x)=c_i \quad \text{for all } x\in(x_{i-1},x_i),\ i=1,\dots,n.
\]
The values of $s$ at the partition points $x_i$ can be chosen arbitrarily without changing this property.

Step functions are basic building blocks in the theory of the [[real-analysis/riemann-integral|Riemann integral]]; in particular, they are [[real-analysis/riemann-integrable-function|Riemann integrable]] and play a role analogous to a [[measure-theory/simple-function|simple function]] in measure theory.

**Examples:**
- Any constant function $s(x)=c$ on $[a,b]$ is a step function (take $P=\{a,b\}$).
- On $[-1,1]$, the function $s(x)=0$ for $x<0$ and $s(x)=1$ for $x>0$ is a step function (take $P=\{-1,0,1\}$).
