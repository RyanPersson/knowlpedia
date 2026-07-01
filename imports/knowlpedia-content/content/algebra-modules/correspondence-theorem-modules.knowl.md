+++
id = "algebra-modules/correspondence-theorem-modules"
title = "Correspondence theorem for modules"
kind = "knowl"
summary = "Submodules of M containing N correspond to submodules of M/N."
aliases = ["correspondence-theorem-modules", "Correspondence theorem for modules"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/correspondence-theorem-modules.md"
+++

**Correspondence theorem (modules)**: Let \(M\) be an \(R\)-module and \(N\subseteq M\) a submodule. Let \(\pi\colon M\to M/N\) be the quotient map. Then the assignments
- \(L \mapsto L/N\) (for submodules \(L\subseteq M\) with \(N\subseteq L\)),
- \(K \mapsto \pi^{-1}(K)\) (for submodules \(K\subseteq M/N\)),
define inverse, inclusion-preserving bijections between the set of [[algebra-modules/submodule|submodules]] of \(M\) containing \(N\) and the set of submodules of the [[algebra-modules/quotient-module|quotient module]] \(M/N\). The inverse image operation uses the notion of [[shared-foundations/preimage|preimage]] under \(\pi\).

Under this correspondence, lattice operations are respected (e.g. intersections and sums correspond), and many structural statements about submodules “above \(N\)” translate into statements about submodules of \(M/N\).
