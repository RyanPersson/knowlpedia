+++
id = "algebra-modules/quotient-module-universal-property"
title = "Universal property of quotient modules"
kind = "knowl"
summary = "A map that kills a submodule factors uniquely through the quotient."
aliases = ["quotient-module-universal-property", "Universal property of quotient modules"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/quotient-module-universal-property.md"
+++

**Universal property of quotient modules**: Let $M$ be an $R$-module, let $N\le M$ be a submodule, and let $\pi:M\to M/N$ be the quotient map. For any $R$-module $Q$ and any homomorphism $f:M\to Q$ such that $N\subseteq \ker(f)$, there exists a unique homomorphism $\bar f:M/N\to Q$ with $f=\bar f\circ \pi$.

This is the defining mapping property of the [[algebra-modules/quotient-module|quotient module]], and it expresses quotients as the universal way to force a [[algebra-modules/submodule|submodule]] to lie in the [[algebra-modules/kernel-module|kernel]] of a [[algebra-modules/module-homomorphism|module homomorphism]].
