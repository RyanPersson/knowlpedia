---
title: "Subsequence"
description: "A sequence obtained by restricting to a strictly increasing sequence of indices."
---

A **subsequence** of a sequence $(a_n)_{n\ge 1}$ is a sequence of the form $(a_{n_k})_{k\ge 1}$, where $n_1<n_2<n_3<\cdots$ is a strictly increasing sequence of indices.

Subsequences are a standard way to isolate “partial” limiting behavior of a sequence; they are used in defining {{< knowl id="limit-superior" text="limit superior" >}} and {{< knowl id="limit-inferior" text="limit inferior" >}}. The {{< knowl id="monotone-subsequence-lemma" text="monotone subsequence lemma" >}} guarantees monotone subsequences under mild hypotheses.

**Examples:**
- If $a_n=(-1)^n$, then $(a_{2k})_{k\ge 1}$ is the subsequence $1,1,1,\dots$.
- If $a_n=n$, then $(a_{2k})_{k\ge 1}$ is the subsequence $2,4,6,\dots$.
