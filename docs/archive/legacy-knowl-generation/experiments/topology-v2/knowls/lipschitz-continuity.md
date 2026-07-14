---
title: "Lipschitz continuity"
description: "A strong continuity condition bounded by a global linear inequality"
---

A map $f:(X,d_X)\to(Y,d_Y)$ between {{< knowl id="metric-space" text="metric spaces" >}} is **Lipschitz continuous** if there exists $L\ge 0$ such that
\[
d_Y\bigl(f(x),f(y)\bigr)\le L\,d_X(x,y)\quad\text{for all }x,y\in X.
\]

Lipschitz continuity implies {{< knowl id="uniformly-continuous-map" text="uniform continuity" >}}, and it is the special case $\alpha=1$ of {{< knowl id="holder-continuity" text="Hölder continuity" >}}.

**Examples:**
- On $\mathbb{R}$, $f(x)=ax+b$ is Lipschitz with constant $|a|$.
- On $[0,1]$, the map $f(x)=x^2$ is Lipschitz (one can take constant $2$).
- On $[0,1]$, the map $f(x)=\sqrt{x}$ is not Lipschitz (but it is Hölder).
