+++
id = "real-analysis/higher-derivatives"
title = "Higher derivatives"
kind = "knowl"
summary = "Derivatives of order two and higher, defined iteratively."
aliases = ["higher-derivatives", "Higher derivatives"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/higher-derivatives.md"
+++

A **higher derivative** of a function $f$ is a derivative of order $n\ge 2$, defined recursively by $f^{(0)}=f$, $f^{(1)}=f'$, and $f^{(n)}=(f^{(n-1)})'$ wherever the [[real-analysis/derivative|derivative]] exists.

Higher derivatives quantify finer local behavior and are central in approximation results such as [[real-analysis/taylors-theorem-with-remainder|Taylor's theorem with remainder]]. They also determine smoothness classes such as [[real-analysis/class-ck-function|class C^k functions]].

**Examples:**
- For $f(x)=e^x$, one has $f^{(n)}(x)=e^x$ for every $n\ge 0$.
- For $f(x)=x^m$ (a polynomial), $f^{(n)}\equiv 0$ for all $n>m$.
