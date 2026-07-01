+++
id = "real-analysis/limit-superior"
title = "Limit superior"
kind = "knowl"
summary = "The eventual upper limiting value of a real sequence."
aliases = ["limit-superior", "Limit superior"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-superior.md"
+++

A **limit superior** of a real sequence $(a_n)_{n\ge 1}$ is the extended real number
\[
\limsup_{n\to\infty} a_n \;=\; \inf_{n\ge 1}\,\sup_{k\ge n} a_k,
\]
provided the right-hand side is interpreted in $[-\infty,\infty]$.

This definition is built from repeated use of [[real-analysis/supremum|supremum]] and [[real-analysis/infimum|infimum]] on the “tails” of the sequence. It packages subsequential behavior: values near $\limsup a_n$ are realized along suitable [[real-analysis/subsequence|subsequences]].

**Examples:**
- If $a_n=(-1)^n$, then $\limsup_{n\to\infty} a_n=1$.
- If $a_n=\tfrac1n$, then $\limsup_{n\to\infty} a_n=0$.
