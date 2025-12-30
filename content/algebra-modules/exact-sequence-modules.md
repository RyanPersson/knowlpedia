---
title: "Exact sequence of modules"
description: "A sequence of module homomorphisms where each image equals the next kernel."
---

An **exact sequence of modules** is a sequence of modules and {{< knowl id="module-homomorphism" text="module homomorphisms" >}}
\[
\cdots \to M_{i-1}\xrightarrow{d_{i-1}} M_i \xrightarrow{d_i} M_{i+1}\to \cdots
\]
such that for every $i$ one has $\operatorname{im}(d_{i-1})=\ker(d_i)$, where the kernel and image are taken in the sense of {{< knowl id="kernel-module" text="kernels" >}} and {{< knowl id="image-module" text="images" >}}. A convenient checklist formulation is given in {{< knowl id="exactness-via-kernels-images" text="exactness via kernels/images" >}}.

Exact sequences package algebraic information: injectivity, surjectivity, quotients, and splitting phenomena are all phrased as exactness conditions.

**Examples:**
- For a submodule $N\le M$, the sequence $0\to N\to M\to M/N\to 0$ is exact.
- The sequence $0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0$ is exact for $n\ne 0$.
- (Edge case) The sequence $M\xrightarrow{\mathrm{id}} M\to 0$ is exact, but $0\to M\xrightarrow{0} M$ is not exact unless $M=0$.
