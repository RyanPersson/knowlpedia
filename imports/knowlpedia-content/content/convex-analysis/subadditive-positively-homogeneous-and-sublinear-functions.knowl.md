+++
id = "convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions"
title = "Subadditive, Positively Homogeneous, and Sublinear Functions"
kind = "knowl"
summary = "Key algebraic properties for gauges and Hahn–Banach domination."
aliases = ["subadditive-positively-homogeneous-and-sublinear-functions", "Subadditive, Positively Homogeneous, and Sublinear Functions"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $p:X\to\mathbb{R}$.

- $p$ is **subadditive** if
  $$
  p(x+y)\le p(x)+p(y)\quad\text{for all }x,y\in X.
  $$

- $p$ is **positively homogeneous** if
  $$
  p(\lambda x)=\lambda p(x)\quad\text{for all }x\in X,\ \lambda>0.
  $$

- $p$ is **sublinear** if it is both subadditive and positively homogeneous.

Sublinear functions appear as domination bounds in [[convex-analysis/hahn-banach-theorem-in-real-vector-spaces|the real Hahn–Banach theorem]]. A primary source of sublinear functions is the [[convex-analysis/minkowski-function-gauge-of-a-set|Minkowski gauge]] of an [[convex-analysis/balanced-and-absorbing-sets|absorbing]] [[convex-analysis/convex-set|convex set]].
