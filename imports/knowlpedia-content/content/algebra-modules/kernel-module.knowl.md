+++
id = "algebra-modules/kernel-module"
title = "Kernel of a module homomorphism"
kind = "knowl"
summary = "The submodule mapped to zero by a module homomorphism."
aliases = ["kernel-module", "Kernel of a module homomorphism"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/kernel-module.md"
+++

Let $f:M\to N$ be a [[algebra-modules/module-homomorphism|module homomorphism]]. The **kernel** of $f$ is
\[
\ker(f)=\{m\in M: f(m)=0\}.
\]
It is a [[algebra-modules/submodule|submodule]], as recorded in [[algebra-modules/kernels-are-submodules|kernels are submodules]].

Kernels measure injectivity: $f$ is injective iff $\ker(f)=0$. They also define the notion of exactness (see [[algebra-modules/exact-sequence-modules|exact sequences]], where kernels match images).

**Examples:**
- For $f:\mathbb Z^2\to\mathbb Z$ given by $f(a,b)=a+b$, one has $\ker(f)=\{(t,-t):t\in\mathbb Z\}$.
- For $f:\mathbb Z\to\mathbb Z$ given by $f(n)=kn$, the kernel is $0$ if $k\ne 0$ and all of $\mathbb Z$ if $k=0$.
- (Edge case) If $N=0$, then $\ker(f)=M$ for every $f:M\to 0$.
