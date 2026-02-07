---
title: "Linear operator"
description: "A linear map from a vector space to itself."
---

A **linear operator** is a {{< knowl id="linear-map" text="linear map" >}} $T:V\to V$ on a {{< knowl id="vector-space" text="vector space" >}} $V$.

Because the domain and codomain agree, one can form iterates $T^k$ using {{< knowl id="composition" section="shared-foundations" text="composition" >}}. Linear operators are the objects to which {{< knowl id="eigenvalue" text="eigenvalues" >}}, {{< knowl id="eigenspace" text="eigenspaces" >}}, and the {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}} are attached.

**Examples:**
- The identity map $I:V\to V$ given by $I(v)=v$ is a linear operator.
- On $\mathbb{R}^2$, rotation by a fixed angle is a linear operator.
- On $\mathbb{R}[x]$, the differentiation map $p\mapsto p'$ is a linear operator.
