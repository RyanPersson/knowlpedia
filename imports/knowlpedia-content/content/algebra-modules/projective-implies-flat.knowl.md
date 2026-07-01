+++
id = "algebra-modules/projective-implies-flat"
title = "Projective implies flat"
kind = "knowl"
summary = "Every projective module is flat, so tensoring with it preserves exact sequences."
aliases = ["projective-implies-flat", "Projective implies flat"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/projective-implies-flat.md"
+++

**Projective implies flat**: Let $P$ be a projective right $R$-module. Then $P$ is flat: for every short exact sequence of left $R$-modules
\[
0\to A\to B\to C\to 0,
\]
the induced sequence
\[
0\to A\otimes_R P\to B\otimes_R P\to C\otimes_R P\to 0
\]
is exact.

A standard proof uses that [[algebra-modules/projective-module|projective modules]] are direct summands of [[algebra-modules/free-module|free modules]], and that [[algebra-modules/tensor-product|tensoring]] preserves exactness for free modules and respects direct summands, yielding [[algebra-modules/flat-module|flatness]].
