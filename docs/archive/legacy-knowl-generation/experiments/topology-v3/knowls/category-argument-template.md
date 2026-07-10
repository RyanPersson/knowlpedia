---
title: "Category argument template"
description: "A common proof pattern in Baire category theory using dense open sets and meager sets."
---

A **category argument** is a proof strategy in a {{{< knowl id="baire-space" text="Baire space" >}}} that proves existence or “genericity” of points with a desired property by showing the set of exceptions is {{{< knowl id="meager-set" text="meager" >}}}, or equivalently by exhibiting the set of good points as (or containing) a countable intersection of {{{< knowl id="open-set" section="topology-core" text="open" >}}} {{{< knowl id="dense-set" section="topology-core" text="dense" >}}} sets.

The underlying engine is the defining property of Baire spaces, often supplied in practice by the {{{< knowl id="baire-category-theorem" text="Baire category theorem" >}}} (for example, in complete metric spaces). The typical conclusion is that the good set is {{{< knowl id="residual-set" text="residual" >}}}, hence dense.

Template:
1. Work in a Baire space $X$ and define “good” sets $U_n\subseteq X$ encoding increasingly many requirements.
2. Prove each $U_n$ is open and dense (often using {{{< knowl id="intersection-of-dense-open-is-dense" text="finite stability of dense open sets" >}}} along the way).
3. Conclude $\bigcap_{n\in\mathbb{N}} U_n$ is dense (in particular nonempty), and pick $x$ in that intersection.
4. Unpack the definitions to see that $x$ satisfies the desired property.
