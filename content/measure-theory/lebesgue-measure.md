---
title: "Lebesgue measure"
description: "The standard complete translation-invariant measure on Euclidean space built from covering by rectangles."
---

A **Lebesgue measure** on $\mathbb{R}^n$ is the {{< knowl id="measure" text="measure" >}} $\lambda^n$ obtained by applying the {{< knowl id="caratheodory-construction" text="Carathéodory construction" >}} to the {{< knowl id="outer-measure" text="outer measure" >}} $\lambda^{n,*}$ defined by
$$
\lambda^{n,*}(E)
=\inf\left\{\sum_{k=1}^\infty \operatorname{vol}(R_k)\,:\, E\subseteq \bigcup_{k=1}^\infty R_k,\ \text{each } R_k \text{ is a measurable rectangle}\right\},
$$

where a {{< knowl id="measurable-rectangle" text="measurable rectangle" >}} is typically a half-open box $R=\prod_{i=1}^n (a_i,b_i]$ and
$$
\operatorname{vol}(R)=\prod_{i=1}^n (b_i-a_i).
$$

A set $E\subseteq \mathbb{R}^n$ is **Lebesgue measurable** if it is a {{< knowl id="caratheodory-measurable-set" text="Carathéodory measurable set" >}} for $\lambda^{n,*}$, and then $\lambda^n(E):=\lambda^{n,*}(E)$.

Lebesgue measure is the foundational example of a {{< knowl id="measure-space" text="measure space" >}} on Euclidean space and is the standard reference for notions like {{< knowl id="null-set" text="null set" >}} and {{< knowl id="almost-everywhere" text="almost everywhere" >}}.

**Examples:**
- On $\mathbb{R}$, $\lambda^1((a,b))=b-a$ for any open interval $(a,b)$.
- In $\mathbb{R}^n$, $\lambda^n\!\left(\prod_{i=1}^n (a_i,b_i]\right)=\prod_{i=1}^n (b_i-a_i)$ for any measurable rectangle.
- Any countable subset of $\mathbb{R}^n$ (for example, $\mathbb{Q}\cap[0,1]$) has Lebesgue measure $0$.
