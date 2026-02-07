---
title: "Equivalent conditions for reduction of structure group"
description: "Reduction of a principal G bundle to a subgroup H is equivalent to an H subbundle, H valued transition functions, or a section of the G mod H bundle."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $G$, and let $H\subset G$ be a Lie subgroup (see {{< knowl id="lie-subgroup" text="Lie subgroup" section="lie-groups">}}). A **reduction of structure group to $H$** means, informally, that $P$ can be described using $H$ as the structure group instead of $G$ (see {{< knowl id="reduction-of-structure-group" text="reduction of structure group" >}}).

## Theorem (TFAE: reduction to H)
The following are equivalent:

1. (**Principal H-subbundle**)  
   There exists a {{< knowl id="principal-h-subbundle" text="principal H-subbundle" >}} $Q\subset P$ such that $Q\to M$ is a principal $H$-bundle and the inclusion $Q\hookrightarrow P$ is $H$-equivariant (with $H$ acting on $P$ through the inclusion $H\subset G$).

2. (**Associated bundle model**)  
   There exists a principal $H$-bundle $Q\to M$ such that $P$ is isomorphic (as a principal $G$-bundle) to the extension of structure group
   \[
   P \cong Q\times_H G
   \]
   (compare {{< knowl id="extension-of-structure-group" text="extension of structure group" >}}).

3. (**H-valued transition functions**)  
   There exists a bundle atlas for $P$ whose transition functions take values in $H\subset G$. Equivalently, the cocycle of transition functions is represented by an $H$-valued cocycle (see {{< knowl id="principal-bundle-transition-function" text="principal bundle transition functions" >}} and {{< knowl id="reduction-by-cocycle-structure-group-reduces-to-h-iff-transition-functions-can-be-chosen-h-valued" text="reduction by cocycle" >}}). This is the transition-function viewpoint used in {{< knowl id="construction-reduction-of-structure-group-to-h-via-transition-functions-valued-in-h" text="constructing reductions via H-valued transition functions" >}}.

4. (**Section of the coset bundle**)  
   Let $G$ act on the homogeneous space $G/H$ by left translation. Form the associated bundle
   \[
   P/H \;:=\; P\times_G (G/H),
   \]
   sometimes called the bundle of cosets (compare {{< knowl id="bundle-of-orbits" text="bundle of orbits" >}} in the special case of homogeneous fibers). Then $P$ admits a reduction of structure group to $H$ if and only if $P/H\to M$ admits a smooth global section.

In (4), given a reduction $Q\subset P$, the corresponding section of $P/H$ sends $x\in M$ to the coset represented by any $q\in Q_x$. Conversely, a section selects an $H$-orbit in each fiber of $P$, and its preimage defines the reduced subbundle $Q$.

## Examples
1. **Riemannian metric reduces GL(n) to O(n).**  
   Let $E\to M$ be a rank-$n$ real vector bundle with frame bundle $\mathrm{Fr}(E)$ (see {{< knowl id="frame-bundle-frame-bundle-of-a-rank-n-vector-bundle" text="frame bundle" >}}). A {{< knowl id="bundle-metric" text="bundle metric" >}} on $E$ is equivalent to a reduction of $\mathrm{Fr}(E)$ from $GL(n)$ to $O(n)$, whose reduced bundle is the orthonormal frame bundle (see {{< knowl id="orthonormal-frame-bundle-reduction-of-the-frame-bundle" text="orthonormal frame bundle reduction" >}} and {{< knowl id="example-reduction-of-gl-structure-to-o-using-a-bundle-metric" text="metric reduction example" >}}).

2. **Orientation reduces GL(n) to GL+(n).**  
   An {{< knowl id="orientation-of-a-real-vector-bundle" text="orientation of a real vector bundle" >}} is equivalent to a reduction of the structure group from $GL(n)$ to the identity component $GL^+(n)$. In transition-function terms, this means one can choose local frames so that all transition matrices have positive determinant.

3. **Unitary to special unitary reduction.**  
   For a complex Hermitian vector bundle, the unitary frame bundle gives a reduction to $U(n)$ (see {{< knowl id="unitary-frame-bundle-reduction" text="unitary frame bundle reduction" >}}). A further reduction to $SU(n)$ corresponds to choosing a trivialization of the determinant bundle compatible with the Hermitian structure, producing the {{< knowl id="special-unitary-frame-bundle-reduction" text="special unitary frame bundle reduction" >}}.
