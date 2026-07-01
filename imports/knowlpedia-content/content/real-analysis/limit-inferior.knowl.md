+++
id = "real-analysis/limit-inferior"
title = "Limit inferior"
kind = "knowl"
summary = "The eventual lower limiting value of a real sequence."
aliases = ["limit-inferior", "Limit inferior"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-inferior.md"
+++

A **limit inferior** of a real sequence $(a_n)_{n\ge 1}$ is the extended real number
\[
\liminf_{n\to\infty} a_n \;=\; \sup_{n\ge 1}\,\inf_{k\ge n} a_k,
\]
provided the right-hand side is interpreted in $[-\infty,\infty]$.

This definition is built from repeated use of [[real-analysis/infimum|infimum]] and [[real-analysis/supremum|supremum]] on the tails of the sequence. Together with the [[real-analysis/limit-superior|limit superior]], it describes the full range of subsequential behavior via [[real-analysis/subsequence|subsequences]].

**Examples:**
- If $a_n=(-1)^n$, then $\liminf_{n\to\infty} a_n=-1$.
- If $a_n=\tfrac1n$, then $\liminf_{n\to\infty} a_n=0$.
