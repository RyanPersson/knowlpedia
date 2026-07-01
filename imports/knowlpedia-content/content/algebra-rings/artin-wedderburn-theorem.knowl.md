+++
id = "algebra-rings/artin-wedderburn-theorem"
title = "Artin–Wedderburn theorem"
kind = "knowl"
summary = "Semisimple Artinian rings are exactly finite products of matrix rings over division rings."
aliases = ["artin-wedderburn-theorem", "Artin–Wedderburn theorem"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/artin-wedderburn-theorem.md"
+++

**Artin–Wedderburn theorem**: A ring \(R\) is [[algebra-rings/artinian-semisimple-ring|semisimple Artinian]] if and only if there exist positive integers \(n_1,\dots,n_t\) and [[algebra-rings/division-ring|division rings]] \(D_1,\dots,D_t\) such that
\[
R \ \cong\ \prod_{i=1}^t M_{n_i}(D_i),
\]
where \(M_{n_i}(D_i)\) is the [[algebra-rings/matrix-ring|matrix ring]] of size \(n_i\) over \(D_i\). In particular, \(R\) is [[algebra-rings/simple-ring|simple]] Artinian if and only if \(R\cong M_n(D)\) for some division ring \(D\).

This is the structural classification underpinning [[algebra-rings/semisimple-ring|semisimple rings]] and explains why representation-theoretic decompositions are controlled by matrix blocks.
