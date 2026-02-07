---
title: "Pullback bundle"
description: "The fiber bundle over N obtained by pulling back a bundle over M along a smooth map f: N to M."
---

Let \(\pi:E\to M\) be a {{< knowl id="smooth-fiber-bundle" text="smooth fiber bundle" >}} and let \(f:N\to M\) be a {{< knowl id="smooth-map" text="smooth map" >}}. The **pullback bundle** \(f^*E\to N\) is defined as the fiber product
\[
f^*E \;:=\;\{(n,e)\in N\times E \mid f(n)=\pi(e)\}.
\]
Let \(\pi_f:f^*E\to N\) be the restriction of the projection \(\mathrm{pr}_1:N\times E\to N\). Then \(\pi_f\) is a smooth fiber bundle over \(N\) with the same typical fiber as \(E\to M\).

There is a canonical map \(\widetilde f:f^*E\to E\), \(\widetilde f(n,e)=e\), which is a {{< knowl id="bundle-morphism" text="bundle morphism" >}} covering \(f\). Locally, if \(E|_U\cong U\times F\), then \((f^*E)|_{f^{-1}(U)}\cong f^{-1}(U)\times F\), so pullback respects local trivializations.

## Examples
1. **Restriction to a submanifold:** if \(i:Z\hookrightarrow M\) is an embedding and \(E\to M\) is a bundle, then \(i^*E\to Z\) is the restricted bundle \(E|_Z\).
2. **Pullback of the tangent bundle:** for \(f:N\to M\), the bundle \(f^*(TM)\to N\) has fiber \((f^*TM)_n\cong T_{f(n)}M\) and is used to view \(df\) as a fiberwise linear map \(TN\to f^*TM\).
3. **Trivial bundles pull back trivially:** if \(E=M\times F\), then \(f^*E\cong N\times F\).
