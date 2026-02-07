---
title: "Quotient set"
description: "The set of equivalence classes of a set under an equivalence relation"
---

A **quotient set** is the set of equivalence classes determined by an equivalence relation: if $A$ is a {{< knowl id="set" text="set" >}} and $\sim$ is an {{< knowl id="equivalence-relation" text="equivalence relation" >}} on $A$, then the quotient set $A/{\sim}$ is
$$
A/{\sim}=\{[a]_{\sim}: a\in A\},\qquad [a]_{\sim}=\{x\in A: x\sim a\}.
$$

Each element of $A/{\sim}$ is an {{< knowl id="equivalence-class" text="equivalence class" >}}, and the collection of all classes forms a {{< knowl id="partition" text="partition" >}} of $A$. Conversely, any partition of $A$ determines an equivalence relation and hence a quotient set.

**Examples:**
- On {{< knowl id="integers" text="the integers" >}}, fix $n\in\mathbb{N}$ with $n\ge 2$ and define $a\sim b$ if $a-b$ is divisible by $n$; then $\mathbb{Z}/{\sim}$ is the set of congruence classes modulo $n$.
- On {{< knowl id="real-numbers" text="the real numbers" >}}, define $x\sim y$ if $x-y\in\mathbb{Z}$; then $\mathbb{R}/{\sim}$ identifies real numbers that differ by an integer.
