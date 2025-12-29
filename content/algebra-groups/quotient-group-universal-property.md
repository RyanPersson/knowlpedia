---
title: "Universal Property of Quotient Groups"
description: "Homomorphisms out of G that kill N factor uniquely through G/N"
---

**Universal Property of Quotient Groups**: Let $G$ be a {{</* knowl id="group" text="group" */>}} and let $N\trianglelefteq G$ be a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}}. Let $\pi:G\to G/N$ be the canonical projection to the {{</* knowl id="quotient-group" text="quotient group" */>}}. If $K$ is a group and $f:G\to K$ is a {{</* knowl id="group-homomorphism" text="group homomorphism" */>}} such that $N\subseteq \ker(f)$ (where $\ker(f)$ is the {{</* knowl id="kernel-group" text="kernel" */>}} of $f$), then there exists a unique homomorphism $\bar f:G/N\to K$ with
$
f = \bar f \circ \pi.
$

Equivalently: giving a homomorphism $G/N\to K$ is the same as giving a homomorphism $G\to K$ that sends every element of $N$ to the identity of $K$.

**Proof sketch**: Define $\bar f(gN)=f(g)$. This is well-defined because if $gN=g'N$ then $g^{-1}g'\in N\subseteq\ker(f)$, so $f(g)=f(g')$. Homomorphism and uniqueness follow because $\pi$ is surjective and $\bar f$ is forced by $\bar f(\pi(g))=f(g)$.
