---
title: "Cocycle condition for transition functions"
description: "The compatibility identities on double and triple overlaps needed to glue a fiber bundle."
---

Let \(\{(U_i,\Phi_i)\}\) be a {{< knowl id="bundle-atlas" text="bundle atlas" >}} for a smooth fiber bundle with typical fiber \(F\), and let \(t_{ij}:U_{ij}\to \mathrm{Diff}(F)\) be the associated {{< knowl id="transition-function" text="transition functions" >}}. They satisfy the following identities:

1. **Identity on the diagonal:** \(t_{ii}(x)=\mathrm{id}_F\) for all \(x\in U_i\).
2. **Inverse on overlaps:** on \(U_{ij}\), one has \(t_{ji}(x)=t_{ij}(x)^{-1}\).
3. **Cocycle condition on triple overlaps:** on \(U_{ijk}=U_i\cap U_j\cap U_k\),
   \[
   t_{ij}(x)\circ t_{jk}(x)=t_{ik}(x)\qquad \text{for all }x\in U_{ijk}.
   \]

These conditions are exactly the statement that the changes of trivialization compose consistently, so that the local products \(U_i\times F\) glue to a well-defined {{< knowl id="smooth-fiber-bundle" text="smooth fiber bundle" >}}.

## Examples
1. **Trivial bundle:** all \(t_{ij}\) are the identity, so the cocycle condition holds tautologically.
2. **Möbius line bundle:** with \(t_{12}\equiv-1\), the cocycle identity on a triple overlap reduces to \((-1)\cdot(-1)=1\).
3. **Tangent bundle:** on triple overlaps of coordinate charts, the cocycle condition is the chain rule for Jacobians of coordinate changes.
