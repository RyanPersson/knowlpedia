---
title: "Sylow Conjugacy Lemma"
description: "Every p-subgroup lies in a conjugate of a Sylow p-subgroup"
---

**Sylow Conjugacy Lemma**: Let $G$ be a finite {{</* knowl id="group" text="group" */>}}, let $p$ be a prime, and let $P$ be a {{</* knowl id="sylow-subgroup" text="Sylow p-subgroup" */>}} of $G$. If $Q\le G$ is a subgroup whose order is a power of $p$ (equivalently, $Q$ is a finite {{</* knowl id="p-group" text="p-group" */>}}), then there exists $g\in G$ such that $Q\le gPg^{-1}$.

In particular, any two Sylow $p$-subgroups are conjugate in $G$ (take $Q$ to be another Sylow $p$-subgroup), a key input toward {{</* knowl id="sylows-second-theorem" text="Sylow's second theorem" */>}}.

**Proof sketch**: Consider the {{</* knowl id="group-action" text="action" */>}} of $Q$ on the set of left cosets $G/P$ by left multiplication. Counting fixed points modulo $p$ shows there is a fixed coset $gP$, which implies $g^{-1}Qg\le P$, i.e. $Q\le gPg^{-1}$.
