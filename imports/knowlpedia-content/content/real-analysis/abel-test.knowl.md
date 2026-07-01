+++
id = "real-analysis/abel-test"
title = "Abel test"
kind = "knowl"
summary = "A convergence test for sums of products when one series converges and the other factor is monotone and bounded."
aliases = ["abel-test", "Abel test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/abel-test.md"
+++

**Abel test:** Consider a series $\sum_{n=1}^\infty a_n b_n$ of real or complex numbers. Suppose

1. the series $\sum_{n=1}^\infty a_n$ [[real-analysis/convergent-series|converges]], and
2. the sequence $(b_n)$ is monotone and bounded.

Then the series $\sum_{n=1}^\infty a_n b_n$ converges.

Abel’s test can be viewed as complementary to the [[real-analysis/dirichlet-test|Dirichlet test]]: Dirichlet assumes bounded [[real-analysis/partial-sums|partial sums]] of $(a_n)$ and $b_n\to 0$, while Abel assumes convergence of $\sum a_n$ and only boundedness of $(b_n)$.
