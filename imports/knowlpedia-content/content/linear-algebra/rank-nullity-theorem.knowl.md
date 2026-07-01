+++
id = "linear-algebra/rank-nullity-theorem"
title = "Rank–nullity theorem"
kind = "knowl"
summary = "For a linear map on a finite-dimensional space, dimension equals rank plus nullity."
aliases = ["rank-nullity-theorem", "Rank–nullity theorem"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/rank-nullity-theorem.md"
+++

**Rank–nullity theorem:** Let $T:V\to W$ be a [[linear-algebra/linear-map|linear map]] between finite-dimensional [[linear-algebra/vector-space|vector spaces]]. Define
\[
\ker T=\{v\in V:T(v)=0\},\qquad \operatorname{im}T=\{T(v):v\in V\}.
\]
Then
\[
\dim V=\dim(\ker T)+\dim(\operatorname{im}T).
\]
In particular, the rank $\operatorname{rank}(T)=\dim(\operatorname{im}T)$ and the nullity $\operatorname{nullity}(T)=\dim(\ker T)$ satisfy $\dim V=\operatorname{rank}(T)+\operatorname{nullity}(T)$.

The set $\operatorname{im}T$ is the [[shared-foundations/image|image]] of the underlying function, and $\ker T$ is the [[shared-foundations/preimage|preimage]] of $\{0\}$. This identity is the basic dimension bookkeeping behind the structure of solution spaces to linear equations.
