+++
id = "fiber-bundles/tfae-reduction-of-structure-group-to-hg-principal-g-bundle-pm"
title = "Equivalent conditions for reduction of structure group"
kind = "knowl"
summary = "Reduction of a principal G bundle to a subgroup H is equivalent to an H subbundle, H valued transition functions, or a section of the G mod H bundle."
aliases = ["tfae-reduction-of-structure-group-to-hg-principal-g-bundle-pm", "Equivalent conditions for reduction of structure group"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/tfae-reduction-of-structure-group-to-hg-principal-g-bundle-pm.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $G$, and let $H\subset G$ be a Lie subgroup (see [[lie-groups/lie-subgroup|Lie subgroup]]). A **reduction of structure group to $H$** means, informally, that $P$ can be described using $H$ as the structure group instead of $G$ (see [[fiber-bundles/reduction-of-structure-group|reduction of structure group]]).

## Theorem (TFAE: reduction to H)
The following are equivalent:

1. (**Principal H-subbundle**)
   There exists a [[fiber-bundles/principal-h-subbundle|principal H-subbundle]] $Q\subset P$ such that $Q\to M$ is a principal $H$-bundle and the inclusion $Q\hookrightarrow P$ is $H$-equivariant (with $H$ acting on $P$ through the inclusion $H\subset G$).

2. (**Associated bundle model**)
   There exists a principal $H$-bundle $Q\to M$ such that $P$ is isomorphic (as a principal $G$-bundle) to the extension of structure group
   \[
   P \cong Q\times_H G
   \]
   (compare [[fiber-bundles/extension-of-structure-group|extension of structure group]]).

3. (**H-valued transition functions**)
   There exists a bundle atlas for $P$ whose transition functions take values in $H\subset G$. Equivalently, the cocycle of transition functions is represented by an $H$-valued cocycle (see [[fiber-bundles/principal-bundle-transition-function|principal bundle transition functions]] and [[fiber-bundles/reduction-by-cocycle-structure-group-reduces-to-h-iff-transition-functions-can-be-chosen-h-valued|reduction by cocycle]]). This is the transition-function viewpoint used in [[fiber-bundles/construction-reduction-of-structure-group-to-h-via-transition-functions-valued-in-h|constructing reductions via H-valued transition functions]].

4. (**Section of the coset bundle**)
   Let $G$ act on the homogeneous space $G/H$ by left translation. Form the associated bundle
   \[
   P/H \;:=\; P\times_G (G/H),
   \]
   sometimes called the bundle of cosets (compare [[fiber-bundles/bundle-of-orbits|bundle of orbits]] in the special case of homogeneous fibers). Then $P$ admits a reduction of structure group to $H$ if and only if $P/H\to M$ admits a smooth global section.

In (4), given a reduction $Q\subset P$, the corresponding section of $P/H$ sends $x\in M$ to the coset represented by any $q\in Q_x$. Conversely, a section selects an $H$-orbit in each fiber of $P$, and its preimage defines the reduced subbundle $Q$.

## Examples
1. **Riemannian metric reduces GL(n) to O(n).**
   Let $E\to M$ be a rank-$n$ real vector bundle with frame bundle $\mathrm{Fr}(E)$ (see [[fiber-bundles/frame-bundle-frame-bundle-of-a-rank-n-vector-bundle|frame bundle]]). A [[fiber-bundles/bundle-metric|bundle metric]] on $E$ is equivalent to a reduction of $\mathrm{Fr}(E)$ from $GL(n)$ to $O(n)$, whose reduced bundle is the orthonormal frame bundle (see [[fiber-bundles/orthonormal-frame-bundle-reduction-of-the-frame-bundle|orthonormal frame bundle reduction]] and [[fiber-bundles/example-reduction-of-gl-structure-to-o-using-a-bundle-metric|metric reduction example]]).

2. **Orientation reduces GL(n) to GL+(n).**
   An [[fiber-bundles/orientation-of-a-real-vector-bundle|orientation of a real vector bundle]] is equivalent to a reduction of the structure group from $GL(n)$ to the identity component $GL^+(n)$. In transition-function terms, this means one can choose local frames so that all transition matrices have positive determinant.

3. **Unitary to special unitary reduction.**
   For a complex Hermitian vector bundle, the unitary frame bundle gives a reduction to $U(n)$ (see [[fiber-bundles/unitary-frame-bundle-reduction|unitary frame bundle reduction]]). A further reduction to $SU(n)$ corresponds to choosing a trivialization of the determinant bundle compatible with the Hermitian structure, producing the [[fiber-bundles/special-unitary-frame-bundle-reduction|special unitary frame bundle reduction]].
