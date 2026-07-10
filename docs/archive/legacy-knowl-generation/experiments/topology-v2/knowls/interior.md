---
title: "Interior"
description: "Largest open subset contained in a given set."
---

The **interior** of a subset $A\subseteq X$ in a {{< knowl id="topological-space" text="topological space" >}} $(X,\tau)$ is
\[
\operatorname{int}(A)=\bigcup\{\,U\in\tau : U\subseteq A\,\}.
\]

That is, $\operatorname{int}(A)$ is the {{< knowl id="union" section="shared-foundations" text="union" >}} of all {{< knowl id="open-set" text="open sets" >}} contained in $A$, hence it is itself open.

**Examples:**
- In $\mathbb{R}$, $\operatorname{int}([0,1])=(0,1)$.
- In $\mathbb{R}$, $\operatorname{int}(\mathbb{Q})=\varnothing$.
- If $U$ is open, then $\operatorname{int}(U)=U$.
