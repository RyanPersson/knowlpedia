---
title: "Finite Field Multiplicative Group is Cyclic"
description: "The nonzero elements of a finite field form a cyclic group."
---

**Theorem.**  
If \( \mathbb{F}_q \) is a {{< knowl id="finite-field" text="finite field" >}}, then its multiplicative group
\[
\mathbb{F}_q^\times = \mathbb{F}_q\setminus\{0\}
\]
is a {{< knowl id="group" section="algebra-groups" text="group" >}} that is {{< knowl id="finite-field-multiplicative-cyclic" text="cyclic" >}} of order \(q-1\). In particular, there exists a **primitive element** \(g\in \mathbb{F}_q^\times\) such that \(\mathbb{F}_q^\times=\langle g\rangle\).

**Examples.**
1. \(\mathbb{F}_5^\times=\{1,2,3,4\}\) is cyclic of order \(4\); \(2\) is a generator since \(2,2^2=4,2^3=3,2^4=1\).
2. \(\mathbb{F}_7^\times\) is cyclic of order \(6\); \(3\) generates because its powers give all nonzero residues mod \(7\).
3. \(\mathbb{F}_8^\times\) has order \(7\), hence is cyclic (every group of prime order is cyclic).

**Related.** {{< knowl id="cyclic-subgroup" section="algebra-groups" text="cyclic subgroups" >}}, {{< knowl id="finite-field-existence-uniqueness" text="finite fields exist uniquely" >}}.
