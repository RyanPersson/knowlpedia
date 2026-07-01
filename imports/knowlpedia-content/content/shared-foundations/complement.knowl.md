+++
id = "shared-foundations/complement"
title = "Complement"
kind = "knowl"
summary = "The elements of an ambient universe that are not in a given set."
aliases = ["complement"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/complement.md"
+++

A **complement** of a set $A$ is defined relative to a fixed ambient set (universe) $U$ with $A\subseteq U$. The complement of $A$ in $U$ is
$$
A^{c}=\{x\in U : x\notin A\}.
$$

Equivalently, $A^{c}$ is the [[shared-foundations/set-difference|set difference]] $U\setminus A$. Complements interact with [[shared-foundations/union|union]] and [[shared-foundations/intersection|intersection]] through De Morgan’s laws.

**Examples:**
- If $U=\{1,2,3,4\}$ and $A=\{1,4\}$, then $A^{c}=\{2,3\}$.
- If $U=\mathbb{R}$ and $A=\{x\in\mathbb{R}: x\ge 0\}$, then $A^{c}=\{x\in\mathbb{R}: x<0\}$.
