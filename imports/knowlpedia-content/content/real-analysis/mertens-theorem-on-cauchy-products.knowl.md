+++
id = "real-analysis/mertens-theorem-on-cauchy-products"
title = "Mertens theorem on Cauchy products"
kind = "knowl"
summary = "Convergence of the Cauchy product under absolute convergence of one factor"
aliases = ["mertens-theorem-on-cauchy-products", "Mertens theorem on Cauchy products"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mertens-theorem-on-cauchy-products.md"
+++

**Mertens theorem (Cauchy products)**: Let $\sum_{n=0}^\infty a_n$ and $\sum_{n=0}^\infty b_n$ be [[real-analysis/convergent-series|convergent]] [[real-analysis/series|series]] (real or complex). Define the [[real-analysis/cauchy-product|Cauchy product]] coefficients
$c_n=\sum_{k=0}^n a_k b_{n-k}.$
If at least one of the series $\sum a_n$ or $\sum b_n$ [[real-analysis/absolutely-convergent-series|converges absolutely]], then the Cauchy product series $\sum c_n$ converges and
$\sum_{n=0}^\infty c_n = \left(\sum_{n=0}^\infty a_n\right)\left(\sum_{n=0}^\infty b_n\right).$

This result justifies multiplying power series and many other formal series manipulations when absolute convergence is present.
