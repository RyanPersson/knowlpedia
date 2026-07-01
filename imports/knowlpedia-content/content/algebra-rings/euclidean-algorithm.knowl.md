+++
id = "algebra-rings/euclidean-algorithm"
title = "Euclidean algorithm yields gcd and Bézout identity"
kind = "knowl"
summary = "In a Euclidean domain, the Euclidean algorithm computes a gcd and expresses it as a linear combination."
aliases = ["euclidean-algorithm", "Euclidean algorithm yields gcd and Bézout identity"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/euclidean-algorithm.md"
+++

**Euclidean algorithm yields gcd and Bézout identity**: Let $R$ be a Euclidean domain and let $a,b\in R$ be not both zero. The Euclidean algorithm produces $d\in R$ and $x,y\in R$ such that $d=\gcd(a,b)$ and $d=ax+by$. Equivalently, $(a,b)=(d)$ as ideals.

In a [[algebra-rings/euclidean-domain|Euclidean domain]], the algorithm computes a [[algebra-rings/gcd|gcd]] and simultaneously shows that the ideal [[algebra-rings/ideal-generated|generated]] by $a$ and $b$ is a [[algebra-rings/principal-ideal|principal ideal]]. This is the core input for [[algebra-rings/euclidean-implies-pid|Euclidean implies PID]].
