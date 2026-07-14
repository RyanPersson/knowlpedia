---
title: "Lebesgue number lemma auxiliary refinement"
description: "An open cover in a metric space can be refined by balls contained in the cover sets"
---

**Auxiliary refinement lemma**: Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $\mathcal{U}$ be an {{< knowl id="open-cover" text="open cover" >}} of $X$. For each $x\in X$, choose $U_x\in\mathcal{U}$ with $x\in U_x$. Since $U_x$ is open, there exists $r_x>0$ such that the {{< knowl id="open-ball" text="open ball" >}} $B(x,r_x)\subseteq U_x$.

Then the family $\mathcal{B}=\{B(x,r_x)\}_{x\in X}$ is an open cover of $X$ and is a {{< knowl id="refinement-of-an-open-cover" text="refinement" >}} of $\mathcal{U}$.

This refinement is the standard first step in proving the {{< knowl id="lebesgue-number-lemma" text="Lebesgue number lemma" >}}: compactness is then used to extract finitely many of the smaller balls and take a minimum radius.

**Examples:**
- In $\mathbb{R}$, if $\mathcal{U}$ is a cover by open intervals, each point $x$ lies in some interval $(a,b)$ and one can take $r_x=\min\{x-a,b-x\}$ so that $B(x,r_x)\subset(a,b)$.
- If $\mathcal{U}=\{X\}$, then one may take $r_x=1$ for all $x$ (any positive radius works).
