+++
id = "real-analysis/order-axioms"
title = "Order axioms"
kind = "knowl"
summary = "Axioms for a total order compatible with addition and multiplication on the real numbers."
aliases = ["order-axioms", "Order axioms"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/order-axioms.md"
+++

**Order axioms:** Let $F$ be a field (satisfying the [[real-analysis/field-axioms|field axioms]]) and let $\le$ be a [[shared-foundations/relation|relation]] on $F$. The following are required for all $a,b,c\in F$:

- (Reflexivity) $a\le a$.
- (Antisymmetry) if $a\le b$ and $b\le a$, then $a=b$.
- (Transitivity) if $a\le b$ and $b\le c$, then $a\le c$.
- (Totality) for any $a,b$, either $a\le b$ or $b\le a$.
- (Compatibility with addition) if $a\le b$, then $a+c\le b+c$.
- (Compatibility with multiplication) if $0\le a$ and $0\le b$, then $0\le ab$.

A field equipped with such an order is an ordered field; the real numbers form the standard example. The order interacts with the [[real-analysis/absolute-value|absolute value]] and underlies definitions of [[real-analysis/interval|intervals]], bounds, and $\varepsilon$–$\delta$ limits.
