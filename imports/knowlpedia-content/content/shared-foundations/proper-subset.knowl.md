+++
id = "shared-foundations/proper-subset"
title = "Proper subset"
kind = "knowl"
summary = "A subset that is strictly smaller than the set it sits inside."
aliases = ["proper-subset", "Proper subset"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/proper-subset.md"
+++

A **proper subset** of a set $B$ is a set $A$ such that $A\subseteq B$ and $A\neq B$. One writes $A\subsetneq B$ (or $A\subset B$ in contexts where ambiguity is avoided).

Proper inclusion strengthens the [[shared-foundations/subset|subset]] relation by excluding equality, and it often appears when describing strict containments such as $A\subsetneq A\cup\{x\}$.

**Examples:**
- $\{1,2\}\subsetneq \{1,2,3\}$.
- For any set $A$, $\varnothing\subsetneq A$ holds exactly when $A\neq \varnothing$.
