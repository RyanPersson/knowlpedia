+++
id = "algebra-groups/conjugation-preserves-order"
title = "Conjugation preserves order"
kind = "knowl"
summary = "Conjugate elements have the same order in a group"
aliases = ["conjugation-preserves-order", "Conjugation preserves order"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/conjugation-preserves-order.md"
+++

**Proposition (Conjugation preserves order).**
Let $G$ be a [[algebra-groups/group|group]]. For $x\in G$, the **order** of $x$, denoted $\mathrm{ord}(x)$, is the least positive integer $n$ such that $x^n=e$ (if such an $n$ exists), and $\mathrm{ord}(x)=\infty$ otherwise.
If $x,y\in G$ are [[algebra-groups/conjugate-element|conjugate]], i.e. $y=gxg^{-1}$ for some $g\in G$, then $\mathrm{ord}(y)=\mathrm{ord}(x)$.

**Context.**
Many group-theoretic invariants are constant on conjugacy classes. Order is the first basic example and is used, for instance, in the class equation and Sylow theory.
