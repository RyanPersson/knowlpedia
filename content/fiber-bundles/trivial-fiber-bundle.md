---
title: "Trivial fiber bundle"
description: "A fiber bundle globally isomorphic to a product M times F over the base."
---

A {{< knowl id="smooth-fiber-bundle" text="smooth fiber bundle" >}} \(\pi:E\to M\) with typical fiber \(F\) is **trivial** (or **globally trivial**) if there exists a {{< knowl id="bundle-isomorphism" text="bundle isomorphism" >}}
\[
\Psi:E\longrightarrow M\times F
\]
covering \(\mathrm{id}_M\), i.e. \(\mathrm{pr}_1\circ \Psi=\pi\). Equivalently, \(E\) admits a single global trivialization, so that all transition functions can be chosen to be the identity.

Triviality is a global property: every fiber bundle is locally a product by definition, but global triviality can fail because the local product charts may glue nontrivially.

## Examples
1. **Product bundles:** \(\mathrm{pr}_1:M\times F\to M\) is trivial by construction.
2. **Euclidean tangent bundle:** \(T\mathbb{R}^n\to\mathbb{R}^n\) is trivial via the standard identification \(T\mathbb{R}^n\cong \mathbb{R}^n\times\mathbb{R}^n\).
3. **Nontrivial example:** the Möbius line bundle over \(S^1\) is a smooth fiber bundle with typical fiber \(\mathbb{R}\) but is not trivial.
