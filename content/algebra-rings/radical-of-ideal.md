---
title: "Radical of an ideal"
description: "The set of elements whose some power lies in a given ideal."
---

Let $R$ be a commutative ring and let $I\subseteq R$ be an ideal. The **radical of $I$** is
\[
\sqrt{I}=\{\,r\in R:\exists n\ge 1\text{ with }r^n\in I\,\}.
\]
Then $\sqrt{I}$ is an {{< knowl id="ideal" text="ideal" >}} containing $I$.

The radical measures “nilpotence modulo $I$”: $r\in \sqrt{I}$ iff the image of $r$ in $R/I$ is {{< knowl id="nilpotent-element" text="nilpotent" >}}. The {{< knowl id="nilradical" text="nilradical" >}} is the special case $\sqrt{(0)}$, and one has $\sqrt{I}=\bigcap_{\mathfrak p\supseteq I}\mathfrak p$ as an {{< knowl id="intersection-of-ideals" text="intersection" >}} over all {{< knowl id="prime-ideal" text="prime ideals" >}} containing $I$.

**Examples:**
- In $\mathbb{Z}$, $\sqrt{(12)}=(6)$ since an integer has a power divisible by $12$ iff it is divisible by $2$ and $3$.
- In $k[x]$, $\sqrt{(x^2)}=(x)$.
- In $k[x,y]$, $\sqrt{(xy)}=(x)\cap (y)$.