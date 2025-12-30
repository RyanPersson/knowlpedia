---
title: "Krull–Schmidt–Azumaya theorem"
description: "Finite-length modules decompose uniquely (up to permutation) into indecomposable summands."
---

**Krull–Schmidt–Azumaya theorem**: Let \(M\) be an \(R\)-module that has finite {{< knowl id="length-module" text="length" >}} (equivalently, \(M\) admits a {{< knowl id="composition-series-module" text="composition series" >}}). Then:
1. \(M\) decomposes as a finite {{< knowl id="direct-sum-modules" text="direct sum" >}} of indecomposable submodules.
2. Any two decompositions of \(M\) into finite direct sums of indecomposable modules are equivalent up to permutation and isomorphism of summands: if \(M\cong \bigoplus_{i=1}^n M_i \cong \bigoplus_{j=1}^m N_j\) with all \(M_i,N_j\) indecomposable, then \(n=m\) and after reindexing \(M_i\cong N_i\) for all \(i\).

A common sufficient hypothesis for Krull–Schmidt is that \(M\) is both {{< knowl id="artinian-module" text="Artinian" >}} and {{< knowl id="noetherian-module" text="Noetherian" >}} (which implies finite length). The theorem underlies the uniqueness of indecomposable decompositions and contrasts with the stronger behavior of {{< knowl id="semisimple-module" text="semisimple modules" >}} where summands can be taken simple.

**Proof sketch** *(optional)*: Existence follows from descending chain conditions on direct summands, splitting off indecomposables inductively. Uniqueness uses that endomorphism rings of indecomposable finite-length modules are local, enabling a cancellation argument that matches summands between two decompositions.
