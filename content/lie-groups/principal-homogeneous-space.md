---
title: "Principal Homogeneous Space"
description: "A space with a free and transitive action of a Lie group, also called a torsor."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. A **principal homogeneous space** (or **\(G\)-torsor**) is a {{< knowl id="smooth-manifold" section="fiber-bundles" text="smooth manifold" >}} \(P\) equipped with a smooth action
$$
G\times P \to P,\qquad (g,p)\mapsto g\cdot p,
$$
that is:
- **Free:** if \(g\cdot p=p\) for some \(p\in P\), then \(g=e\).
- **Transitive:** for any \(p,q\in P\), there exists \(g\in G\) with \(g\cdot p=q\).

Equivalently, the action is **simply transitive**: for each \(p,q\in P\) there is a unique \(g\in G\) with \(g\cdot p=q\).

## Choosing a basepoint identifies it with the group
Fix \(p_0\in P\). The map
$$
\theta_{p_0}:G\to P,\qquad \theta_{p_0}(g)=g\cdot p_0
$$
is a diffeomorphism. This identifies \(P\) with \(G\), but the identification depends on the choice of \(p_0\), so there is generally no canonical “origin” in a torsor.

## Examples and related notions
- \(G\) acting on itself by {{< knowl id="left-translation" text="left translation" >}} is a principal homogeneous space.
- More generally, a transitive action with stabilizer \(H\) gives a homogeneous space \(G/H\); compare {{< knowl id="quotient-lie-group" text="quotients" >}}. A principal homogeneous space is the special case \(H=\{e\}\).

Principal homogeneous spaces are the geometric backdrop for principal bundles and symmetry without a preferred identity element.
