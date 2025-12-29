---
title: "Dense set"
description: "A subset whose closure is the whole space (equivalently, it meets every nonempty open set)"
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $D\subseteq X$.

The set $D$ is **dense in $X$** if its **{{< knowl id="closure" text="closure" >}}** equals $X$:
$
\overline{D}=X,
$
where $\overline{D}$ is the intersection of all {{< knowl id="closed-set" text="closed" >}} subsets of $X$ that contain $D$.

Equivalently, $D$ is dense in $X$ if and only if any (hence all) of the following hold:
- For every $x\in X$ and every $\varepsilon>0$, the {{< knowl id="open-ball" text="open ball" >}} $B(x,\varepsilon)=\{y\in X:d(x,y)<\varepsilon\}$ intersects $D$:
  $
  B(x,\varepsilon)\cap D\neq\varnothing.
  $
- Every nonempty {{< knowl id="open-set" text="open set" >}} $U\subseteq X$ intersects $D$:
  $
  U\neq\varnothing,\ U\text{ open}\ \Rightarrow\ U\cap D\neq\varnothing.
  $

Dense sets are "topologically large" in the sense that they cannot be avoided by any nontrivial open neighborhood structure.

**Examples:**
- $\mathbb{Q}$ is dense in $\mathbb{R}$ (usual metric): every interval contains a rational number.
- $\mathbb{R}\setminus\mathbb{Q}$ is dense in $\mathbb{R}$: every interval contains an irrational number.
- $\mathbb{Q}^k$ is dense in $\mathbb{R}^k$.
- $\mathbb{Z}$ is **not** dense in $\mathbb{R}$ (e.g. $(0,\tfrac12)$ contains no integers).
