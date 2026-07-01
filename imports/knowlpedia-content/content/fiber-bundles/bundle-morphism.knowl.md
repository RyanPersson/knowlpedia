+++
id = "fiber-bundles/bundle-morphism"
title = "Bundle morphism"
kind = "knowl"
summary = "A map of fiber bundles compatible with the projections and covering a specified base map."
aliases = ["bundle-morphism", "Bundle morphism"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/bundle-morphism.md"
+++

Let \(\pi:E\to M\) and \(\pi':E'\to M'\) be [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundles]]. A **bundle morphism** from \(E\) to \(E'\) **covering** a map \(f:M\to M'\) is a [[fiber-bundles/smooth-map|smooth map]] \(\Phi:E\to E'\) such that
\[
\pi'\circ \Phi \;=\; f\circ \pi.
\]
Thus \(\Phi\) is a [[fiber-bundles/fiber-preserving-map|fiber-preserving map]] whose domain and codomain carry fiber-bundle structures.

Equivalently, for every point \(x\in M\) the map \(\Phi\) restricts to a smooth map of fibers
\[
\Phi_x:E_x\to E'_{f(x)},
\]
and this fiberwise map depends smoothly on \(x\) (a fact that can be made explicit using [[fiber-bundles/local-trivialization|local trivializations]]).

A bundle morphism is an isomorphism precisely when it is a bundle morphism whose total-space map is a diffeomorphism and whose base map is a diffeomorphism.

## Examples
1. **Maps between products:** a map \((x,u)\mapsto(f(x),g(x,u))\) from \(M\times F\) to \(M'\times F'\) is a bundle morphism covering \(f\).
2. **Differentials:** for any \(f:M\to N\), the differential \(df:TM\to TN\) is a bundle morphism covering \(f\) (and is fiberwise linear).
3. **Pullback projection:** for \(f:N\to M\) and a bundle \(E\to M\), the canonical map \(f^*E\to E\) from the [[fiber-bundles/pullback-bundle|pullback bundle]] is a bundle morphism covering \(f\).
