---
title: "Connections on vector bundles via frame bundles"
description: "Equivalence between covariant derivatives on a rank-n vector bundle and principal connections on its frame bundle."
---

Let $E\to M$ be a smooth real rank-$n$ vector bundle over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$. Denote by $\mathrm{Fr}(E)\to M$ the principal $\mathrm{GL}(n,\mathbb R)$-bundle of frames of $E$ (ordered bases of each fiber).

A {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} can be described either by a covariant derivative on sections of $E$ or by a principal connection on $\mathrm{Fr}(E)$.

## Theorem (TFAE: vector bundle connections and frame bundle connections)
The following data are equivalent, naturally and bijectively:

1. A vector bundle connection $\nabla$ on $E$ (a covariant derivative satisfying the Leibniz rule).

2. A {{< knowl id="principal-connection" text="principal connection" >}} on the principal bundle $\mathrm{Fr}(E)\to M$.

3. A $\mathrm{GL}(n,\mathbb R)$-equivariant horizontal distribution $H\subset T\,\mathrm{Fr}(E)$, i.e. a smooth subbundle such that
   \[
   T_p\mathrm{Fr}(E)=H_p\oplus \ker(d\pi_p)\quad\text{and}\quad (dR_A)(H_p)=H_{p\cdot A}
   \]
   for all $A\in \mathrm{GL}(n,\mathbb R)$, where $R_A$ is the right action on frames.

4. A connection 1-form $\omega\in\Omega^1(\mathrm{Fr}(E);\mathfrak{gl}(n,\mathbb R))$ satisfying the standard axioms (reproduces fundamental vertical fields and is equivariant under the right action).

Moreover, under this correspondence:

- Given a principal connection on $\mathrm{Fr}(E)$, one obtains $\nabla$ by declaring that a section of $E$ is parallel if and only if its equivariant function on $\mathrm{Fr}(E)$ is constant along horizontal lifts (equivalently, parallel transport in $\mathrm{Fr}(E)$ induces parallel transport in $E$).

- Given $\nabla$, one obtains a principal connection on $\mathrm{Fr}(E)$ by transporting frames along curves using the induced {{< knowl id="parallel-transport" text="parallel transport" >}} and taking the resulting horizontal lifts of tangent vectors.

A useful special case is $E=TM$: connections on the tangent bundle correspond to principal connections on the {{< knowl id="frame-bundle-fr-of-a-manifold-m" text="frame bundle" >}} of $M$.

## Examples
1. **Trivial bundle and matrix-valued 1-forms.**  
   For the {{< knowl id="trivial-vector-bundle-mvm" text="trivial vector bundle" >}} $E=M\times\mathbb R^n$, a connection is determined by a matrix of 1-forms $A\in\Omega^1(M;\mathfrak{gl}(n,\mathbb R))$ via
   \[
   \nabla = d + A
   \]
   in the standard frame. The corresponding principal connection on $M\times \mathrm{GL}(n,\mathbb R)$ has connection form obtained from $A$ in that trivialization.

2. **Riemannian geometry.**  
   On a Riemannian manifold, the Levi–Civita connection on $TM$ corresponds to a principal connection on the {{< knowl id="orthonormal-frame-bundle-o-of-a-riemannian-manifold" text="orthonormal frame bundle" >}} (a reduction from $\mathrm{GL}(n)$ to $\mathrm{O}(n)$).

3. **Line bundles.**  
   For a real line bundle $L\to M$, the frame bundle is a principal $\mathrm{GL}(1,\mathbb R)\cong \mathbb R^\times$-bundle. A connection on $L$ is equivalent to a principal connection on that frame bundle; in a local trivialization, it is described by an ordinary 1-form.
