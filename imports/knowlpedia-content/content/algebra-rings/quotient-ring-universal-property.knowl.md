+++
id = "algebra-rings/quotient-ring-universal-property"
title = "Universal property of quotient rings"
kind = "knowl"
summary = "A homomorphism that kills an ideal factors uniquely through the quotient."
aliases = ["quotient-ring-universal-property", "Universal property of quotient rings"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/quotient-ring-universal-property.md"
+++

**Universal property of quotient rings**: Let \(R\) be a ring, let \(I\triangleleft R\) be an [[algebra-rings/ideal|ideal]], and let \(\pi:R\to R/I\) be the canonical projection onto the [[algebra-rings/quotient-ring|quotient ring]]. For any [[algebra-rings/ring-homomorphism|ring homomorphism]] \(f:R\to S\) such that \(I\subseteq \ker(f)\) (where \(\ker(f)\) is the [[algebra-rings/kernel-ring|kernel]]), there exists a unique ring homomorphism \(\bar f:R/I\to S\) with
\[
f=\bar f\circ \pi.
\]

This property characterizes \(R/I\) up to unique isomorphism and is the categorical mechanism behind “imposing relations” by quotienting.
