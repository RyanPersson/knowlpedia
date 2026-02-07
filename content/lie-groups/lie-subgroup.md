---
title: "Lie Subgroup"
description: "A subgroup of a Lie group that carries a compatible immersed submanifold structure."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. A **Lie subgroup** of \(G\) is a subgroup \(H\le G\) together with the structure of an immersed {{< knowl id="smooth-manifold" section="fiber-bundles" text="submanifold" >}} such that the inclusion map
$$
i:H\hookrightarrow G
$$
is a smooth immersion and a group homomorphism (so the group operations on \(H\) are smooth).

A Lie subgroup is called **embedded** if \(i\) is an embedding (so \(H\) is an actual submanifold of \(G\)).

## Closed subgroups
A crucial fact is the {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}: if \(H\) is a closed subgroup of \(G\) (as a subset), then \(H\) is an embedded Lie subgroup.

## Relationship to Lie algebras
The Lie algebra \(\mathfrak{h}=T_eH\) identifies with a {{< knowl id="lie-subalgebra" text="Lie subalgebra" >}} of \(\mathfrak{g}=T_eG\); see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}.

## Quotients
If \(H\) is closed, the quotient \(G/H\) carries a natural smooth structure and is the underlying manifold of the {{< knowl id="quotient-lie-group" text="quotient construction" >}} when \(H\) is normal.

## Examples
- \(\operatorname{SO}(n)\le \operatorname{GL}(n,\mathbb{R})\).
- The diagonal matrices form a Lie subgroup of \(\operatorname{GL}(n,\mathbb{R})\).
