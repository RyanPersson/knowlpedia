---
title: "Image of a module homomorphism"
description: "The submodule consisting of all values attained by a module homomorphism."
---

Let $f:M\to N$ be a {{</* knowl id="module-homomorphism" text="module homomorphism" */>}}. The **image** of $f$ is
\[
\operatorname{im}(f)=\{f(m): m\in M\}\subseteq N.
\]
It is a {{</* knowl id="submodule" text="submodule" */>}} of $N$; see {{</* knowl id="kernel-image-submodules" text="kernel/image are submodules" */>}} for the standard closure argument.

Images measure surjectivity: $f$ is surjective iff $\operatorname{im}(f)=N$. Together with kernels, images define exactness via the condition $\operatorname{im}(f)=\ker(g)$ for consecutive maps (see {{</* knowl id="exactness-via-kernels-images" text="exactness via kernels and images" */>}}

**Examples:**
- For $f:\mathbb Z\to\mathbb Z$ given by $f(n)=2n$, the image is $2\mathbb Z$.
- For the projection $\pi:R^2\to R$, $\pi(a,b)=a$, the image is all of $R$.
- (Edge case) The image of the zero homomorphism is $\{0\}$.
