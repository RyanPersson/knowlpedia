+++
id = "algebra-rings/maximal-ideal"
title = "Maximal ideal"
kind = "knowl"
summary = "A proper ideal maximal under inclusion; in the commutative unital case, equivalently the quotient is a field."
aliases = ["maximal-ideal", "Maximal ideal"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/maximal-ideal.md"
+++

Let $R$ be a [[algebra-rings/commutative-ring|commutative ring]] with $1\neq 0$. A **maximal ideal** $M\subsetneq R$ is a proper [[algebra-rings/ideal|ideal]] such that there is no ideal $I$ with $M\subsetneq I\subsetneq R$.

Maximal ideals are characterized by quotients: $M$ is maximal if and only if the [[algebra-rings/quotient-ring|quotient ring]] $R/M$ is a [[algebra-rings/field|field]]. In commutative algebra, every maximal ideal is [[algebra-rings/prime-ideal|prime]].

**Examples:**
- In $\mathbb{Z}$, the ideal $(p)$ is maximal exactly when $p$ is a prime integer; then $\mathbb{Z}/(p)\cong \mathbb{F}_p$.
- If $k$ is a field, then in $k[x]$ the ideal $(x-a)$ is maximal for any $a\in k$.
- The ideal $(0)\subset \mathbb{Z}$ is not maximal since $(0)\subsetneq (2)\subsetneq \mathbb{Z}$.
