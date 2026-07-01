+++
id = "lie-groups/principal-homogeneous-space"
title = "Principal Homogeneous Space"
kind = "knowl"
summary = "A space with a free and transitive action of a Lie group, also called a torsor."
aliases = ["principal-homogeneous-space", "Principal Homogeneous Space"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/principal-homogeneous-space.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. A **principal homogeneous space** (or **\(G\)-torsor**) is a [[fiber-bundles/smooth-manifold|smooth manifold]] \(P\) equipped with a smooth action
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
- \(G\) acting on itself by [[lie-groups/left-translation|left translation]] is a principal homogeneous space.
- More generally, a transitive action with stabilizer \(H\) gives a homogeneous space \(G/H\); compare [[lie-groups/quotient-lie-group|quotients]]. A principal homogeneous space is the special case \(H=\{e\}\).

Principal homogeneous spaces are the geometric backdrop for principal bundles and symmetry without a preferred identity element.
