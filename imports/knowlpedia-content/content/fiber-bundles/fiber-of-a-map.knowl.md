+++
id = "fiber-bundles/fiber-of-a-map"
title = "Fiber of a map"
kind = "knowl"
summary = "The subset of the domain mapping to a fixed point in the codomain, also called a preimage fiber."
aliases = ["fiber-of-a-map", "Fiber of a map"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/fiber-of-a-map.md"
+++

Let $f:X\to Y$ be a map of sets and let $y\in Y$. The **fiber of $f$ over $y$** (or **preimage fiber**) is the subset
\[
f^{-1}(y)=\{x\in X \mid f(x)=y\}\subset X.
\]

If $f:M\to N$ is a [[fiber-bundles/smooth-map|smooth map]] between [[fiber-bundles/smooth-manifold|smooth manifolds]], the fiber $f^{-1}(y)$ is still defined as a subset of $M$. Additional geometry arises when $y$ is a regular value in the sense of the [[fiber-bundles/differential-of-a-smooth-map|differential of a smooth map]]: in that case, $f^{-1}(y)$ is an embedded submanifold of $M$ of codimension $\dim N$.

Fibers are especially important when $f$ is a bundle projection; for instance, in a [[fiber-bundles/principal-g-bundle|principal G-bundle]] $\pi:P\to B$, each fiber $\pi^{-1}(b)$ is (noncanonically) diffeomorphic to the structure group $G$.

## Examples
1. **Projection of a product.** For $\pi:M\times F\to M$, the fiber over $m\in M$ is $\pi^{-1}(m)=\{m\}\times F$, canonically identified with $F$.
2. **Radius-squared map.** For $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=x^2+y^2$, the fiber over $r$ is empty if $r<0$, is a single point if $r=0$, and is a circle of radius $\sqrt r$ if $r>0$.
3. **Hopf fibration (geometric fiber).** The Hopf map $S^3\to S^2$ has fibers diffeomorphic to $S^1$; it is a principal $S^1$-bundle, so every fiber is an orbit of the $S^1$-action.
