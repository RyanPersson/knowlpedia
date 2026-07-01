+++
id = "real-analysis/limit-algebra-for-sequences"
title = "Limit Algebra for Sequences"
kind = "knowl"
summary = "Rules for limits of sums, products, and quotients of convergent sequences."
aliases = ["limit-algebra-for-sequences", "Limit Algebra for Sequences"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-algebra-for-sequences.md"
+++

**Limit algebra for sequences:** Let $(a_n)$ and $(b_n)$ be real sequences, and suppose $a_n \to a$ and $b_n \to b$ (in the sense of a [[topology/convergent-sequence|convergent sequence]]). Then:

- $a_n+b_n \to a+b$ and $a_n-b_n \to a-b$.
- For any $c\in\mathbb{R}$, $c\,a_n \to c\,a$.
- $a_n b_n \to ab$.
- If $b\ne 0$ and $b_n\ne 0$ for all sufficiently large $n$, then $\frac{a_n}{b_n}\to \frac{a}{b}$.
- $|a_n|\to |a|$ (see [[real-analysis/absolute-value|absolute value]]).

These rules are used constantly to build new limits from known ones and often pair with the [[real-analysis/squeeze-theorem|squeeze theorem]] for estimates.
