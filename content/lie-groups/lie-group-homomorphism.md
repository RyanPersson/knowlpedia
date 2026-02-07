---
title: "Lie Group Homomorphism"
description: "A smooth map between Lie groups that is also a group homomorphism."
---

A **Lie group homomorphism** is a map \(\varphi:G\to H\) between {{< knowl id="lie-group" text="Lie groups" section="fiber-bundles">}} such that:
- \(\varphi(gh)=\varphi(g)\varphi(h)\) for all \(g,h\in G\), and
- \(\varphi\) is a {{< knowl id="smooth-map" section="fiber-bundles" text="smooth map" >}}.

Equivalently, \(\varphi\) is a group homomorphism that is smooth as a map of manifolds.

## Differential at the identity
The {{< knowl id="differential-of-a-smooth-map" section="fiber-bundles" text="differential" >}} at the identity,
$$
(d\varphi)_e:T_eG\to T_eH,
$$
is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}
\((d\varphi)_e:\mathfrak{g}\to\mathfrak{h}\), where \(\mathfrak{g}=T_eG\) and \(\mathfrak{h}=T_eH\); see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}.

## Kernels, images, and coverings
- \(\ker(\varphi)\) is a closed subgroup of \(G\), hence an embedded {{< knowl id="lie-subgroup" text="Lie subgroup" >}} (by {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}).
- The image \(\varphi(G)\) is an immersed Lie subgroup of \(H\).
- When \(\ker(\varphi)\) is discrete and \(\varphi\) is a local diffeomorphism, \(\varphi\) is a {{< knowl id="covering-lie-group" text="covering Lie group" >}} map.

Lie group homomorphisms are the morphisms in the category underlying the {{< knowl id="lie-correspondence" text="Lie correspondence" >}}.
