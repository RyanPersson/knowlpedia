---
title: "Flat connection on a trivial bundle"
description: "The product connection on a trivial bundle whose curvature and holonomy are trivial."
---

Let $P=M\times G\to M$ be the {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}} over a smooth manifold $M$.

## Definition (product connection / zero gauge potential)
Define a horizontal subspace at $(x,g)\in M\times G$ by
\[
H_{(x,g)} := T_xM \times \{0\} \;\subset\; T_xM\oplus T_gG \cong T_{(x,g)}(M\times G).
\]
This $G$-invariant splitting defines a {{< knowl id="principal-connection" text="principal connection" >}} on $P$, often called the **product connection**.

In the global trivialization given by the canonical section $s(x)=(x,e)$, the associated gauge potential is the $\mathfrak g$-valued 1-form $A\in\Omega^1(M;\mathfrak g)$ given by $A=0$.

## Properties
- The {{< knowl id="curvature" text="curvature" >}} of this connection vanishes identically.
- {{< knowl id="parallel-transport" text="Parallel transport" >}} along a curve $\gamma$ keeps the $G$-coordinate constant in the product chart.
- The {{< knowl id="holonomy-group" text="holonomy group" >}} is trivial (contained in the identity element), for each basepoint.

The induced connection on any associated vector bundle $M\times V$ is the “ordinary derivative” connection: in the standard frame, $\nabla=d$.

## Examples
1. **Flat connections on trivial line bundles.**  
   On $M\times U(1)$, this is the standard flat circle-bundle connection; parallel transport is literally constant phase in the chosen trivialization.

2. **Associated vector bundle: constant sections are parallel.**  
   For $E=M\times\mathbb R^n$, the induced connection satisfies $\nabla s=ds$; in particular, constant maps $s:M\to\mathbb R^n$ are parallel sections.

3. **Restriction to open subsets.**  
   If $U\subset M$ is open, restricting the trivial bundle and this connection to $U$ gives the same product connection on $U\times G\to U$.
