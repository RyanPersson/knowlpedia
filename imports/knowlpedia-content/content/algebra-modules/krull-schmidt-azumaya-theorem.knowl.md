+++
id = "algebra-modules/krull-schmidt-azumaya-theorem"
title = "Krull–Schmidt–Azumaya theorem"
kind = "knowl"
summary = "Finite-length modules decompose uniquely (up to permutation) into indecomposable summands."
aliases = ["krull-schmidt-azumaya-theorem", "Krull–Schmidt–Azumaya theorem"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/krull-schmidt-azumaya-theorem.md"
+++

**Krull–Schmidt–Azumaya theorem**: Let \(M\) be an \(R\)-module that has finite [[algebra-modules/length-module|length]] (equivalently, \(M\) admits a [[algebra-modules/composition-series-module|composition series]]). Then:
1. \(M\) decomposes as a finite [[algebra-modules/direct-sum-modules|direct sum]] of indecomposable submodules.
2. Any two decompositions of \(M\) into finite direct sums of indecomposable modules are equivalent up to permutation and isomorphism of summands: if \(M\cong \bigoplus_{i=1}^n M_i \cong \bigoplus_{j=1}^m N_j\) with all \(M_i,N_j\) indecomposable, then \(n=m\) and after reindexing \(M_i\cong N_i\) for all \(i\).

A common sufficient hypothesis for Krull–Schmidt is that \(M\) is both [[algebra-modules/artinian-module|Artinian]] and [[algebra-modules/noetherian-module|Noetherian]] (which implies finite length). The theorem underlies the uniqueness of indecomposable decompositions and contrasts with the stronger behavior of [[algebra-modules/semisimple-module|semisimple modules]] where summands can be taken simple.
