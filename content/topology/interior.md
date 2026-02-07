---
title: "Interior"
description: "The largest open set contained in a given subset."
---

The **interior** of a subset $A\subseteq X$ in a {{< knowl id="topological-space" text="topological space" >}} $(X,\mathcal{T})$ is
\[
\operatorname{int}(A)=\bigcup\{U\in\mathcal{T}: U\subseteq A\}.
\]
Equivalently, $\operatorname{int}(A)$ is the largest {{< knowl id="open-set" text="open set" >}} contained in $A$.

A point $x$ lies in $\operatorname{int}(A)$ exactly when $A$ is a {{< knowl id="neighborhood" text="neighborhood" >}} of $x$. Interior is dual to {{< knowl id="closure" text="closure" >}} via complements: $\operatorname{int}(A)=X\setminus \overline{X\setminus A}$.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $\operatorname{int}([0,1])=(0,1)$.
- In $\mathbb{R}$ with the usual topology, $\operatorname{int}(\mathbb{Q})=\varnothing$.
- If $U$ is open, then $\operatorname{int}(U)=U$.
