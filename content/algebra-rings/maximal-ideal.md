---
title: "Maximal ideal"
description: "A proper ideal maximal under inclusion; in the commutative unital case, equivalently the quotient is a field."
---

Let $R$ be a {{< knowl id="commutative-ring" text="commutative ring" >}} with $1\neq 0$. A **maximal ideal** $M\subsetneq R$ is a proper {{< knowl id="ideal" text="ideal" >}} such that there is no ideal $I$ with $M\subsetneq I\subsetneq R$.

Maximal ideals are characterized by quotients: $M$ is maximal if and only if the {{< knowl id="quotient-ring" text="quotient ring" >}} $R/M$ is a {{< knowl id="field" text="field" >}}. In commutative algebra, every maximal ideal is {{< knowl id="prime-ideal" text="prime" >}}.

**Examples:**
- In $\mathbb{Z}$, the ideal $(p)$ is maximal exactly when $p$ is a prime integer; then $\mathbb{Z}/(p)\cong \mathbb{F}_p$.
- If $k$ is a field, then in $k[x]$ the ideal $(x-a)$ is maximal for any $a\in k$.
- The ideal $(0)\subset \mathbb{Z}$ is not maximal since $(0)\subsetneq (2)\subsetneq \mathbb{Z}$.