+++
id = "measure-theory/measurable-rectangle"
title = "Measurable rectangle"
kind = "knowl"
summary = "A product set whose factors are measurable in their respective spaces."
aliases = ["measurable-rectangle", "Measurable rectangle"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/measurable-rectangle.md"
+++

A **measurable rectangle** in the [[shared-foundations/cartesian-product|Cartesian product]] $X\times Y$ of measurable spaces $(X,\Sigma)$ and $(Y,\mathcal T)$ is a set of the form $A\times B$, where $A\in\Sigma$ and $B\in\mathcal T$ are [[measure-theory/measurable-set|measurable sets]].

Measurable rectangles are the basic “generators” used to build the product sigma-algebra on $X\times Y$, and they are central in product-measure constructions and Fubini/Tonelli-type results.

**Examples:**
- In $\mathbb R^2$ with the Borel sigma-algebra, a set such as $[a,b]\times(c,d)$ is a measurable rectangle, where $[a,b]$ and $(c,d)$ are [[real-analysis/interval|intervals]].
- If $A$ is measurable in $(X,\Sigma)$, then $A\times Y$ is a measurable rectangle in $X\times Y$ (taking $B=Y$).
- If $B$ is measurable in $(Y,\mathcal T)$, then $X\times B$ is a measurable rectangle in $X\times Y$ (taking $A=X$).
