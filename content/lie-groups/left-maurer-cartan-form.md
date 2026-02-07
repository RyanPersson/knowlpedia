---
title: "Left Maurer–Cartan form"
description: "The canonical g-valued 1-form θ^L = (dL_{g^{-1}})_g on a Lie group."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with Lie algebra $\mathfrak g=T_eG$.

**Definition (Left Maurer–Cartan form).**  
The **left Maurer–Cartan form** is the $\mathfrak g$-valued $1$-form $\theta^L\in \Omega^1(G;\mathfrak g)$ defined by
\[
\theta^L_g : T_gG \to \mathfrak g,\qquad \theta^L_g(v)=(dL_{g^{-1}})_g(v).
\]
Equivalently, $\theta^L$ is characterized by:

- (Normalization) $\theta^L_e=\mathrm{id}_{\mathfrak g}$, and
- (Left invariance) $(L_h)^*\theta^L=\theta^L$ for all $h\in G$.

**Maurer–Cartan equation.**  
$\theta^L$ satisfies the {{< knowl id="maurer-cartan-equation" text="Maurer–Cartan equation" >}}
\[
d\theta^L + \tfrac12[\theta^L,\theta^L]=0,
\]
where the bracket combines the Lie bracket on $\mathfrak g$ with wedge product.

**Context and use.**  
The left Maurer–Cartan form identifies tangent vectors on $G$ with elements of $\mathfrak g$ in a left-translation invariant way, and it packages all {{< knowl id="left-invariant-differential-form" text="left-invariant forms" >}} as alternating tensors on $\mathfrak g$. The right-handed analogue is the {{< knowl id="right-maurer-cartan-form" text="right Maurer–Cartan form" >}}.
