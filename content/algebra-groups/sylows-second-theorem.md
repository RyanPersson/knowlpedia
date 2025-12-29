---
title: "Sylow's Second Theorem"
description: "All Sylow p-subgroups are conjugate, and every p-subgroup lies in one"
---

**Sylow's Second Theorem.**
Let $G$ be a finite {{< knowl id="group" text="group" >}}, let $p$ be a prime, and let $P$ be a {{< knowl id="sylow-subgroup" text="Sylow p-subgroup" >}} of $G$. If $Q \le G$ is any {{< knowl id="p-group" text="p-group" >}} (equivalently, $|Q|$ is a power of $p$), then there exists $g\in G$ such that
$$
Q \subseteq gPg^{-1}.
$$
In particular, any two Sylow $p$-subgroups of $G$ are conjugate (they lie in the same orbit under the {{< knowl id="conjugation-action" text="conjugation action" >}}).

Sylow's second theorem implies Sylow $p$-subgroups are "unique up to conjugacy," and it is the key input for the normality test {{< knowl id="sylow-normal-criterion" text="n_p=1 implies the Sylow p-subgroup is normal" >}}. It is typically proved using {{< knowl id="sylows-first-theorem" text="Sylow's first theorem" >}} plus an action on cosets.

**Proof sketch.**
Let $Q$ act by left multiplication on the set of left cosets $G/P$. Orbit sizes are powers of $p$, so the number of fixed points is congruent to $|G/P|$ modulo $p$. A fixed point corresponds to a coset $gP$ with $Q \subseteq gPg^{-1}$, forcing such a conjugate to contain $Q$.
