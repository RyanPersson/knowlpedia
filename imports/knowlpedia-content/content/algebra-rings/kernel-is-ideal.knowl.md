+++
id = "algebra-rings/kernel-is-ideal"
title = "Kernel is an ideal"
kind = "knowl"
summary = "The kernel of a ring homomorphism is a two-sided ideal of the domain."
aliases = ["kernel-is-ideal", "Kernel is an ideal"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/kernel-is-ideal.md"
+++

**Kernel is an ideal**: Let $\varphi:R\to S$ be a ring homomorphism. Then
\[
\ker(\varphi)=\{r\in R:\varphi(r)=0_S\}
\]
is a two-sided ideal of $R$.

For a [[algebra-rings/ring-homomorphism|ring homomorphism]] $\varphi$, the [[algebra-rings/kernel-ring|kernel]] is therefore an [[algebra-rings/ideal|ideal]] (indeed a [[algebra-rings/two-sided-ideal|two-sided ideal]] in general), so one can form the [[algebra-rings/quotient-ring|quotient ring]] $R/\ker\varphi$. This is the key input for [[algebra-rings/first-isomorphism-theorem-rings|the First Isomorphism Theorem for rings]].
