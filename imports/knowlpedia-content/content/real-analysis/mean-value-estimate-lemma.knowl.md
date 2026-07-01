+++
id = "real-analysis/mean-value-estimate-lemma"
title = "Mean value estimate"
kind = "knowl"
summary = "A bound on the change in a function in terms of a bound on its derivative."
aliases = ["mean-value-estimate-lemma", "Mean value estimate"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mean-value-estimate-lemma.md"
+++

**Mean value estimate lemma:** Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and [[real-analysis/differentiability-1d|differentiable]] on $(a,b)$. If there exists $M\ge 0$ such that $|f'(x)|\le M$ for all $x\in(a,b)$, then
$$
|f(b)-f(a)|\le M\,|b-a|.
$$

This is an immediate quantitative consequence of the [[real-analysis/mean-value-theorem|mean value theorem]] and is a standard step in results like [[real-analysis/bounded-derivative-implies-uniform-continuity|bounded derivative implies uniform continuity]].
