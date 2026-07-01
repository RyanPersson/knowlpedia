+++
id = "real-analysis/subsequence"
title = "Subsequence"
kind = "knowl"
summary = "A sequence obtained by restricting to a strictly increasing sequence of indices."
aliases = ["subsequence"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/subsequence.md"
+++

A **subsequence** of a sequence $(a_n)_{n\ge 1}$ is a sequence of the form $(a_{n_k})_{k\ge 1}$, where $n_1<n_2<n_3<\cdots$ is a strictly increasing sequence of indices.

Subsequences are a standard way to isolate “partial” limiting behavior of a sequence; they are used in defining [[real-analysis/limit-superior|limit superior]] and [[real-analysis/limit-inferior|limit inferior]]. The [[real-analysis/monotone-subsequence-lemma|monotone subsequence lemma]] guarantees monotone subsequences under mild hypotheses.

**Examples:**
- If $a_n=(-1)^n$, then $(a_{2k})_{k\ge 1}$ is the subsequence $1,1,1,\dots$.
- If $a_n=n$, then $(a_{2k})_{k\ge 1}$ is the subsequence $2,4,6,\dots$.
