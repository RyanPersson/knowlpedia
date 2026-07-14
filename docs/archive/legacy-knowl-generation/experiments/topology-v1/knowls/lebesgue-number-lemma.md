---
title: "Lebesgue number lemma"
description: "A compact metric space admits a uniform scale for any open cover"
---

**Lebesgue number lemma**: Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $X$ be {{< knowl id="compact-set" text="compact" >}}. For every {{< knowl id="open-cover" text="open cover" >}} $\mathcal{U}$ of $X$, there exists a number $\delta>0$ such that every subset $A\subseteq X$ with {{< knowl id="diameter" text="diameter" >}} $\operatorname{diam}(A)<\delta$ is contained in some $U\in\mathcal{U}$.

An equivalent and commonly used form: there exists $\delta>0$ such that for every $x\in X$, the {{< knowl id="open-ball" text="open ball" >}} $B(x,\delta)$ is contained in some member of the cover.

**Proof sketch**: For each $x\in X$, pick $U_x\in\mathcal{U}$ with $x\in U_x$ and choose $r_x>0$ with $B(x,r_x)\subseteq U_x$. The balls $B(x,r_x/2)$ form an open cover of $X$; extract a finite subcover $B(x_i,r_{x_i}/2)$. Let $\delta=\min_i r_{x_i}/2$. Then any set of diameter $<\delta$ fits inside some $U_{x_i}$.

**Examples:**
- On $[0,1]$, any open cover by intervals has a Lebesgue number.
- The lemma is a standard tool in proving that continuous maps from compact metric spaces are {{< knowl id="uniformly-continuous-map" text="uniformly continuous" >}}.
