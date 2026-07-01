+++
id = "algebra-rings/gcd"
title = "Greatest common divisor"
kind = "knowl"
summary = "A divisor d of a and b that is divisible by every common divisor (defined up to associates)."
aliases = ["gcd", "Greatest common divisor"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/gcd.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]] and let $a,b\in R$. A **greatest common divisor** of $a$ and $b$ is an element $d\in R$ such that:
1. $d\mid a$ and $d\mid b$, and
2. if $c\mid a$ and $c\mid b$, then $c\mid d$.

A gcd is unique up to [[algebra-rings/associated-elements|associates]] (so one often fixes a “normal form” when possible). When gcds exist for all pairs, one can define lcms and obtain identities relating gcd and [[algebra-rings/lcm|lcm]].

**Examples:**
- In $\mathbb{Z}$, $\gcd(12,18)=6$.
- In $\mathbb{Q}[x]$, a gcd of $x^2-1$ and $x^2-3x+2$ is $x-1$ (up to nonzero rational scalars).
- For any $a\in R$, a gcd of $a$ and $0$ is $a$ (up to associates).
