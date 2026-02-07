---
title: "Dirichlet test"
description: "A convergence test for sums of products using bounded partial sums and monotone factors."
---

**Dirichlet test:** Consider a series $\sum_{n=1}^\infty a_n b_n$ of real or complex numbers. Let
\[
A_n=\sum_{k=1}^n a_k
\]
denote the {{< knowl id="partial-sums" text="partial sums" >}} of $\sum a_n$. If

1. the sequence $(A_n)$ is bounded, and
2. $(b_n)$ is monotone and $b_n\to 0$,

then $\sum_{n=1}^\infty a_n b_n$ {{< knowl id="convergent-series" text="converges" >}}.

The {{< knowl id="alternating-series-test" text="alternating series test" >}} is a special case (take $a_n=(-1)^{n-1}$), and Dirichlet’s test is closely paired with the {{< knowl id="abel-test" text="Abel test" >}}.
