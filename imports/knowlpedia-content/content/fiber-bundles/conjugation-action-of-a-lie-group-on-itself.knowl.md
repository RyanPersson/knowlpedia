+++
id = "fiber-bundles/conjugation-action-of-a-lie-group-on-itself"
title = "Conjugation action of a Lie group on itself"
kind = "knowl"
summary = "The smooth action of a Lie group on itself given by sending an element to its conjugate by another element."
aliases = ["conjugation-action-of-a-lie-group-on-itself", "Conjugation action of a Lie group on itself"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/conjugation-action-of-a-lie-group-on-itself.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]]. The **conjugation action** of $G$ on itself is the map
\[
C:G\times G\to G,\qquad C(g,h)=ghg^{-1}.
\]
This is a smooth left action: one has $C(e,h)=h$ and $C(g_1,C(g_2,h))=C(g_1g_2,h)$ for all $g_1,g_2,h\in G$. For each fixed $g$, the map $h\mapsto ghg^{-1}$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]] of $G$, with inverse given by conjugation by $g^{-1}$.

Differentiating the conjugation map at the identity in the second variable yields the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]] on the Lie algebra: $\mathrm{Ad}_g=(\mathrm{d}C_g)_e$ where $C_g(h)=ghg^{-1}$.

## Examples
1. **Abelian groups.** If $G$ is abelian, then $ghg^{-1}=h$ for all $g,h$, so the conjugation action is trivial and every conjugacy class is a point.
2. **Similarity of matrices.** For $G=\mathrm{GL}(n,\mathbb{R})$, conjugation is $C(A,B)=ABA^{-1}$; its orbits are similarity classes, which control Jordan normal form over algebraically closed fields.
3. **Normal subgroups via conjugation.** A subgroup $N\subset G$ is normal if and only if it is invariant under conjugation: $gNg^{-1}=N$ for all $g\in G$.
