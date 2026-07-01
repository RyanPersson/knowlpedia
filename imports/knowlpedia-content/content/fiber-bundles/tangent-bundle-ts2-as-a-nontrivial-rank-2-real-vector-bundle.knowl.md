+++
id = "fiber-bundles/tangent-bundle-ts2-as-a-nontrivial-rank-2-real-vector-bundle"
title = "The tangent bundle of the 2-sphere is nontrivial"
kind = "knowl"
summary = "The tangent bundle of the 2-sphere is a rank-2 real vector bundle that admits no global nowhere-zero vector field."
aliases = ["tangent-bundle-ts2-as-a-nontrivial-rank-2-real-vector-bundle", "The tangent bundle of the 2-sphere is nontrivial"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/tangent-bundle-ts2-as-a-nontrivial-rank-2-real-vector-bundle.md"
+++

Let $S^2$ be the 2-sphere. Its [[fiber-bundles/tangent-bundle|tangent bundle]] $\pi:TS^2\to S^2$ is a smooth real vector bundle of rank $2$.

## Statement
The bundle $TS^2$ is **not** isomorphic (as a rank-2 real vector bundle) to the [[fiber-bundles/trivial-vector-bundle-mvm|trivial rank-2 bundle]] $S^2\times \mathbb R^2$.

Equivalently:
- $TS^2$ does not admit a global frame of smooth sections, and in particular
- $TS^2$ admits no nowhere-vanishing smooth [[fiber-bundles/vector-field|vector field]] on $S^2$.

A standard proof uses the “hairy ball” phenomenon: every continuous tangent vector field on $S^2$ has a zero. Since a global nowhere-zero section would trivialize a rank-1 subbundle and (together with a second independent section) produce a global frame, this obstructs triviality.

## Examples
1. **Local triviality is easy: remove a point.**
   On $S^2\setminus\{p\}\cong \mathbb R^2$, the tangent bundle is trivial: $T(S^2\setminus\{p\})\cong (S^2\setminus\{p\})\times\mathbb R^2$. The obstruction is global, not local.

2. **Contrast with the circle.**
   The circle $S^1$ admits a nowhere-vanishing tangent vector field (rotation), so $TS^1$ is trivial. This highlights that the failure for $S^2$ is not automatic for spheres.

3. **Frame bundle reflection.**
   Nontriviality of $TS^2$ implies that the frame bundle $\mathrm{Fr}(TS^2)$ is not globally a product $S^2\times \mathrm{GL}(2,\mathbb R)$, even though it is locally trivial by definition.
