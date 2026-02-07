---
title: "Atiyah sequence"
description: "The short exact sequence 0 to ad(P) to TP/G to TM to 0 associated to a principal bundle."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle with Lie algebra \(\mathfrak{g}\). Its {{< knowl id="atiyah-algebroid-of-a-principal-bundle" text="Atiyah algebroid" >}} is \(A(P)=TP/G\to M\), equipped with the anchor \(a:A(P)\to TM\) induced by \(d\pi\).

Define the **adjoint bundle** \(\mathrm{ad}(P)=P\times_{\mathrm{Ad}}\mathfrak{g}\to M\). There is a natural injection
\[
\iota:\mathrm{ad}(P)\hookrightarrow TP/G
\]
defined fiberwise by sending \([p,X]\in \mathrm{ad}(P)_x\) to the class of the fundamental vertical vector \(X^\#_p\in T_pP\). The anchor \(a\) is surjective, and its kernel is exactly the image of \(\iota\). Thus one obtains the **Atiyah sequence** of vector bundles over \(M\):
\[
0 \longrightarrow \mathrm{ad}(P) \xrightarrow{\ \iota\ } TP/G \xrightarrow{\ a\ } \, TM \longrightarrow 0.
\]

Exactness means:
- \(\iota\) is injective,
- \(a\circ \iota=0\),
- \(\ker(a)=\mathrm{im}(\iota)\),
- \(a\) is surjective.

## Examples
1. **Trivial bundle.** If \(P=M\times G\), then \(TP/G\cong TM\oplus (M\times\mathfrak{g})\), \(\mathrm{ad}(P)\cong M\times \mathfrak{g}\), and the sequence is
   \[
   0\to M\times\mathfrak{g}\to TM\oplus(M\times\mathfrak{g})\to TM\to 0,
   \]
   split by the obvious projection.

2. **Bundle over a point.** For \(P=G\to\{\ast\}\), the sequence becomes \(0\to \mathfrak{g}\xrightarrow{=}\mathfrak{g}\to 0\).

3. **Circle bundles.** For a principal \(U(1)\)-bundle, \(\mathrm{ad}(P)\cong M\times i\mathbb{R}\) is a trivial line bundle, and the sequence exhibits \(TP/U(1)\) as an extension of \(TM\) by this line.
