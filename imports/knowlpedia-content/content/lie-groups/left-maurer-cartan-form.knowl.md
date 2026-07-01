+++
id = "lie-groups/left-maurer-cartan-form"
title = "Left Maurer–Cartan form"
kind = "knowl"
summary = "The canonical g-valued 1-form θ^L = (dL_{g^{-1}})_g on a Lie group."
aliases = ["left-maurer-cartan-form", "Left Maurer–Cartan form"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/left-maurer-cartan-form.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak g=T_eG$.

**Definition (Left Maurer–Cartan form).**
The **left Maurer–Cartan form** is the $\mathfrak g$-valued $1$-form $\theta^L\in \Omega^1(G;\mathfrak g)$ defined by
\[
\theta^L_g : T_gG \to \mathfrak g,\qquad \theta^L_g(v)=(dL_{g^{-1}})_g(v).
\]
Equivalently, $\theta^L$ is characterized by:

- (Normalization) $\theta^L_e=\mathrm{id}_{\mathfrak g}$, and
- (Left invariance) $(L_h)^*\theta^L=\theta^L$ for all $h\in G$.

**Maurer–Cartan equation.**
$\theta^L$ satisfies the [[lie-groups/maurer-cartan-equation|Maurer–Cartan equation]]
\[
d\theta^L + \tfrac12[\theta^L,\theta^L]=0,
\]
where the bracket combines the Lie bracket on $\mathfrak g$ with wedge product.

**Context and use.**
The left Maurer–Cartan form identifies tangent vectors on $G$ with elements of $\mathfrak g$ in a left-translation invariant way, and it packages all [[lie-groups/left-invariant-differential-form|left-invariant forms]] as alternating tensors on $\mathfrak g$. The right-handed analogue is the [[lie-groups/right-maurer-cartan-form|right Maurer–Cartan form]].
