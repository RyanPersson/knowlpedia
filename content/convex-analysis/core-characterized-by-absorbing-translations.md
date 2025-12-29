---
title: "Core Characterized by Absorbing Translations"
description: "A point lies in core(Ω) iff translating Ω by that point makes it absorbing"
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}} and $\Omega\subset X$ be nonempty. For $x\in X$, consider the translate $\Omega-x:=\{w-x\mid w\in\Omega\}$ (using {{< knowl id="set-operations-sum-scalar-multiple-difference" text="set difference/translation notation" >}}).

**Proposition**: A point $x\in X$ lies in {{< knowl id="algebraic-interior-core" text="core(Ω)" >}} if and only if $\Omega-x$ is an {{< knowl id="balanced-and-absorbing-sets" text="absorbing set" >}}, i.e., for every $v\in X$ there exists $\lambda>0$ such that $v\in \alpha(\Omega-x)$ for all scalars $\alpha$ with $|\alpha|\ge \lambda$.

**Context:** This characterization turns the "two-sided line" definition of the core into a scaling condition that is often easier to check in practice.
