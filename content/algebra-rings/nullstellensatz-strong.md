---
title: "Hilbert's Nullstellensatz (strong)"
description: "Over an algebraically closed field, the ideal of a variety is the radical of the defining ideal."
---

**Hilbert's Nullstellensatz (strong)**: Let \(k\) be an algebraically closed {{< knowl id="field" text="field" >}} and let \(I\triangleleft k[x_1,\dots,x_n]\) be an {{< knowl id="ideal" text="ideal" >}} in the {{< knowl id="polynomial-ring" text="polynomial ring" >}}. Let
\[
I(V(I))=\{f\in k[x_1,\dots,x_n] : f(a)=0\ \text{for all }a\in V(I)\}.
\]
Then
\[
I(V(I))=\sqrt{I},
\]
where \(\sqrt{I}\) denotes the {{< knowl id="radical-of-ideal" text="radical of an ideal" >}}.

This identifies geometric vanishing with algebraic nilpotence modulo \(I\) and implies, for instance, that varieties correspond to radical ideals and irreducible varieties correspond to {{< knowl id="prime-ideal" text="prime ideals" >}}.

**Proof sketch**: The inclusion \(\sqrt{I}\subseteq I(V(I))\) is immediate. For the reverse inclusion one uses the Rabinowitsch trick: if \(f\notin \sqrt{I}\), then \(I+(1-tf)\subset k[x_1,\dots,x_n,t]\) is a proper ideal, hence has a common zero by the weak form, which forces a point in \(V(I)\) where \(f\) does not vanish.