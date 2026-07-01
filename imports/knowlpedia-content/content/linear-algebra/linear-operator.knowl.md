+++
id = "linear-algebra/linear-operator"
title = "Linear operator"
kind = "knowl"
summary = "A linear map from a vector space to itself."
aliases = ["linear-operator", "Linear operator"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/linear-operator.md"
+++

A **linear operator** is a [[linear-algebra/linear-map|linear map]] $T:V\to V$ on a [[linear-algebra/vector-space|vector space]] $V$.

Because the domain and codomain agree, one can form iterates $T^k$ using [[shared-foundations/composition|composition]]. Linear operators are the objects to which [[linear-algebra/eigenvalue|eigenvalues]], [[linear-algebra/eigenspace|eigenspaces]], and the [[linear-algebra/characteristic-polynomial|characteristic polynomial]] are attached.

**Examples:**
- The identity map $I:V\to V$ given by $I(v)=v$ is a linear operator.
- On $\mathbb{R}^2$, rotation by a fixed angle is a linear operator.
- On $\mathbb{R}[x]$, the differentiation map $p\mapsto p'$ is a linear operator.
