---
title: "Exactness via kernels and images"
description: "A sequence is exact at a term precisely when the incoming image equals the outgoing kernel."
---

**Exactness via kernels and images**: A sequence of $R$-modules and homomorphisms
\[
\cdots \longrightarrow M_{i-1}\xrightarrow{d_{i-1}} M_i \xrightarrow{d_i} M_{i+1}\longrightarrow \cdots
\]
is exact at $M_i$ if and only if $\operatorname{im}(d_{i-1})=\ker(d_i)$.

This rewrites {{< knowl id="exact-sequence-modules" text="exactness" >}} purely in terms of {{< knowl id="kernel-module" text="kernels" >}} and {{< knowl id="image-module" text="images" >}}, and is used constantly for {{< knowl id="short-exact-sequence" text="short exact sequences" >}}.
