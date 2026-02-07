---
title: "Uniform continuity"
description: "Continuity where a single delta works for the whole set, not point by point."
---
Let \(f:(X,d_X)\to(Y,d_Y)\) and \(A\subseteq X\). The function \(f\) is **uniformly continuous on \(A\)** if
\[
\forall \varepsilon>0\ \exists \delta>0\ \text{such that}\ \forall x,y\in A,\ d_X(x,y)<\delta \Rightarrow d_Y(f(x),f(y))<\varepsilon.
\]
Compared to {{< knowl id="continuity-on-a-set" section="real-analysis" text="ordinary continuity on \(A\)" >}}, the key point is that \(\delta\) depends only on \(\varepsilon\), not on the location in \(A\).

Useful properties:
- Uniformly continuous functions send Cauchy sequences to Cauchy sequences; this links naturally with {{< knowl id="complete-metric-space" section="topology" text="completeness" >}}.
- If \(f\) is continuous on a {{< knowl id="compact-set" section="topology" text="compact set" >}} \(K\), then \(f\) is uniformly continuous on \(K\) (Heine–Cantor).
- Every Lipschitz function (i.e., \(d_Y(f(x),f(y))\le L\,d_X(x,y)\)) is uniformly continuous.

Examples in \(\mathbb{R}\):
- \(f(x)=x^2\) is not uniformly continuous on \(\mathbb{R}\), but it is uniformly continuous on \([0,1]\).
- \(f(x)=1/x\) is continuous on \((0,1)\) but not uniformly continuous there.

14m45s · gpt-5.2-pro[browser] · ↑547 ↓3.41k ↻0 Δ3.95k
