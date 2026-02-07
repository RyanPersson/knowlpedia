---
title: "Naturality of Chern–Weil classes under pullback"
description: "Chern–Weil forms and their de Rham classes commute with pullback of principal bundles."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with a {{< knowl id="principal-connection" text="principal connection" >}} $\omega$ and {{< knowl id="curvature" text="curvature" >}} $\Omega$. Let $f:N\to M$ be a {{< knowl id="smooth-map" text="smooth map" >}} and let $f^*P\to N$ be the pullback principal bundle, with pulled-back connection $f^*\omega$ and curvature $f^*\Omega$.

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
using the defining property of {{< knowl id="chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection" text="Chern–Weil forms" >}}.

## Examples
1. **Restriction to a submanifold.** If $i:S\hookrightarrow M$ is an embedded submanifold, then $i^*P\to S$ carries the restricted characteristic classes: $\operatorname{cw}_P(i^*\omega)=i^*\operatorname{cw}_P(\omega)$.
2. **Diffeomorphism invariance.** If $f$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}, then characteristic classes transform by pullback under $f$ and in particular are invariants of the bundle up to isomorphism over the diffeomorphic base.
3. **Constant map.** If $f:N\to M$ is constant, then $f^*P$ is a trivial bundle; the pulled-back characteristic classes are zero in positive degree, so $f^*([\operatorname{cw}_P(\omega)])=0$ for $k>0$.
