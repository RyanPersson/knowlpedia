---
title: "Equicontinuity"
description: "A uniform form of continuity shared by all functions in a family."
---

A family $\mathcal{F}$ of functions from a {{< knowl id="metric-space" section="topology" text="metric space" >}} $(X,d_X)$ to a {{< knowl id="metric-space" section="topology" text="metric space" >}} $(Y,d_Y)$ is **equicontinuous at a point** $x_0\in X$ if for every $\varepsilon>0$ there exists $\delta>0$ such that for every $f\in\mathcal{F}$ and every $x\in X$,
\[
d_X(x,x_0)<\delta \implies d_Y\bigl(f(x),f(x_0)\bigr)<\varepsilon.
\]

Equicontinuity strengthens the statement that each $f\in\mathcal{F}$ is a {{< knowl id="continuous-map" section="topology" text="continuous map" >}}: here the same $\delta$ must work simultaneously for all functions in the family. A family that is equicontinuous at every point is an {{< knowl id="equicontinuous-family" text="equicontinuous family" >}}.

**Examples:**
- The family $\{f_a\}_{a\in\mathbb{R}}$ with $f_a(x)=\sin(x+a)$ is equicontinuous on $\mathbb{R}$ because $|\sin(x+a)-\sin(y+a)|\le |x-y|$ for all $a$.
- The family $f_n(x)=\sin(nx)$ on $[0,2\pi]$ is not equicontinuous at any point (rapid oscillations prevent a single $\delta$ from working for all $n$).
