+++
id = "algebra-rings/euclidean-domain"
title = "Euclidean domain"
kind = "knowl"
summary = "An integral domain admitting division with remainder controlled by a Euclidean function."
aliases = ["euclidean-domain", "Euclidean domain"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/euclidean-domain.md"
+++

A **Euclidean domain** is an [[algebra-rings/integral-domain|integral domain]] $R$ equipped with a function $\delta:R\setminus\{0\}\to \mathbb{N}$ such that for all $a\in R$ and $b\in R\setminus\{0\}$, there exist $q,r\in R$ with $a=bq+r$ and either $r=0$ or $\delta(r)<\delta(b)$.

This “division algorithm” implies the [[algebra-rings/euclidean-algorithm|Euclidean algorithm]] and ensures existence of [[algebra-rings/gcd|gcds]]. In particular, every Euclidean domain is a [[algebra-rings/pid|PID]] (see [[algebra-rings/euclidean-implies-pid|Euclidean implies PID]]).

**Examples:**
- $\mathbb{Z}$ with $\delta(n)=|n|$ is Euclidean.
- If $k$ is a field, then $k[x]$ is Euclidean with $\delta(f)=\deg(f)$ for $f\neq 0$.
- $k[x,y]$ is not Euclidean (it is not even a PID).
