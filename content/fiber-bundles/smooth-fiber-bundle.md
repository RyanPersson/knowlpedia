---
title: "Smooth fiber bundle"
description: "A surjective submersion that is locally a product with a fixed model fiber."
---

Let \(M\), \(E\), and \(F\) be smooth manifolds. A map \(\pi:E\to M\) is a **smooth fiber bundle** with typical fiber \(F\) if:

1. \(\pi\) is a surjective submersion (so \((E,\pi,M)\) is a {{< knowl id="fibered-manifold" text="fibered manifold" >}}), and
2. for every \(x\in M\) there exists an open neighborhood \(U\ni x\) and a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}
   \[
   \Phi:\pi^{-1}(U)\longrightarrow U\times F
   \]
   such that \(\mathrm{pr}_1\circ \Phi=\pi|_{\pi^{-1}(U)}\).

Such a \(\Phi\) is a {{< knowl id="local-trivialization" text="local trivialization" >}} of the bundle over \(U\), and \(F\) is called the {{< knowl id="typical-fiber" text="typical fiber" >}} (model fiber). A family of compatible local trivializations covering \(M\) forms a {{< knowl id="bundle-atlas" text="bundle atlas" >}}, and on overlaps the change of trivialization is encoded by a {{< knowl id="transition-function" text="transition function" >}}.

## Examples
1. **Trivial bundle:** \(M\times F\to M\) with projection \(\mathrm{pr}_1\) is a smooth fiber bundle with typical fiber \(F\).
2. **Tangent bundle:** \(\tau:TM\to M\) is a smooth fiber bundle with typical fiber \(\mathbb{R}^{\dim M}\), using coordinate charts on \(M\) to build trivializations.
3. **Principal bundles:** every {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} \(P\to M\) is a smooth fiber bundle with typical fiber \(G\) (with additional group-action structure).
