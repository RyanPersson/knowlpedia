---
title: "Euler's Theorem"
description: "If gcd(a,n)=1 then a^{φ(n)} ≡ 1 (mod n)."
---

**Euler's Theorem**: Let $n\ge 1$ and let $a\in\mathbb{Z}$. If the {{< knowl id="gcd" section="algebra-rings" text="greatest common divisor" >}} of $a$ and $n$ is $1$ (written $\gcd(a,n)=1$), then
$$a^{\varphi(n)} \equiv 1 \pmod n,$$

where $\varphi(n)$ is Euler's totient function, defined by
$$\varphi(n)=\bigl|\{\,k\in\{1,2,\dots,n\}: \gcd(k,n)=1\,\}\bigr|.$$

As usual, $x \equiv y \pmod n$ means $n$ divides $x-y$.

This follows immediately from {{< knowl id="lagranges-theorem" text="Lagrange's theorem" >}} applied to the {{< knowl id="group-of-units" section="algebra-rings" text="group of units" >}} $(\mathbb{Z}/n\mathbb{Z})^\times$, a finite {{< knowl id="group" text="group" >}} with $|(\mathbb{Z}/n\mathbb{Z})^\times|=\varphi(n)$. The special case $n=p$ prime is {{< knowl id="fermats-little-theorem" text="Fermat's little theorem" >}}.


**Examples:**
- $n=10$, $a=3$: $\varphi(10)=4$, and $3^4=81\equiv 1 \pmod{10}$.
- $n=12$, $a=5$: $\varphi(12)=4$, and $5^4=625\equiv 1 \pmod{12}$.
- The hypothesis $\gcd(a,n)=1$ matters: for $n=8$, $a=2$ we have $\gcd(2,8)\ne 1$, and indeed $2^{\varphi(8)}=2^4=16\equiv 0 \pmod 8\neq 1$.
