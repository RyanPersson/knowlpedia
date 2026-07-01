+++
id = "real-analysis/taylors-theorem-with-remainder"
title = "Taylor's theorem with remainder"
kind = "knowl"
summary = "Taylor expansion with an explicit remainder term for a smooth real function."
aliases = ["taylors-theorem-with-remainder", "Taylor's theorem with remainder"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/taylors-theorem-with-remainder.md"
+++

**Taylor's theorem with remainder:** Let $I\subseteq\mathbb R$ be an [[real-analysis/interval|interval]], let $a\in I$, and let $f:I\to\mathbb R$ have continuous [[real-analysis/higher-derivatives|derivatives up to order]] $n+1$ on $I$. For each $x\in I$ there exists a point $\xi$ between $a$ and $x$ such that
$$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}.
$$

The polynomial part is the [[real-analysis/taylor-polynomial|Taylor polynomial]] of degree $n$ at $a$, and the final term is the Lagrange-form remainder, which provides effective error bounds when $f^{(n+1)}$ is bounded.
