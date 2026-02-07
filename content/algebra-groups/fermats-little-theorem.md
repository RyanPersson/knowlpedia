---
title: "Fermat's Little Theorem"
description: "For prime p, a^{p-1} ≡ 1 (mod p) when p ∤ a."
---

**Fermat's Little Theorem**: Let $p$ be a prime and let $a \in \mathbb{Z}$. Then
$$a^p \equiv a \pmod p.$$

Equivalently, if $p \nmid a$ (i.e., $a \not\equiv 0 \pmod p$), then
$$a^{p-1} \equiv 1 \pmod p.$$

Here $x \equiv y \pmod p$ means that $p$ divides $x-y$.

This is a standard application of {{< knowl id="lagranges-theorem" text="Lagrange's theorem" >}} to the {{< knowl id="group-of-units" section="algebra-rings" text="group of units" >}} $(\mathbb{Z}/p\mathbb{Z})^\times$, a finite {{< knowl id="group" text="group" >}} of order $p-1$. It is also the prime-modulus special case of {{< knowl id="eulers-theorem" text="Euler's theorem" >}} (since $\varphi(p)=p-1$).


**Examples:**
- $p=7$, $a=3$: $3^{6}=729=7\cdot 104+1$, so $3^{6}\equiv 1 \pmod 7$.
- $p=5$, $a=10$: both $10^5$ and $10$ are divisible by $5$, so $10^5 \equiv 10 \pmod 5$ (this is the "$a^p \equiv a$" form).
- If $p \nmid a$, then $a^{p-2}$ is a multiplicative inverse of $a$ modulo $p$ (since $a\cdot a^{p-2}=a^{p-1}\equiv 1$). For instance, with $p=7$, $a=3$: $3^{5}=243=7\cdot 34+5$, so $3^{-1}\equiv 5 \pmod 7$ because $3\cdot 5=15\equiv 1 \pmod 7$.
