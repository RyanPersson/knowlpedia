+++
id = "real-analysis/infimum"
title = "Infimum"
kind = "knowl"
summary = "The greatest lower bound of a nonempty set of real numbers."
aliases = ["infimum"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/infimum.md"
+++

An **infimum** of a nonempty set $A\subseteq\mathbb R$ that is [[real-analysis/bounded-below|bounded below]] is a real number $t\in\mathbb R$ such that:
1. $t$ is a lower bound of $A$ (i.e., $t\le x$ for all $x\in A$), and
2. for every lower bound $\ell$ of $A$, one has $\ell\le t$.

The infimum is the “greatest lower bound” and may exist even when $A$ has no [[real-analysis/minimum|minimum]]. Using the [[real-analysis/completeness-axiom|completeness axiom]], every nonempty bounded-below set of real numbers has an infimum.

**Examples:**
- If $A=(0,1)$, then $\inf A=0$.
- If $A=\{\tfrac1n : n\in\mathbb N\}$, then $\inf A=0$ (even though $0\notin A$).
