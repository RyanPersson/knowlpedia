---
title: "Basic Properties of limsup and liminf"
description: "Standard inequalities and identities involving limit superior and limit inferior."
---

**limsup/liminf properties:** Let $(a_n)$ and $(b_n)$ be real sequences, and let $\limsup$ and $\liminf$ denote the {{< knowl id="limit-superior" text="limit superior" >}} and {{< knowl id="limit-inferior" text="limit inferior" >}}.

1. Always $\liminf a_n \le \limsup a_n$.
2. If $a_n \le b_n$ for all sufficiently large $n$, then $\limsup a_n \le \limsup b_n$ and $\liminf a_n \le \liminf b_n$.
3. One has $\liminf a_n = -\,\limsup(-a_n)$.
4. If $(a_n)$ converges to $L$ (as a {{< knowl id="convergent-sequence" section="topology" text="convergent sequence" >}}), then $\limsup a_n=\liminf a_n=L$.
5. If $\limsup a_n < \alpha$, then there exists $N$ such that $a_n < \alpha$ for all $n\ge N$; if $\liminf a_n > \beta$, then there exists $N$ such that $a_n > \beta$ for all $n\ge N$.

These properties allow one to convert eventual bounds into statements about $\limsup$ and $\liminf$, and conversely, which is useful in comparison and convergence arguments.
