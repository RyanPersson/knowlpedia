---
title: "Equivalent descriptions of a principal connection"
description: "A principal connection can be specified by a horizontal distribution, a splitting of the tangent sequence, or a connection one-form."
---

Let \(\pi:P\to M\) be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group \(G\). Write \(V\!P=\ker(d\pi)\subset TP\) for the vertical subbundle, and note that \(d\pi:TP\to \pi^*TM\) relates \(TP\) to the pullback of the {{< knowl id="tangent-bundle" text="tangent bundle" >}} of \(M\).

## Theorem (TFAE: principal connection data)
The following are equivalent:

1. **Principal connection.** A {{< knowl id="principal-connection" text="principal connection" >}} on \(P\).
2. **Horizontal distribution.** A smooth subbundle \(H\subset TP\) such that:
   - \(TP = H \oplus V\!P\) (direct sum),
   - \(H\) is \(G\)-equivariant: \((dR_g)_p(H_p)=H_{p\cdot g}\) for all \(g\in G\).
3. **Equivariant splitting of \(d\pi\).** A \(G\)-equivariant bundle map \(\mathrm{hor}:\pi^*TM\to TP\) such that \(d\pi\circ \mathrm{hor}=\mathrm{id}_{\pi^*TM}\). Its image is the horizontal distribution \(H\).
4. **Connection one-form.** A \(\mathfrak g\)-valued 1-form \(\omega\in\Omega^1(P;\mathfrak g)\) such that:
   - \(\omega(\xi^\#)=\xi\) for all \(\xi\in\mathfrak g\) (reproduces fundamental vector fields),
   - \(R_g^*\omega=\mathrm{Ad}_{g^{-1}}\omega\) for all \(g\in G\).
   The corresponding horizontal distribution is \(H=\ker\omega\).

These correspondences are inverse to each other: a connection 1-form determines horizontals via \(\ker\omega\), and a horizontal distribution determines \(\omega\) by projection \(TP\to V\!P\cong P\times\mathfrak g\).

## Examples
1. **Trivial bundle.** On \(P=M\times G\), any \(\mathfrak g\)-valued 1-form \(A\) on \(M\) defines a principal connection with connection form \(\omega = \mathrm{Ad}_{g^{-1}}A + g^{-1}dg\) in the product coordinates \((x,g)\).
2. **Levi–Civita connection as a principal connection.** The Levi–Civita connection on \(TM\) corresponds to a principal connection on the orthonormal frame bundle \(O(TM)\to M\), with horizontals defined by parallel translation of frames.
3. **Connection from a splitting.** If one has a \(G\)-equivariant splitting of \(TP\to \pi^*TM\), its image gives horizontals directly, without writing a connection form.
