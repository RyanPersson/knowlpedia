---
title: "Category argument template"
description: "A standard way to prove a property holds on a dense or residual set"
---

A **category argument template** is a standard proof strategy in a {{< knowl id="baire-space" text="Baire space" >}} $X$ to show that a “generic” point satisfies a property $P$ by proving that the set of points where $P$ holds is {{< knowl id="residual-set" text="residual" >}} (equivalently, that the exceptional set is {{< knowl id="meager-set" text="meager" >}}).

One typically proceeds in one of the following two ways.

1. **Build a large set as a countable intersection.**  
   For each $n$, define a set $U_n$ of points satisfying an $n$-th approximation to $P$. Prove that each $U_n$ is an {{< knowl id="open-set" text="open set" >}} and is {{< knowl id="dense-set" text="dense" >}}. Then apply {{< knowl id="intersection-of-dense-open-is-dense" text="intersection of dense open sets is dense" >}} to conclude that the {{< knowl id="countable-set" text="countable" >}} {{< knowl id="intersection" text="intersection" >}} $\bigcap_n U_n$ is dense (and hence residual), so points satisfying all approximations exist densely.

2. **Show the bad set is small as a countable union.**  
   Let $E$ be the set of points where $P$ fails. Write $E=\bigcup_n N_n$ as a countable {{< knowl id="union" text="union" >}} where each $N_n$ is {{< knowl id="nowhere-dense-set" text="nowhere dense" >}}. Then $E$ is meager, so its complement is residual, and $P$ holds on a residual (hence dense) set.

When $X$ is known to be a complete metric space, the needed Baire hypothesis is typically supplied by the {{< knowl id="baire-category-theorem" text="Baire category theorem" >}}.

**Examples:**
- In $\mathbb{R}$, to show that “most” points are irrational, note that $\mathbb{Q}$ is meager, so $\mathbb{R}\setminus\mathbb{Q}$ is residual.
- In many function spaces equipped with complete metrics, one proves existence of functions with infinitely many simultaneous “typical” properties by expressing each property as an open dense condition and intersecting them.
