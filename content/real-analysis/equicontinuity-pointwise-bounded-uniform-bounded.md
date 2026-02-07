---
title: "Equicontinuity + pointwise boundedness implies uniform boundedness on compact sets"
description: "On a compact domain, equicontinuity upgrades pointwise bounds to a global bound"
---

Let $(K,d)$ be a {{< knowl id="compact-set" section="topology" text="compact" >}} {{< knowl id="metric-space" section="topology" text="metric space" >}} and let $\mathcal{F}\subseteq C(K,\mathbb{R})$ be a family of {{< knowl id="continuous-map" section="topology" text="continuous functions" >}}. Assume:
- $\mathcal{F}$ is {{< knowl id="equicontinuous-family" text="equicontinuous" >}} on $K$, and
- $\mathcal{F}$ is {{< knowl id="pointwise-bounded-family" text="pointwise bounded" >}} on $K$ (for each $x\in K$, $\sup_{f\in\mathcal{F}}|f(x)|<\infty$).

**Lemma**: Then $\mathcal{F}$ is {{< knowl id="uniformly-bounded-family" text="uniformly bounded" >}} on $K$; i.e., there exists $M<\infty$ such that
$
|f(x)|\le M\quad \text{for all } f\in\mathcal{F},\ x\in K.
$

This lemma is a standard step in the proof of the {{< knowl id="arzela-ascoli-theorem" text="Arzelà–Ascoli theorem" >}}.
