+++
id = "algebra-rings/radical-of-ideal"
title = "Radical of an ideal"
kind = "knowl"
summary = "The set of elements whose some power lies in a given ideal."
aliases = ["radical-of-ideal", "Radical of an ideal"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/radical-of-ideal.md"
+++

Let $R$ be a commutative ring and let $I\subseteq R$ be an ideal. The **radical of $I$** is
\[
\sqrt{I}=\{\,r\in R:\exists n\ge 1\text{ with }r^n\in I\,\}.
\]
Then $\sqrt{I}$ is an [[algebra-rings/ideal|ideal]] containing $I$.

The radical measures “nilpotence modulo $I$”: $r\in \sqrt{I}$ iff the image of $r$ in $R/I$ is [[algebra-rings/nilpotent-element|nilpotent]]. The [[algebra-rings/nilradical|nilradical]] is the special case $\sqrt{(0)}$, and one has $\sqrt{I}=\bigcap_{\mathfrak p\supseteq I}\mathfrak p$ as an [[algebra-rings/intersection-of-ideals|intersection]] over all [[algebra-rings/prime-ideal|prime ideals]] containing $I$.

**Examples:**
- In $\mathbb{Z}$, $\sqrt{(12)}=(6)$ since an integer has a power divisible by $12$ iff it is divisible by $2$ and $3$.
- In $k[x]$, $\sqrt{(x^2)}=(x)$.
- In $k[x,y]$, $\sqrt{(xy)}=(x)\cap (y)$.
