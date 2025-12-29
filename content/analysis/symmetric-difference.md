---
title: "Symmetric difference"
description: "The set of elements that belong to exactly one of two sets."
---

The **symmetric difference** of sets $A$ and $B$ is
$$A\triangle B := (A\setminus B)\cup(B\setminus A).$$
Equivalently, $x\in A\triangle B$ iff $(x\in A)\ \oplus\ (x\in B)$, where $\oplus$ denotes exclusive-or.

Symmetric difference measures how two sets differ and is useful as an operation on sets (it makes the power set of a fixed universe into an abelian group under $\triangle$).

**Examples:**
- If $A=\{1,2\}$ and $B=\{2,3\}$, then $A\triangle B=\{1,3\}$.
- For any set $A$, $A\triangle A=\varnothing$.
- If $A\subseteq B$, then $A\triangle B = B\setminus A$.
