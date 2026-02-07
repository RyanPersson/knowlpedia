---
title: "Pontryagin class via Chern–Weil theory"
description: "Characteristic cohomology classes of a real vector bundle defined from curvature, using the complexification in Chern–Weil theory."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\pi:E\to M$ be a real vector bundle of rank $r$. Choose a bundle metric on $E$ and a compatible {{< knowl id="connection-on-a-vector-bundle" text="connection" >}} $\nabla$ (so the structure group reduces to $O(r)$). Let $F_\nabla\in\Omega^2(M;\mathfrak{so}(E))$ be its {{< knowl id="curvature" text="curvature" >}}.

## Definition (Pontryagin forms and Pontryagin classes)
Let $E^{\mathbb C}:=E\otimes_{\mathbb R}\mathbb C$ be the complexification, and let $\nabla^{\mathbb C}$ be the induced complex connection. Define the **Pontryagin forms** by
\[
p_k(\nabla)\;:=\;(-1)^k\,c_{2k}(\nabla^{\mathbb C})\in \Omega^{4k}(M),
\]
where $c_{2k}(\nabla^{\mathbb C})$ is the $(2k)$th Chern form of the complex bundle $E^{\mathbb C}$ (defined as in {{< knowl id="chern-class" text="Chern–Weil Chern forms" >}}).

Then:
1. Each $p_k(\nabla)$ is closed: $d\,p_k(\nabla)=0$, where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.
2. The de Rham class $[p_k(\nabla)]\in H^{4k}_{\mathrm{dR}}(M)$ is independent of the choice of compatible connection.
3. The **$k$th Pontryagin class** $p_k(E)\in H^{4k}(M;\mathbb Z)$ is the unique integral class whose real image equals $[p_k(\nabla)]$.

Equivalently, $p_k(E)$ is the Chern–Weil class associated to the structure group $O(r)$ (or $SO(r)$ in the oriented case) by applying an $Ad$-invariant polynomial on $\mathfrak{so}(r)$ corresponding to the $k$th elementary symmetric polynomial in the squares of the formal curvature eigenvalues.

Naturality holds: for any {{< knowl id="smooth-map" text="smooth map" >}} $f:N\to M$,
\[
p_k(f^*E)=f^*p_k(E).
\]

## Examples
1. **Trivial bundle / flat connection.** If $E\cong M\times\mathbb R^r$ with the flat connection, then $F_\nabla=0$, hence $p_k(\nabla)=0$ for all $k\ge 1$, and thus $p_k(E)=0$.

2. **Underlying real bundle of a complex line bundle.** Let $L\to M$ be a complex line bundle with $c_1(L)=x\in H^2(M;\mathbb Z)$. For the underlying real rank-2 bundle $L_{\mathbb R}$ one has
   \[
   p_1(L_{\mathbb R})=x^2\in H^4(M;\mathbb Z),
   \]
   because $p_1=(-1)c_2\big((L_{\mathbb R})^{\mathbb C}\big)$ and $(L_{\mathbb R})^{\mathbb C}\cong L\oplus \overline{L}$.

3. **Dimensional vanishing.** If $\dim M < 4k$, then every $4k$-form vanishes and hence $p_k(E)=0$ in de Rham cohomology (and therefore in rational cohomology) for degree reasons.
