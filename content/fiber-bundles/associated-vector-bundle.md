---
title: "Associated vector bundle"
description: "A vector bundle obtained from a principal bundle and a linear representation of its structure group."
---

Associated vector bundles are a special case of {{< knowl id="associated-bundle" text="associated bundles" >}} where the fiber is a vector space and the structure group acts linearly.

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with right action $(p,g)\mapsto p\cdot g$. Let $\rho:G\to GL(V)$ be a {{< knowl id="representation-of-a-lie-group" text="representation of a Lie group" section="lie-groups">}}. View this as a left action of $G$ on $V$ via
\[
g\cdot v := \rho(g)\,v.
\]
(Compare the convention in {{< knowl id="convention-associated-bundles-use-a-left-g-action-on-the-fiber-f" text="associated bundles use a left G-action on the fiber" >}}.)

The **associated vector bundle** with fiber $V$ is
\[
E := P\times_G V := (P\times V)/\sim,
\]
where the equivalence relation is
\[
(p\cdot g,\; v)\sim (p,\; g\cdot v)\qquad\text{for all }p\in P,\ g\in G,\ v\in V.
\]
Write the equivalence class of $(p,v)$ as $[p,v]$.

The projection map $\pi_E:E\to M$ is defined by
\[
\pi_E([p,v]) := \pi(p).
\]
With this projection and the linear structure on the fibers inherited from $V$, $E$ becomes a {{< knowl id="vector-bundle" text="vector bundle" >}} over $M$.

This construction is the specialization of {{< knowl id="construction-associated-bundle-p-g-f-from-a-left-g-space-f" text="the associated bundle construction P times_G F" >}} to the case $F=V$.

## Local trivializations and transition functions
Given a local section $s:U\to P$ (see {{< knowl id="construction-local-trivialization-from-a-local-section" text="local trivialization from a local section" >}}), there is a canonical vector bundle trivialization
\[
\Phi_s: E|_U \longrightarrow U\times V,\qquad \Phi_s([s(x),v])=(x,v).
\]

If $s_i$ and $s_j$ are local sections on $U_i$ and $U_j$ with $s_i(x)=s_j(x)\,g_{ij}(x)$ on overlaps, then the corresponding transition function for $E$ is
\[
(x,v)\longmapsto \bigl(x,\ \rho(g_{ij}(x))\,v\bigr),
\]
so the vector bundle transition functions are obtained by composing the principal bundle transition functions (see {{< knowl id="transition-function" text="transition function" >}}) with the representation $\rho$.

## Examples
1. **Tangent bundle as an associated bundle**
   Let $M$ be an $n$-manifold and let $Fr(M)\to M$ be its {{< knowl id="frame-bundle-fr-of-a-manifold-m" text="frame bundle" >}}, a principal $GL(n,\mathbb{R})$-bundle. Using the standard representation of $GL(n,\mathbb{R})$ on $\mathbb{R}^n$, the associated vector bundle is canonically isomorphic to the tangent bundle:
   \[
   TM \cong Fr(M)\times_{GL(n,\mathbb{R})}\mathbb{R}^n.
   \]

2. **Complex line bundles from principal $U(1)$-bundles**
   If $P\to M$ is a principal $U(1)$-bundle and $\rho:U(1)\to GL(1,\mathbb{C})$ is the standard character $\rho(e^{i\theta})=e^{i\theta}$, then
   \[
   L := P\times_{U(1)}\mathbb{C}
   \]
   is a complex line bundle. For instance, using the {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}} $S^3\to S^2$ as $P$, this produces the tautological line bundle over $S^2\cong \mathbb{CP}^1$.

3. **Adjoint (Lie algebra) bundle**
   Taking $V=\mathfrak{g}$ with the adjoint representation gives the associated bundle
   \[
   \mathrm{Ad}(P)=P\times_G \mathfrak{g},
   \]
   which is the usual adjoint Lie algebra bundle (see {{< knowl id="construction-adjoint-lie-algebra-bundle-ad" text="construction of the adjoint Lie algebra bundle" >}}).
