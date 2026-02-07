---
title: "Module"
description: "An abelian group equipped with a compatible scalar action by a ring (left or right)."
---

Let $R$ be a {{< knowl id="ring" section="algebra-rings" text="ring" >}} (often assumed a {{< knowl id="unital-ring" section="algebra-rings" text="unital ring" >}}). A **left $R$-module** is an abelian group $(M,+)$ together with a scalar multiplication map $R\times M\to M$, $(r,m)\mapsto rm$, such that for all $r,s\in R$ and $m,n\in M$:
1. $r(m+n)=rm+rn$,
2. $(r+s)m=rm+sm$,
3. $(rs)m=r(sm)$,
4. if $R$ is unital, then $1_R m=m$.

A **right $R$-module** is defined similarly with a map $M\times R\to M$, $(m,r)\mapsto mr$, satisfying the analogous axioms.

The axioms are collected in {{< knowl id="module-axioms" text="module axioms" >}}. When $R$ is a {{< knowl id="field" section="algebra-rings" text="field" >}}, left $R$-modules are the same objects as {{< knowl id="vector-space" section="linear-algebra" text="vector spaces" >}}. Ideals of a ring give basic examples of modules, linking module theory to {{< knowl id="ideal" section="algebra-rings" text="ideal" >}} theory.

**Examples:**
- For any ring $R$, the additive group of $R$ is a left $R$-module via multiplication: $r\cdot x=rx$.
- For $R=\mathbb Z$, a left $\mathbb Z$-module is exactly an abelian group (with $n\cdot m$ defined as repeated addition).
- If $I\lhd R$ is an ideal, then $I$ is an $R$-module under the restricted multiplication action.
