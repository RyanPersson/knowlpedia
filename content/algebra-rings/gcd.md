---
title: "Greatest common divisor"
description: "A divisor d of a and b that is divisible by every common divisor (defined up to associates)."
---

Let $R$ be an {{< knowl id="integral-domain" text="integral domain" >}} and let $a,b\in R$. A **greatest common divisor** of $a$ and $b$ is an element $d\in R$ such that:
1. $d\mid a$ and $d\mid b$, and
2. if $c\mid a$ and $c\mid b$, then $c\mid d$.

A gcd is unique up to {{< knowl id="associated-elements" text="associates" >}} (so one often fixes a “normal form” when possible). When gcds exist for all pairs, one can define lcms and obtain identities relating gcd and {{< knowl id="lcm" text="lcm" >}}.

**Examples:**
- In $\mathbb{Z}$, $\gcd(12,18)=6$.
- In $\mathbb{Q}[x]$, a gcd of $x^2-1$ and $x^2-3x+2$ is $x-1$ (up to nonzero rational scalars).
- For any $a\in R$, a gcd of $a$ and $0$ is $a$ (up to associates).