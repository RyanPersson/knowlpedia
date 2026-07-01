+++
id = "fiber-bundles/complex-vector-bundle"
title = "Complex vector bundle"
kind = "knowl"
summary = "A smooth vector bundle whose fibers are complex vector spaces and whose transition functions are complex linear."
aliases = ["complex-vector-bundle", "Complex vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/complex-vector-bundle.md"
+++

Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]]. A **(smooth) complex vector bundle** over $M$ is a smooth surjective map $\pi:E\to M$ together with the following data and properties:

1. For each $x\in M$, the fiber $E_x:=\pi^{-1}(x)$ is a finite-dimensional complex vector space.

2. There is an open cover $\{U_\alpha\}$ of $M$ and smooth maps (local trivializations)
   \[
   \Phi_\alpha:\pi^{-1}(U_\alpha)\to U_\alpha\times \mathbb C^r
   \]
   such that:
   - $\mathrm{pr}_1\circ \Phi_\alpha=\pi$ on $\pi^{-1}(U_\alpha)$, and
   - for each $x\in U_\alpha$, the induced map $(\Phi_\alpha)_x:E_x\to \{x\}\times\mathbb C^r\cong \mathbb C^r$ is complex linear.

Equivalently, on overlaps $U_\alpha\cap U_\beta$ the transition maps
\[
\Phi_\alpha\circ \Phi_\beta^{-1}:(U_\alpha\cap U_\beta)\times \mathbb C^r\to (U_\alpha\cap U_\beta)\times \mathbb C^r
\]
have the form $(x,v)\mapsto (x,g_{\alpha\beta}(x)v)$ for a smooth map $g_{\alpha\beta}:U_\alpha\cap U_\beta\to \mathrm{GL}(r,\mathbb C)$.

The integer $r$ is the (complex) rank; it is locally constant and hence constant if $M$ is connected (see [[fiber-bundles/rank-of-a-vector-bundle|rank of a vector bundle]]).

## Examples
1. **Trivial bundle.** For any $r\ge 1$, the projection $M\times\mathbb C^r\to M$ is a complex vector bundle with the obvious trivializations.

2. **Complexified tangent and cotangent bundles.** The bundles $TM\otimes_\mathbb R \mathbb C$ and $T^*M\otimes_\mathbb R \mathbb C$ are complex vector bundles obtained by complexifying the [[fiber-bundles/tangent-bundle|tangent bundle]] and [[fiber-bundles/cotangent-bundle|cotangent bundle]].

3. **Bundle of complex-valued $k$-forms.** The exterior power $\Lambda^k(T^*M\otimes\mathbb C)$ is a complex vector bundle whose smooth sections are complex-valued [[fiber-bundles/differential-k-form|differential k-forms]].
