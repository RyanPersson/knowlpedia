+++
id = "analysis/absolute-continuity"
title = "Absolute continuity"
kind = "knowl"
summary = "A strong continuity condition on an interval controlling total change over collections of small subintervals"
aliases = ["absolute-continuity", "Absolute continuity"]
domains = ["analysis"]
legacy_source_path = "analysis/absolute-continuity.md"
+++

A function $f:[a,b]\to\mathbb{R}$ is **absolutely continuous** if for every $\varepsilon>0$ there exists $\delta>0$ such that for every finite collection of pairwise disjoint subintervals $(a_k,b_k)\subseteq [a,b]$ with $\sum_k (b_k-a_k)<\delta$, one has
\[
\sum_k |f(b_k)-f(a_k)|<\varepsilon.
\]

Absolute continuity is stronger than [[real-analysis/uniform-continuity|uniform continuity]] and implies [[real-analysis/bounded-variation-function|bounded variation]]. A key characterization is that $f$ is absolutely continuous if and only if there exists a [[measure-theory/lebesgue-integrable-function|Lebesgue integrable function]] $g$ on $[a,b]$ such that $f(x)=f(a)+\int_a^x g(t)\,dt$ for all $x\in[a,b]$ (with the integral taken as the [[measure-theory/lebesgue-integral|Lebesgue integral]]); in that case the [[real-analysis/derivative|derivative]] satisfies $f'(x)=g(x)$ [[measure-theory/almost-everywhere|almost everywhere]].

**Examples:**
- If $g$ is Lebesgue integrable on $[a,b]$ and $f(x)=\int_a^x g(t)\,dt$, then $f$ is absolutely continuous.
- Every [[topology/lipschitz-continuity|Lipschitz continuous]] function on $[a,b]$ is absolutely continuous.
- The Cantor function is continuous and of bounded variation but not absolutely continuous; it increases on a [[measure-theory/set-of-measure-zero-in-rk|set of measure zero]].
