+++
id = "algebra-rings/correspondence-theorem-rings"
title = "Correspondence theorem for rings"
kind = "knowl"
summary = "Ideals of a quotient ring correspond to ideals of the original ring containing the kernel."
aliases = ["correspondence-theorem-rings", "Correspondence theorem for rings"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/correspondence-theorem-rings.md"
+++

**Correspondence theorem (rings)**: Let \(R\) be a ring, let \(I\triangleleft R\) be an [[algebra-rings/ideal|ideal]], and let \(\pi:R\to R/I\) be the quotient map. Then the assignment
\[
J\ \longmapsto\ J/I
\]
is an inclusion-preserving bijection between ideals \(J\) of \(R\) with \(I\subseteq J\) and ideals of the [[algebra-rings/quotient-ring|quotient ring]] \(R/I\). The inverse bijection sends an ideal \(K\triangleleft R/I\) to the [[shared-foundations/preimage|preimage]] \(\pi^{-1}(K)\).

Under this correspondence, [[algebra-rings/prime-ideal|prime ideals]] (and likewise [[algebra-rings/maximal-ideal|maximal ideals]] in the commutative case) correspond to prime (respectively maximal) ideals containing \(I\).
