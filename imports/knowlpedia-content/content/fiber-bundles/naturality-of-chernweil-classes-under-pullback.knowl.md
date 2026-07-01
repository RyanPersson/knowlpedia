+++
id = "fiber-bundles/naturality-of-chernweil-classes-under-pullback"
title = "Naturality of Chern–Weil classes under pullback"
kind = "knowl"
summary = "Chern–Weil forms and their de Rham classes commute with pullback of principal bundles."
aliases = ["naturality-of-chernweil-classes-under-pullback", "Naturality of Chern–Weil classes under pullback"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/naturality-of-chernweil-classes-under-pullback.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with a [[fiber-bundles/principal-connection|principal connection]] $\omega$ and [[fiber-bundles/curvature|curvature]] $\Omega$. Let $f:N\to M$ be a [[fiber-bundles/smooth-map|smooth map]] and let $f^*P\to N$ be the pullback principal bundle, with pulled-back connection $f^*\omega$ and curvature $f^*\Omega$.

Fix an Ad-invariant homogeneous polynomial $P$ on $\mathfrak g$ of degree $k$.

**Theorem (Naturality).** The Chern–Weil forms satisfy
\[
f^*\big(\operatorname{cw}_P(\omega)\big)=\operatorname{cw}_P(f^*\omega),
\]
and hence the cohomology classes satisfy
\[
f^*\big([\operatorname{cw}_P(\omega)]\big)=[\operatorname{cw}_P(f^*\omega)]\in H^{2k}_{\mathrm{dR}}(N).
\]
Equivalently, on total spaces,
\[
(f^*\pi)^*\operatorname{cw}_P(f^*\omega)=P(f^*\Omega)=f^*(P(\Omega))=f^*\big(\pi^*\operatorname{cw}_P(\omega)\big),
\]
using the defining property of [[fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection|Chern–Weil forms]].

## Examples
1. **Restriction to a submanifold.** If $i:S\hookrightarrow M$ is an embedded submanifold, then $i^*P\to S$ carries the restricted characteristic classes: $\operatorname{cw}_P(i^*\omega)=i^*\operatorname{cw}_P(\omega)$.
2. **Diffeomorphism invariance.** If $f$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]], then characteristic classes transform by pullback under $f$ and in particular are invariants of the bundle up to isomorphism over the diffeomorphic base.
3. **Constant map.** If $f:N\to M$ is constant, then $f^*P$ is a trivial bundle; the pulled-back characteristic classes are zero in positive degree, so $f^*([\operatorname{cw}_P(\omega)])=0$ for $k>0$.
