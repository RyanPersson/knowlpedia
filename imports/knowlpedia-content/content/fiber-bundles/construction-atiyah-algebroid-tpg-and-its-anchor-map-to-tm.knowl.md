+++
id = "fiber-bundles/construction-atiyah-algebroid-tpg-and-its-anchor-map-to-tm"
title = "Atiyah algebroid TP/G and its anchor"
kind = "knowl"
summary = "Construction of the quotient bundle TP/G as a Lie algebroid over M with anchor induced by the projection to TM."
aliases = ["construction-atiyah-algebroid-tpg-and-its-anchor-map-to-tm", "Atiyah algebroid TP/G and its anchor"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-atiyah-algebroid-tpg-and-its-anchor-map-to-tm.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $G$. The right action of $G$ on $P$ differentiates to a right action on the [[fiber-bundles/tangent-bundle|tangent bundle]] $TP$ by $dR_g:TP\to TP$.

**Construction (Atiyah algebroid).** Form the quotient
\[
\mathrm{At}(P) := TP/G,
\]
the bundle whose fiber over $x\in M$ is the set of $G$-orbits in $T_pP$ for any $p\in P_x$. This is a smooth vector bundle over $M$.

**Anchor map.** The differential $d\pi:TP\to TM$ is $G$-invariant (since $\pi\circ R_g=\pi$), hence it descends to a vector bundle map
\[
a:\mathrm{At}(P)\to TM,\qquad a([v_p]) := d\pi_p(v_p),
\]
called the anchor.

**Lie algebroid structure.** Sections of $\mathrm{At}(P)$ identify with $G$-invariant vector fields on $P$. The usual [[fiber-bundles/lie-bracket|Lie bracket]] of $G$-invariant vector fields is again $G$-invariant, so it defines a bracket on sections of $\mathrm{At}(P)$, making $\mathrm{At}(P)$ a Lie algebroid with anchor $a$.

There is a natural short exact sequence of vector bundles
\[
0\to \mathrm{ad}(P)\to \mathrm{At}(P)\xrightarrow{a} TM\to 0,
\]
where $\mathrm{ad}(P)$ embeds as the quotient of vertical tangent vectors (fundamental fields). A principal connection is equivalently a splitting of this sequence.

## Examples
1. If $P$ is trivial, $P\cong M\times G$, then $\mathrm{At}(P)\cong TM\oplus (M\times \mathfrak g)$, and the anchor is projection onto $TM$.
2. For an abelian group, the bracket on the $\mathfrak g$-summand is zero, and $\mathrm{At}(P)$ is (locally) a semidirect product Lie algebroid determined only by how vertical and horizontal parts interact.
3. A choice of principal connection identifies $\mathrm{At}(P)$ with $TM\oplus \mathrm{ad}(P)$ by sending a class $[v_p]$ to its base component and its vertical component measured by the connection form.
