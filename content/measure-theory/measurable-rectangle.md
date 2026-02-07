---
title: "Measurable rectangle"
description: "A product set whose factors are measurable in their respective spaces."
---

A **measurable rectangle** in the {{< knowl id="cartesian-product" section="shared-foundations" text="Cartesian product" >}} $X\times Y$ of measurable spaces $(X,\Sigma)$ and $(Y,\mathcal T)$ is a set of the form $A\times B$, where $A\in\Sigma$ and $B\in\mathcal T$ are {{< knowl id="measurable-set" text="measurable sets" >}}.

Measurable rectangles are the basic “generators” used to build the product sigma-algebra on $X\times Y$, and they are central in product-measure constructions and Fubini/Tonelli-type results.

**Examples:**
- In $\mathbb R^2$ with the Borel sigma-algebra, a set such as $[a,b]\times(c,d)$ is a measurable rectangle, where $[a,b]$ and $(c,d)$ are {{< knowl id="interval" section="real-analysis" text="intervals" >}}.
- If $A$ is measurable in $(X,\Sigma)$, then $A\times Y$ is a measurable rectangle in $X\times Y$ (taking $B=Y$).
- If $B$ is measurable in $(Y,\mathcal T)$, then $X\times B$ is a measurable rectangle in $X\times Y$ (taking $A=X$).
