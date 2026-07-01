+++
id = "algebra-groups/sylow-congruence"
title = "Sylow Congruence"
kind = "knowl"
summary = "The number n_p of Sylow p-subgroups satisfies n_p ≡ 1 (mod p)."
aliases = ["sylow-congruence", "Sylow Congruence"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/sylow-congruence.md"
+++

**Sylow Congruence**: Let $G$ be a finite [[algebra-groups/group|group]] and let $p$ be a prime. Write $|G|=p^a m$ with $a\ge 1$ and $p\nmid m$. Let $n_p$ be the number of [[algebra-groups/sylow-subgroup|Sylow p-subgroups]] of $G$. Then
$$n_p \equiv 1 \pmod p.$$

This congruence is part of the standard consequences of [[algebra-groups/sylows-third-theorem|Sylow's third theorem]]. A common proof uses a [[algebra-groups/conjugation-action|conjugation action]] and the orbit decomposition of a finite [[algebra-groups/group-action|group action]].


**Examples:**
- If $|G|=12$ and $p=3$, then $n_3\mid 4$ and $n_3\equiv 1\pmod 3$, so $n_3\in\{1,4\}$.
- If $|G|=21=3\cdot 7$, then $n_7\mid 3$ and $n_7\equiv 1\pmod 7$, forcing $n_7=1$. Hence the Sylow $7$-subgroup is [[algebra-groups/normal-subgroup|normal]] (by [[algebra-groups/sylow-normal-criterion|the n_p=1 normality criterion]]).
