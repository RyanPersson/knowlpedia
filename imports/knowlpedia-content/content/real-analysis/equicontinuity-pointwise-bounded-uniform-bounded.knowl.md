+++
id = "real-analysis/equicontinuity-pointwise-bounded-uniform-bounded"
title = "Equicontinuity + pointwise boundedness implies uniform boundedness on compact sets"
kind = "knowl"
summary = "On a compact domain, equicontinuity upgrades pointwise bounds to a global bound"
aliases = ["equicontinuity-pointwise-bounded-uniform-bounded", "Equicontinuity + pointwise boundedness implies uniform boundedness on compact sets"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/equicontinuity-pointwise-bounded-uniform-bounded.md"
+++

Let $(K,d)$ be a [[topology/compact-set|compact]] [[topology/metric-space|metric space]] and let $\mathcal{F}\subseteq C(K,\mathbb{R})$ be a family of [[topology/continuous-map|continuous functions]]. Assume:
- $\mathcal{F}$ is [[real-analysis/equicontinuous-family|equicontinuous]] on $K$, and
- $\mathcal{F}$ is [[real-analysis/pointwise-bounded-family|pointwise bounded]] on $K$ (for each $x\in K$, $\sup_{f\in\mathcal{F}}|f(x)|<\infty$).

**Lemma**: Then $\mathcal{F}$ is [[real-analysis/uniformly-bounded-family|uniformly bounded]] on $K$; i.e., there exists $M<\infty$ such that
$
|f(x)|\le M\quad \text{for all } f\in\mathcal{F},\ x\in K.
$

This lemma is a standard step in the proof of the [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli theorem]].
