---
title: "Projective implies flat"
description: "Every projective module is flat, so tensoring with it preserves exact sequences."
---

**Projective implies flat**: Let $P$ be a projective right $R$-module. Then $P$ is flat: for every short exact sequence of left $R$-modules
\[
0\to A\to B\to C\to 0,
\]
the induced sequence
\[
0\to A\otimes_R P\to B\otimes_R P\to C\otimes_R P\to 0
\]
is exact.

A standard proof uses that {{< knowl id="projective-module" text="projective modules" >}} are direct summands of {{< knowl id="free-module" text="free modules" >}}, and that {{< knowl id="tensor-product" text="tensoring" >}} preserves exactness for free modules and respects direct summands, yielding {{< knowl id="flat-module" text="flatness" >}}.
