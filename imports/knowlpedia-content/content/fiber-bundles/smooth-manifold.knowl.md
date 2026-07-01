+++
id = "fiber-bundles/smooth-manifold"
title = "Smooth manifold"
kind = "knowl"
summary = "A topological manifold equipped with a maximal smooth atlas, enabling calculus in local coordinates."
aliases = ["smooth-manifold", "Smooth manifold"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/smooth-manifold.md"
+++

Let $n\in\mathbb{N}$. An **$n$-dimensional smooth manifold** is a pair $(M,\mathcal A)$ such that

- $M$ is an $n$-dimensional topological manifold (Hausdorff, second countable, and every $p\in M$ has a neighborhood homeomorphic to an open subset of $\mathbb{R}^n$), and
- $\mathcal A$ is a **maximal** [[fiber-bundles/smooth-atlas|smooth atlas]] of [[fiber-bundles/smooth-chart-coordinate-chart|coordinate charts]] on $M$.

Maximal means: if $(U,\varphi)$ is a chart on $M$ whose transition maps with every chart in $\mathcal A$ are smooth, then $(U,\varphi)\in\mathcal A$. Any (not-necessarily-maximal) smooth atlas determines a unique maximal one by adjoining all charts smoothly compatible with it.

Once a smooth structure is fixed, one can define intrinsic objects such as the [[fiber-bundles/tangent-space-at-a-point|tangent space at a point]], the [[fiber-bundles/tangent-bundle|tangent bundle]], and differential forms with the [[fiber-bundles/exterior-derivative|exterior derivative]]. Maps between smooth manifolds are compared using charts; see [[fiber-bundles/smooth-map|smooth maps]].

## Examples
1. $\mathbb{R}^n$ with the single global chart $(\mathbb{R}^n,\mathrm{id})$ is a smooth manifold; its maximal atlas consists of all charts whose coordinate changes are smooth.
2. The sphere $S^n\subset\mathbb{R}^{n+1}$ becomes a smooth manifold using the two stereographic projection charts from the north and south poles; their overlap transition map is smooth, so they generate a maximal smooth atlas.
3. Any [[fiber-bundles/lie-group|Lie group]] is, by definition, a smooth manifold for which multiplication and inversion are [[fiber-bundles/smooth-map|smooth maps]].
