---
title: "Burnside's p^a q^b Theorem"
description: "A finite group of order p^a q^b (two primes) is solvable"
---

**Burnside's p^a q^b Theorem.**
Let $G$ be a finite {{< knowl id="group" text="group" >}} with
$$
|G| = p^{a}q^{b}
$$
for primes $p,q$ and integers $a,b \ge 0$. Then $G$ is a {{< knowl id="solvable-group" text="solvable group" >}}.

This theorem is a landmark result: finiteness together with "at most two prime divisors" forces strong structural constraints. Standard proofs use tools from {{< knowl id="group-representation" text="representation theory" >}}, especially properties of {{< knowl id="character" text="characters" >}} of finite groups, to produce a nontrivial normal subgroup and then argue by induction on $|G|$.

**Proof sketch.**
One shows (using character theory) that $G$ has a nontrivial proper normal subgroup $N$. Then both $N$ and $G/N$ again have order of the form $p^{a'}q^{b'}$, so by induction they are solvable, and solvability is inherited by extensions.
