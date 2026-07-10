---
title: "Finite intersection property theorem"
description: "Compactness is equivalent to nonempty intersection for closed families with the finite intersection property"
---

**Finite intersection property theorem**: A topological space $X$ is {{< knowl id="compact-set" text="compact" >}} if and only if every family $\{F_\alpha\}_{\alpha\in A}$ of {{< knowl id="closed-set" text="closed sets" >}} with the following property has nonempty total intersection:

- (**Finite intersection property**) Every finite {{< knowl id="intersection" text="intersection" >}} $F_{\alpha_1}\cap\cdots\cap F_{\alpha_n}$ is nonempty.

Then
$$
\bigcap_{\alpha\in A} F_\alpha \ne \varnothing.
$$

**Proof sketch**: If $X$ is compact and the total intersection were empty, then the complements $X\setminus F_\alpha$ form an {{< knowl id="open-cover" text="open cover" >}} of $X$. A finite subcover would force a finite intersection of the $F_\alpha$ to be empty, contradicting the finite intersection property. Conversely, if the finite intersection property always implies nonempty total intersection, then any open cover with no finite subcover yields a closed family with the finite intersection property whose total intersection is empty, a contradiction.

**Examples:**
- In $[0,1]$, the closed sets $F_n=[0,1/n]$ have the finite intersection property and satisfy $\bigcap_n F_n=\{0\}$.
- In $\mathbb{R}$, the sets $F_n=[n,\infty)$ have the finite intersection property but empty total intersection, reflecting that $\mathbb{R}$ is not compact.
