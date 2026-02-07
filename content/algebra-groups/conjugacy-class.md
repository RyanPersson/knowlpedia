---
title: "Conjugacy class"
description: "The set of all conjugates of a given group element"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $g\in G$. The **conjugacy class of $g$ in $G$** is the subset
$
\mathrm{Cl}_G(g)=\{xgx^{-1} : x\in G\}.
$
Equivalently, $\mathrm{Cl}_G(g)$ is the set of all {{< knowl id="conjugate-element" text="conjugates" >}} of $g$.

Conjugacy classes are exactly the orbits of the {{< knowl id="conjugation-action" text="conjugation action" >}} of $G$ on itself, so they form a {{< knowl id="partition" section="shared-foundations" text="partition" >}} of $G$. An element lies in the {{< knowl id="center-of-group" text="center" >}} of $G$ if and only if its conjugacy class is a singleton. The sizes of conjugacy classes feature prominently in the {{< knowl id="class-equation" text="class equation" >}}.

**Examples:**
- In $S_3$, the conjugacy classes are $\{e\}$, the three transpositions $\{(12),(13),(23)\}$, and the two $3$-cycles $\{(123),(132)\}$.
- If $G$ is abelian, then $\mathrm{Cl}_G(g)=\{g\}$ for every $g\in G$.
- In $D_8=\langle r,s\mid r^4=s^2=e,\ srs=r^{-1}\rangle$, one has $\mathrm{Cl}_{D_8}(r)=\{r,r^{-1}\}=\{r,r^3\}$, so conjugacy classes need not be singletons in nonabelian groups.
