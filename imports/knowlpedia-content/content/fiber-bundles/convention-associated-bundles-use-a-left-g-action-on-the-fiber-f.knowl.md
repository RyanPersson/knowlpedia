+++
id = "fiber-bundles/convention-associated-bundles-use-a-left-g-action-on-the-fiber-f"
title = "Convention: associated bundles use a left action on the fiber"
kind = "knowl"
summary = "Convention for forming an associated bundle from a right principal action and a left action on the typical fiber"
aliases = ["convention-associated-bundles-use-a-left-g-action-on-the-fiber-f", "Convention: associated bundles use a left action on the fiber"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/convention-associated-bundles-use-a-left-g-action-on-the-fiber-f.md"
+++

Associated bundles combine the right principal action on a [[fiber-bundles/principal-g-bundle|principal bundle]] with a left action on the model fiber.

## Convention
Let $\pi:P\to M$ be a principal $G$-bundle equipped with the right action $P\times G\to P$, $(p,g)\mapsto p\cdot g$ (see [[fiber-bundles/convention-principal-bundles-use-a-right-g-action-on-p|right action convention]]). Let $F$ be a smooth left $G$-space, i.e. a manifold with a smooth action $G\times F\to F$, $(g,f)\mapsto g\cdot f$ (compare [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth group action]]).

We define the **associated bundle**
\[
P\times_G F
\]
to be the quotient of $P\times F$ by the equivalence relation
\[
(p\cdot g,\ f)\sim (p,\ g\cdot f).
\]
We denote the equivalence class of $(p,f)$ by $[p,f]$. The projection
\[
[p,f]\longmapsto \pi(p)
\]
is well-defined and makes $P\times_G F\to M$ into a [[fiber-bundles/associated-bundle|fiber bundle associated to P]]. This is the convention used in [[fiber-bundles/construction-associated-bundle-p-g-f-from-a-left-g-space-f|the associated bundle construction]].

A useful bookkeeping consequence is the following: if local sections $s_i:U_i\to P$ define transition functions by $s_j=s_i\,g_{ij}$ (as in [[fiber-bundles/construction-transition-functions-g-iju-iu-jg-from-local-sections|transition functions from local sections]]), then the induced local trivializations satisfy
\[
[s_j(x),f]=[s_i(x),\,g_{ij}(x)\cdot f],
\]
so the same $g_{ij}$ acts on the fiber by the given left action.

## Examples
1. **Associated vector bundle from a representation.**
   If $\rho:G\to GL(V)$ is a [[lie-groups/representation-of-a-lie-group|representation]], then $V$ is a left $G$-space via $g\cdot v:=\rho(g)v$, and $P\times_G V$ is an [[fiber-bundles/associated-vector-bundle|associated vector bundle]].

2. **Recovering a vector bundle from its frame bundle.**
   For a rank $n$ vector bundle $E\to M$ with frame bundle $P=\operatorname{Fr}(E)$, take $F=\mathbb R^n$ with the standard left $GL(n)$-action. Then
   \[
   \operatorname{Fr}(E)\times_{GL(n)}\mathbb R^n \cong E
   \]
   canonically (this is the basic example behind [[fiber-bundles/tfae-vector-bundle-connections-via-frame-bundles-rank-n-vector-bundle-em|frame-bundle descriptions of vector-bundle data]]).

3. **Hopf bundle and the Hopf line bundle.**
   For the [[fiber-bundles/hopf-fibration-s3s2-as-a-principal-u-bundle|Hopf fibration]] $S^3\to S^2$ (a principal $U(1)$-bundle) and $F=\mathbb C$ with the usual left $U(1)$-action by scalar multiplication, the associated bundle $S^3\times_{U(1)}\mathbb C\to S^2$ is the standard nontrivial [[fiber-bundles/complex-vector-bundle|complex line bundle]] over $S^2$.
