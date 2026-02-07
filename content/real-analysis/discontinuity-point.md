---
title: "Discontinuity point"
description: "A point where a function fails to be continuous"
---

A **discontinuity point** of a function $f:U\to \mathbb{R}^m$ at a point $a\in U$ is a point where $f$ is not {{< knowl id="continuous-map" section="topology" text="continuous" >}} at $a$; equivalently, $a$ is a discontinuity point if there exists $\varepsilon>0$ such that for every $\delta>0$ there is $x\in U$ with $\|x-a\|<\delta$ and $\|f(x)-f(a)\|\ge \varepsilon$.

In many common situations, discontinuity at $a$ can be detected by limits: if $\lim_{x\to a} f(x)$ exists (in the sense of {{< knowl id="limit-at-a-point" text="limit at a point" >}}) and is not equal to $f(a)$, then $a$ is a discontinuity point. The collection of all such points is the {{< knowl id="set-of-discontinuities" text="set of discontinuities" >}}.

**Examples:**
- The sign function defined by $f(x)=1$ for $x>0$, $f(x)=-1$ for $x<0$, and $f(0)=0$ is discontinuous at $0$.
- The function $f:\mathbb{R}\to\mathbb{R}$ defined by $f(x)=1$ for rational $x$ and $f(x)=0$ for irrational $x$ is discontinuous at every real number.
