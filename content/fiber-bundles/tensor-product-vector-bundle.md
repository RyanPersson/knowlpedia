---
title: "Tensor product vector bundle"
description: "The bundle over a common base whose fiber is the tensor product of the fibers of two bundles."
---

Let $\pi_E:E\to M$ and $\pi_F:F\to M$ be smooth vector bundles over the same {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$. Their **tensor product bundle** is a vector bundle
\[
\pi_{E\otimes F}:E\otimes F \to M
\]
characterized by the property that each fiber is the tensor product of fibers:
\[
(E\otimes F)_x \cong E_x\otimes_{\mathbb F} F_x.
\]

Concretely, choose local frames $(e_1,\dots,e_r)$ of $E|_U$ and $(f_1,\dots,f_s)$ of $F|_U$. Then $(e_i\otimes f_j)_{1\le i\le r,\,1\le j\le s}$ is a local frame of $(E\otimes F)|_U$. If the transition matrices of $E$ and $F$ on overlaps are $g_E$ and $g_F$, then the transition matrix of $E\otimes F$ is the Kronecker/tensor product representation, i.e. it is given by $g_E\otimes g_F$ in the induced basis.

The rank satisfies $\mathrm{rank}(E\otimes F)=\mathrm{rank}(E)\,\mathrm{rank}(F)$.

## Examples
1. **Endomorphism bundle.** For any bundle $E\to M$, the bundle $\mathrm{End}(E):=E\otimes E^*$ has fiber $\mathrm{End}(E_x)$; fiberwise composition makes $\mathrm{End}(E)$ a bundle of associative algebras.

2. **Type (1,1) tensors.** The bundle $TM\otimes T^*M$ has fiber $T_xM\otimes T_x^*M\cong \mathrm{End}(T_xM)$, so its sections can be viewed as smooth fields of linear endomorphisms of tangent spaces (compare {{< knowl id="tangent-bundle" text="tangent bundle" >}}).

3. **Twisting forms by a bundle.** If $E\to M$ is any bundle, then $T^*M\otimes E$ is the bundle of $E$-valued 1-forms; its sections are used to write down {{< knowl id="connection-on-a-vector-bundle" text="connections on a vector bundle" >}} in local form.
