+++
id = "real-analysis/sup-inf-algebra"
title = "Supremum and Infimum Algebra"
kind = "knowl"
summary = "How supremum and infimum interact with basic set operations such as translation and scaling."
aliases = ["sup-inf-algebra", "Supremum and Infimum Algebra"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/sup-inf-algebra.md"
+++

**Supremum/infimum algebra:** Let $A,B \subseteq \mathbb{R}$ be nonempty [[shared-foundations/subset|subsets]]. Define
$A+B=\{a+b:\ a\in A,\ b\in B\}$ and, for $c\in\mathbb{R}$, $cA=\{ca:\ a\in A\}$.
Assume the displayed quantities are finite (for example, by assuming the relevant [[real-analysis/bounded-above|bounded above]] or [[real-analysis/bounded-below|bounded below]] hypotheses). Then:

- $\sup(A+B)=\sup(A)+\sup(B)$ and $\inf(A+B)=\inf(A)+\inf(B)$.
- If $c\ge 0$, then $\sup(cA)=c\,\sup(A)$ and $\inf(cA)=c\,\inf(A)$.
- If $c\le 0$, then $\sup(cA)=c\,\inf(A)$ and $\inf(cA)=c\,\sup(A)$.
- Writing $-A=\{-a:\ a\in A\}$, one has $\sup(-A)=-\inf(A)$ and $\inf(-A)=-\sup(A)$.

These rules are frequently paired with the [[real-analysis/supremum-approximation-lemma|supremum approximation lemma]] to turn statements about [[real-analysis/supremum|suprema]] and [[real-analysis/infimum|infima]] into $\varepsilon$-estimates.
