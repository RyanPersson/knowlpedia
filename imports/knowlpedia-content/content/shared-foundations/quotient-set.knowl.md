+++
id = "shared-foundations/quotient-set"
title = "Quotient set"
kind = "knowl"
summary = "The set of equivalence classes of a set under an equivalence relation"
aliases = ["quotient-set", "Quotient set"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/quotient-set.md"
+++

A **quotient set** is the set of equivalence classes determined by an equivalence relation: if $A$ is a [[shared-foundations/set|set]] and $\sim$ is an [[shared-foundations/equivalence-relation|equivalence relation]] on $A$, then the quotient set $A/{\sim}$ is
$$
A/{\sim}=\{[a]_{\sim}: a\in A\},\qquad [a]_{\sim}=\{x\in A: x\sim a\}.
$$

Each element of $A/{\sim}$ is an [[shared-foundations/equivalence-class|equivalence class]], and the collection of all classes forms a [[shared-foundations/partition|partition]] of $A$. Conversely, any partition of $A$ determines an equivalence relation and hence a quotient set.

**Examples:**
- On [[shared-foundations/integers|the integers]], fix $n\in\mathbb{N}$ with $n\ge 2$ and define $a\sim b$ if $a-b$ is divisible by $n$; then $\mathbb{Z}/{\sim}$ is the set of congruence classes modulo $n$.
- On [[shared-foundations/real-numbers|the real numbers]], define $x\sim y$ if $x-y\in\mathbb{Z}$; then $\mathbb{R}/{\sim}$ identifies real numbers that differ by an integer.
