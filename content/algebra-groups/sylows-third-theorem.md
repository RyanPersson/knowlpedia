---
title: "Sylow's Third Theorem"
description: "The number of Sylow p-subgroups divides the p'-part of |G| and is ≡ 1 mod p"
---

**Sylow's Third Theorem.**
Let $G$ be a finite {{< knowl id="group" text="group" >}} with $|G| = p^{a}m$ where $p$ is prime and $p\nmid m$. Let $n_p$ denote the number of {{< knowl id="sylow-subgroup" text="Sylow p-subgroups" >}} of $G$. Then:
1. $n_p \mid m$, and
2. $n_p \equiv 1 \pmod p$.

This theorem is a counting consequence of {{< knowl id="sylows-second-theorem" text="Sylow's second theorem" >}} together with the {{< knowl id="normalizer" text="normalizer" >}} and the {{< knowl id="conjugation-action" text="conjugation action" >}} on the set of Sylow $p$-subgroups.

**Proof sketch.**
Fix a Sylow $p$-subgroup $P$. Conjugation gives a {{</* knowl id="transitive-action" text="transitive action" */>}} of $G$ on the set of Sylow $p$-subgroups, and the {{</* knowl id="stabilizer" text="stabilizer" */>}} of $P$ is $N_G(P)$, so $n_p=[G:N_G(P)]$, which divides $m$ because $P\subseteq N_G(P)$ contributes the entire $p^a$-part to $|N_G(P)|$. For the congruence, let $P$ act by conjugation on the set of Sylow $p$-subgroups; orbit sizes are $1$ or multiples of $p$, and $P$ fixes exactly the Sylow $p$-subgroups equal to itself, yielding $n_p \equiv 1 \pmod p$.
