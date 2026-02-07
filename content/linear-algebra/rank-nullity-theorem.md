---
title: "Rank–nullity theorem"
description: "For a linear map on a finite-dimensional space, dimension equals rank plus nullity."
---

**Rank–nullity theorem:** Let $T:V\to W$ be a {{< knowl id="linear-map" text="linear map" >}} between finite-dimensional {{< knowl id="vector-space" text="vector spaces" >}}. Define
\[
\ker T=\{v\in V:T(v)=0\},\qquad \operatorname{im}T=\{T(v):v\in V\}.
\]
Then
\[
\dim V=\dim(\ker T)+\dim(\operatorname{im}T).
\]
In particular, the rank $\operatorname{rank}(T)=\dim(\operatorname{im}T)$ and the nullity $\operatorname{nullity}(T)=\dim(\ker T)$ satisfy $\dim V=\operatorname{rank}(T)+\operatorname{nullity}(T)$.

The set $\operatorname{im}T$ is the {{< knowl id="image" section="shared-foundations" text="image" >}} of the underlying function, and $\ker T$ is the {{< knowl id="preimage" section="shared-foundations" text="preimage" >}} of $\{0\}$. This identity is the basic dimension bookkeeping behind the structure of solution spaces to linear equations.
