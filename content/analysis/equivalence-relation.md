---
title: "Equivalence relation"
description: "A relation that is reflexive, symmetric, and transitive."
---

An **equivalence relation** on a {{< knowl id="set" text="set" >}} $X$ is a {{< knowl id="relation" text="relation" >}} $\sim\ \subseteq X\times X$ such that for all $x,y,z\in X$:
- (**Reflexive**) $x\sim x$.
- (**Symmetric**) If $x\sim y$, then $y\sim x$.
- (**Transitive**) If $x\sim y$ and $y\sim z$, then $x\sim z$.

Equivalence relations formalize "sameness up to a criterion." They {{< knowl id="partition" text="partition" >}} $X$ into {{< knowl id="equivalence-class" text="equivalence classes" >}}, and many constructions in mathematics are quotients by equivalence relations.

**Examples:**
- On $\mathbb{Z}$, define $a\sim b$ iff $a\equiv b\pmod n$ for a fixed $n\in\mathbb{N}$; this is an equivalence relation.
- Equality on any set $X$, defined by $x\sim y$ iff $x=y$, is an equivalence relation.
- On $\mathbb{R}$, define $x\sim y$ iff $x-y\in\mathbb{Q}$; this is an equivalence relation whose classes are cosets $x+\mathbb{Q}$.
