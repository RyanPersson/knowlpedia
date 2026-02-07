---
title: "Reduction of structure group via H-valued transition functions"
description: "Constructing a principal H-subbundle when transition functions take values in a subgroup H."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. Fix an open cover $\{U_i\}$ of $M$ and smooth local sections $s_i:U_i\to P$. Let
\[
g_{ij}:U_i\cap U_j \to G
\]
be the transition functions determined by the $s_i$, as in {{< knowl id="construction-transition-functions-g-iju-iu-jg-from-local-sections" text="constructing transition functions from local sections" >}}.

Let $H\subset G$ be a {{< knowl id="lie-subgroup" text="Lie subgroup" section="lie-groups">}}.

## Construction (reduction from H-valued transitions)
Assume that for all $i,j$ and all $x\in U_i\cap U_j$ we have
\[
g_{ij}(x)\in H.
\]
Define a subset $Q\subset P$ by specifying it locally on each $U_i$:
\[
Q|_{U_i} := s_i(U_i)\cdot H \;\subset\; P|_{U_i}.
\]
Here $s_i(U_i)\cdot H$ means all points of the form $s_i(x)\cdot h$ with $x\in U_i$ and $h\in H$.

### Compatibility on overlaps
On $U_i\cap U_j$, we have $s_j(x)=s_i(x)\cdot g_{ij}(x)$ and by assumption $g_{ij}(x)\in H$. Hence
\[
s_j(x)\cdot H = s_i(x)\cdot g_{ij}(x)\cdot H = s_i(x)\cdot H,
\]
so the locally defined subsets glue to a global smooth submanifold $Q\subset P$.

### Result
The glued space $Q$ is a {{< knowl id="principal-h-subbundle" text="principal H-subbundle" >}} of $P$, i.e. a principal $H$-bundle over $M$ together with an $H$-equivariant inclusion $Q\hookrightarrow P$ covering the identity on $M$. Equivalently, $P$ is obtained from $Q$ by {{< knowl id="extension-of-structure-group" text="extending the structure group" >}} along $H\hookrightarrow G$:
\[
Q\times_H G \;\cong\; P.
\]
This is a concrete realization of {{< knowl id="reduction-of-structure-group" text="reduction of structure group" >}}, and it matches the criterion in {{< knowl id="reduction-by-cocycle-structure-group-reduces-to-h-iff-transition-functions-can-be-chosen-h-valued" text="reduction via H-valued transition functions" >}}.

## Examples
1. **Metric reduction $GL(n)\to O(n)$.** If a rank-$n$ real vector bundle has a {{< knowl id="bundle-metric" text="bundle metric" >}}, one can choose local orthonormal frames so that all transition matrices lie in $O(n)$. Applying the construction yields the orthonormal frame bundle, as in {{< knowl id="orthonormal-frame-bundle-reduction-of-the-frame-bundle" text="the orthonormal frame bundle reduction" >}} (see also {{< knowl id="example-reduction-of-gl-structure-to-o-using-a-bundle-metric" text="reduction of GL structure to O using a bundle metric" >}}).

2. **Hermitian reduction $GL(n,\mathbb C)\to U(n)$.** A {{< knowl id="hermitian-metric" text="Hermitian metric" >}} on a complex rank-$n$ vector bundle allows local unitary frames, so the transition functions are $U(n)$-valued. The resulting principal $U(n)$-subbundle is the {{< knowl id="unitary-frame-bundle-reduction" text="unitary frame bundle reduction" >}}.

3. **Oriented Riemannian reduction to $SO(n)$.** If the bundle is both oriented ({{< knowl id="orientation-of-a-real-vector-bundle" text="orientation" >}}) and metric, then one can choose local oriented orthonormal frames, forcing transitions to lie in $SO(n)$. The construction produces the {{< knowl id="special-orthonormal-frame-bundle-reduction" text="special orthonormal frame bundle" >}}.
