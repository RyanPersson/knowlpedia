+++
id = "real-analysis/taylor-polynomial"
title = "Taylor polynomial"
kind = "knowl"
summary = "The polynomial built from derivatives of a function at a point."
aliases = ["taylor-polynomial", "Taylor polynomial"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/taylor-polynomial.md"
+++

A **Taylor polynomial** of order $n$ for a function $f$ at a point $a$ is the polynomial
$T_n f(x)=\sum_{j=0}^n \frac{f^{(j)}(a)}{j!}(x-a)^j$, assuming the needed [[real-analysis/higher-derivatives|higher derivatives]] exist at $a$.

Taylor polynomials package derivative data at a point into a single [[real-analysis/polynomial|polynomial]] that locally approximates $f$. The approximation is quantified by [[real-analysis/taylors-theorem-with-remainder|Taylor's theorem with remainder]].

**Examples:**
- For $f(x)=e^x$ at $a=0$, $T_n f(x)=\sum_{j=0}^n \frac{x^j}{j!}$.
- For $f(x)=\sin x$ at $a=0$, $T_{2n+1} f(x)=\sum_{j=0}^n (-1)^j \frac{x^{2j+1}}{(2j+1)!}$.
