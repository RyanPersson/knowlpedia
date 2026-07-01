+++
id = "algebra-rings/lcm"
title = "Least common multiple"
kind = "knowl"
summary = "A common multiple m of a and b that divides every other common multiple (defined up to associates)."
aliases = ["lcm", "Least common multiple"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/lcm.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]] and let $a,b\in R$. A **least common multiple** of $a$ and $b$ is an element $m\in R$ such that:
1. $a\mid m$ and $b\mid m$, and
2. if $a\mid n$ and $b\mid n$, then $m\mid n$.

An lcm is unique up to [[algebra-rings/associated-elements|associates]]. In settings where [[algebra-rings/gcd|gcds]] exist, one often has the relation $m\cdot d$ is associate to $ab$, where $d$ is a gcd of $a$ and $b$.

**Examples:**
- In $\mathbb{Z}$, $\mathrm{lcm}(12,18)=36$.
- In $k[x]$, $\mathrm{lcm}(x,x^2)=x^2$ (up to multiplication by a nonzero scalar).
- For any $a\in R$, a least common multiple of $a$ and $0$ is $0$.
