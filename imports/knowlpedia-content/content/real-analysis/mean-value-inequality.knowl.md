+++
id = "real-analysis/mean-value-inequality"
title = "Mean value inequality"
kind = "knowl"
summary = "A bound on the change of a differentiable map using a bound on its derivative."
aliases = ["mean-value-inequality", "Mean value inequality"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mean-value-inequality.md"
+++

**Mean value inequality:** Let $U\subseteq\mathbb R^k$ be an [[topology/open-set|open set]], let $f:U\to\mathbb R^m$ be continuously differentiable, and let $x,y\in U$ be such that the line segment $\{(1-t)x+ty:0\le t\le 1\}$ is contained in $U$. If there is $M\ge 0$ with
$$
\|Df(z)\|\le M \quad \text{for all } z \text{ on the segment from } x \text{ to } y,
$$

where $\|Df(z)\|$ is the [[linear-algebra/operator-norm|operator norm]] of the derivative, then
$$
\|f(y)-f(x)\|\le M\|y-x\|.
$$

For $k=m=1$ this recovers the familiar estimate $|f(y)-f(x)|\le \sup |f'|\cdot |y-x|$ derived from the [[real-analysis/mean-value-theorem|mean value theorem]].
