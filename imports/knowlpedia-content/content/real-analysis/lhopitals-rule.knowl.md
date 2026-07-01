+++
id = "real-analysis/lhopitals-rule"
title = "L'Hôpital's rule"
kind = "knowl"
summary = "A method for evaluating certain indeterminate limits by comparing derivatives."
aliases = ["lhopitals-rule", "L'Hôpital's rule"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/lhopitals-rule.md"
+++

**L'Hôpital's rule (0/0 form, one-sided):** Let $f$ and $g$ be continuous on $[a,b)$ and differentiable on $(a,b)$, and assume that $g'(x)\neq 0$ for all $x\in(a,b)$. Suppose
$$
\lim_{x\to a^+} f(x)=0
\quad\text{and}\quad
\lim_{x\to a^+} g(x)=0,
$$

and that $g(x)\neq 0$ for all $x$ sufficiently close to $a$ with $x>a$. If the limit
$$
L=\lim_{x\to a^+}\frac{f'(x)}{g'(x)}
$$

exists (as a finite number or as $\pm\infty$), then the limit
$$
\lim_{x\to a^+}\frac{f(x)}{g(x)}
$$

also exists and equals $L$.

Analogous statements hold for left-hand limits and for the $\infty/\infty$ indeterminate form, and there are versions for [[real-analysis/limit-at-infinity|limits at infinity]]. The proof is based on the [[real-analysis/cauchy-mean-value-theorem|Cauchy mean value theorem]] and is formulated in terms of [[real-analysis/one-sided-limit|one-sided limits]].
