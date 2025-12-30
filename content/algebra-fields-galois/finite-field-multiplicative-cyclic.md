---
title: "Cyclicity of the Multiplicative Group of a Finite Field"
description: "There exists g in F_q^× that generates all nonzero elements."
---

**Theorem.**  
If \(\mathbb{F}_q\) is a {{< knowl id="finite-field" text="finite field" >}}, then the group \(\mathbb{F}_q^\times\) of nonzero elements under multiplication is cyclic of order \(q-1\). Equivalently, there exists \(g\in\mathbb{F}_q^\times\) such that every nonzero element is \(g^k\) for some \(k\).

This is the same statement as {{< knowl id="finite-field-multiplicative-group-cyclic" text="finite-field multiplicative group is cyclic" >}}.

**Examples.**
1. In \(\mathbb{F}_5\), \(2\) is primitive: \(2^1,2^2,2^3,2^4\equiv 2,4,3,1\pmod 5\).
2. In \(\mathbb{F}_7\), \(3\) is primitive: \(3^k\) for \(k=1,\dots,6\) runs through all nonzero residues mod \(7\).
3. In \(\mathbb{F}_8\), \(\mathbb{F}_8^\times\) has order \(7\) (prime), hence is cyclic; any element \(\ne 1\) generates.

**Related.** {{< knowl id="cyclic-subgroup" text="cyclic groups" >}}, {{< knowl id="finite-field-existence-uniqueness" text="finite field structure" >}}.
