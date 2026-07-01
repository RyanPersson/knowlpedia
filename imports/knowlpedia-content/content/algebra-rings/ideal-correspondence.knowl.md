+++
id = "algebra-rings/ideal-correspondence"
title = "Ideal correspondence for quotients"
kind = "knowl"
summary = "Ideals of R containing I are in bijection with ideals of the quotient ring R/I."
aliases = ["ideal-correspondence", "Ideal correspondence for quotients"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ideal-correspondence.md"
+++

**Ideal correspondence for quotients**: Let $R$ be a ring and let $I\lhd R$ be a two-sided ideal, with quotient map $\pi:R\to R/I$. The assignment
\[
J\longmapsto J/I
\]
is a bijection between two-sided ideals $J\lhd R$ with $I\subseteq J$ and two-sided ideals of $R/I$, with inverse $K\mapsto \pi^{-1}(K)$. This correspondence preserves inclusion and carries sums and intersections to sums and intersections.

This is the ring form of the [[algebra-rings/correspondence-theorem-rings|Correspondence Theorem]] applied to the canonical [[algebra-rings/ring-epimorphism|epimorphism]] $\pi$, and it explains how [[algebra-rings/ideal|ideals]] in a [[algebra-rings/quotient-ring|quotient ring]] lift and descend. In particular, [[algebra-rings/prime-ideal|prime ideals]] and [[algebra-rings/maximal-ideal|maximal ideals]] of $R/I$ correspond to those of $R$ that contain $I$ (in the commutative setting).
