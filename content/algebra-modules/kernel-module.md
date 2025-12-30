---
title: "Kernel of a module homomorphism"
description: "The submodule mapped to zero by a module homomorphism."
---

Let $f:M\to N$ be a {{</* knowl id="module-homomorphism" text="module homomorphism" */>}}. The **kernel** of $f$ is
\[
\ker(f)=\{m\in M: f(m)=0\}.
\]
It is a {{</* knowl id="submodule" text="submodule" */>}}, as recorded in {{</* knowl id="kernels-are-submodules" text="kernels are submodules" */>}}.

Kernels measure injectivity: $f$ is injective iff $\ker(f)=0$. They also define the notion of exactness (see {{</* knowl id="exact-sequence-modules" text="exact sequences" */>}}, where kernels match images).

**Examples:**
- For $f:\mathbb Z^2\to\mathbb Z$ given by $f(a,b)=a+b$, one has $\ker(f)=\{(t,-t):t\in\mathbb Z\}$.
- For $f:\mathbb Z\to\mathbb Z$ given by $f(n)=kn$, the kernel is $0$ if $k\ne 0$ and all of $\mathbb Z$ if $k=0$.
- (Edge case) If $N=0$, then $\ker(f)=M$ for every $f:M\to 0$.
