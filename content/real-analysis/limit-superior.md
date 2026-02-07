---
title: "Limit superior"
description: "The eventual upper limiting value of a real sequence."
---

A **limit superior** of a real sequence $(a_n)_{n\ge 1}$ is the extended real number
\[
\limsup_{n\to\infty} a_n \;=\; \inf_{n\ge 1}\,\sup_{k\ge n} a_k,
\]
provided the right-hand side is interpreted in $[-\infty,\infty]$.

This definition is built from repeated use of {{< knowl id="supremum" text="supremum" >}} and {{< knowl id="infimum" text="infimum" >}} on the “tails” of the sequence. It packages subsequential behavior: values near $\limsup a_n$ are realized along suitable {{< knowl id="subsequence" text="subsequences" >}}.

**Examples:**
- If $a_n=(-1)^n$, then $\limsup_{n\to\infty} a_n=1$.
- If $a_n=\tfrac1n$, then $\limsup_{n\to\infty} a_n=0$.
