---
title: "Root test"
description: "A convergence test using the limsup of the nth roots of the term magnitudes."
---

**Root test:** For a {{< knowl id="series" text="series" >}} $\sum_{n=1}^\infty a_n$, define
\[
L=\limsup_{n\to\infty}\sqrt[n]{|a_n|},
\]
where $|a_n|$ denotes the {{< knowl id="absolute-value" text="absolute value" >}} of the term.

- If $L<1$, then $\sum_{n=1}^\infty a_n$ is {{< knowl id="absolutely-convergent-series" text="absolutely convergent" >}} (hence {{< knowl id="convergent-series" text="convergent" >}}).
- If $L>1$ (including $L=\infty$), then $\sum_{n=1}^\infty a_n$ is {{< knowl id="divergent-series" text="divergent" >}}.
- If $L=1$, the test is inconclusive.

The root test is especially natural for {{< knowl id="power-series" text="power series" >}} and is closely related to the {{< knowl id="cauchy-hadamard-theorem" text="Cauchy–Hadamard theorem" >}}; compare also the {{< knowl id="ratio-test" text="ratio test" >}}.
