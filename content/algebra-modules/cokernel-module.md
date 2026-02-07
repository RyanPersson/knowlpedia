---
title: "Cokernel"
description: "The quotient of the codomain by the image of a module homomorphism."
---

Let $f:M\to N$ be a {{< knowl id="module-homomorphism" text="module homomorphism" >}}. The **cokernel** of $f$ is the {{< knowl id="quotient-module" text="quotient module" >}}
\[
\operatorname{coker}(f)=N/\operatorname{im}(f),
\]
where $\operatorname{im}(f)$ is the {{< knowl id="image-module" text="image" >}} of $f$. It comes with a canonical surjection $N\to \operatorname{coker}(f)$, and one always has an exact tail
\[
M \xrightarrow{\,f\,} N \to \operatorname{coker}(f) \to 0.
\]

Cokernels are the natural “targets” that make maps surjective by force, dual to how kernels make maps injective by force.

**Examples:**
- For $f:\mathbb Z\to\mathbb Z$ given by $f(n)=kn$ with $k\ne 0$, one has $\operatorname{coker}(f)\cong \mathbb Z/k\mathbb Z$.
- If $i:N\hookrightarrow M$ is the inclusion of a submodule, then $\operatorname{coker}(i)\cong M/N$.
- (Edge case) If $f$ is surjective, then $\operatorname{coker}(f)=0$.
