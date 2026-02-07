---
title: "Sylow Congruence"
description: "The number n_p of Sylow p-subgroups satisfies n_p ≡ 1 (mod p)."
---

**Sylow Congruence**: Let $G$ be a finite {{< knowl id="group" text="group" >}} and let $p$ be a prime. Write $|G|=p^a m$ with $a\ge 1$ and $p\nmid m$. Let $n_p$ be the number of {{< knowl id="sylow-subgroup" text="Sylow p-subgroups" >}} of $G$. Then
$$n_p \equiv 1 \pmod p.$$

This congruence is part of the standard consequences of {{< knowl id="sylows-third-theorem" text="Sylow's third theorem" >}}. A common proof uses a {{< knowl id="conjugation-action" text="conjugation action" >}} and the orbit decomposition of a finite {{< knowl id="group-action" text="group action" >}}.


**Examples:**
- If $|G|=12$ and $p=3$, then $n_3\mid 4$ and $n_3\equiv 1\pmod 3$, so $n_3\in\{1,4\}$.
- If $|G|=21=3\cdot 7$, then $n_7\mid 3$ and $n_7\equiv 1\pmod 7$, forcing $n_7=1$. Hence the Sylow $7$-subgroup is {{< knowl id="normal-subgroup" text="normal" >}} (by {{< knowl id="sylow-normal-criterion" text="the n_p=1 normality criterion" >}}).
