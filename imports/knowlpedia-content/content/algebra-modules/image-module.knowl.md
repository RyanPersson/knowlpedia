+++
id = "algebra-modules/image-module"
title = "Image of a module homomorphism"
kind = "knowl"
summary = "The submodule consisting of all values attained by a module homomorphism."
aliases = ["image-module", "Image of a module homomorphism"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/image-module.md"
+++

Let $f:M\to N$ be a [[algebra-modules/module-homomorphism|module homomorphism]]. The **image** of $f$ is
\[
\operatorname{im}(f)=\{f(m): m\in M\}\subseteq N.
\]
It is a [[algebra-modules/submodule|submodule]] of $N$; see [[algebra-modules/kernel-image-submodules|kernel/image are submodules]] for the standard closure argument.

Images measure surjectivity: $f$ is surjective iff $\operatorname{im}(f)=N$. Together with kernels, images define exactness via the condition $\operatorname{im}(f)=\ker(g)$ for consecutive maps (see [[algebra-modules/exactness-via-kernels-images|exactness via kernels and images]]

**Examples:**
- For $f:\mathbb Z\to\mathbb Z$ given by $f(n)=2n$, the image is $2\mathbb Z$.
- For the projection $\pi:R^2\to R$, $\pi(a,b)=a$, the image is all of $R$.
- (Edge case) The image of the zero homomorphism is $\{0\}$.
