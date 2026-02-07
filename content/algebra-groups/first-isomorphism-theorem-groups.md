---
title: "First Isomorphism Theorem (Groups)"
description: "A homomorphism factors through the quotient by its kernel, giving G/ker(f) ≅ im(f)"
---

**First Isomorphism Theorem (Groups).**
Let $G$ and $H$ be {{< knowl id="group" text="groups" >}}, and let $f: G \to H$ be a {{< knowl id="group-homomorphism" text="group homomorphism" >}}. Let $K = \ker(f)$ be the {{< knowl id="kernel-group" text="kernel" >}} of $f$ and let $I = \operatorname{im}(f)$ be the {{< knowl id="image-group" text="image" >}} of $f$, i.e.
$$
K = \{g \in G : f(g) = e_H\}, \qquad I = \{f(g) : g \in G\}.
$$

Then $K$ is a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of $G$ (see {{< knowl id="kernels-are-normal" text="kernels are normal subgroups" >}}), and the induced map
$$
\bar f: G/K \to I, \qquad \bar f(gK) = f(g),
$$

is a well-defined {{< knowl id="group-isomorphism" text="isomorphism" >}}. In particular, if $f$ is surjective then $G/K \cong H$.

This result is the basic "quotient = image" principle and is the prototype for the {{< knowl id="second-isomorphism-theorem-groups" text="second" >}} and {{< knowl id="third-isomorphism-theorem-groups" text="third isomorphism theorems" >}}. It is often packaged as an {{< knowl id="exact-sequence-groups" text="exact sequence" >}} $1 \to K \to G \to I \to 1$.
