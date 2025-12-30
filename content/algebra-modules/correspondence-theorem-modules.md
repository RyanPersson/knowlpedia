---
title: "Correspondence theorem for modules"
description: "Submodules of M containing N correspond to submodules of M/N."
---

**Correspondence theorem (modules)**: Let \(M\) be an \(R\)-module and \(N\subseteq M\) a submodule. Let \(\pi\colon M\to M/N\) be the quotient map. Then the assignments
- \(L \mapsto L/N\) (for submodules \(L\subseteq M\) with \(N\subseteq L\)),
- \(K \mapsto \pi^{-1}(K)\) (for submodules \(K\subseteq M/N\)),
define inverse, inclusion-preserving bijections between the set of {{< knowl id="submodule" text="submodules" >}} of \(M\) containing \(N\) and the set of submodules of the {{< knowl id="quotient-module" text="quotient module" >}} \(M/N\). The inverse image operation uses the notion of {{< knowl id="preimage" section="shared-foundations" text="preimage" >}} under \(\pi\).

Under this correspondence, lattice operations are respected (e.g. intersections and sums correspond), and many structural statements about submodules “above \(N\)” translate into statements about submodules of \(M/N\).

**Proof sketch** *(optional)*: Check that \(\pi^{-1}(L/N)=L\) for \(N\subseteq L\), and that \(\pi(\pi^{-1}(K))=K\). Monotonicity and well-definedness follow from standard properties of quotient maps.
