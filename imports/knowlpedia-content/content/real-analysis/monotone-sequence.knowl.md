+++
id = "real-analysis/monotone-sequence"
title = "Monotone sequence"
kind = "knowl"
summary = "A real sequence that is nondecreasing or nonincreasing."
aliases = ["monotone-sequence", "Monotone sequence"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/monotone-sequence.md"
+++

A **monotone sequence** is a sequence $(a_n)_{n\ge 1}$ of real numbers such that either
- $a_n\le a_{n+1}$ for all $n$ (monotone increasing), or
- $a_n\ge a_{n+1}$ for all $n$ (monotone decreasing).

A sequence can be viewed as a [[shared-foundations/function|function]] from $\mathbb N$ to $\mathbb R$. Monotone sequences are central in the [[real-analysis/monotone-sequence-convergence-theorem|monotone sequence convergence theorem]], which combines monotonicity with being [[real-analysis/bounded-above|bounded above]] or [[real-analysis/bounded-below|bounded below]].

**Examples:**
- $a_n=1-\tfrac1n$ is monotone increasing.
- $a_n=\tfrac1n$ is monotone decreasing.
