---
title: "Limit inferior"
description: "The eventual lower limiting value of a real sequence."
---

A **limit inferior** of a real sequence $(a_n)_{n\ge 1}$ is the extended real number
\[
\liminf_{n\to\infty} a_n \;=\; \sup_{n\ge 1}\,\inf_{k\ge n} a_k,
\]
provided the right-hand side is interpreted in $[-\infty,\infty]$.

This definition is built from repeated use of {{< knowl id="infimum" text="infimum" >}} and {{< knowl id="supremum" text="supremum" >}} on the tails of the sequence. Together with the {{< knowl id="limit-superior" text="limit superior" >}}, it describes the full range of subsequential behavior via {{< knowl id="subsequence" text="subsequences" >}}.

**Examples:**
- If $a_n=(-1)^n$, then $\liminf_{n\to\infty} a_n=-1$.
- If $a_n=\tfrac1n$, then $\liminf_{n\to\infty} a_n=0$.
