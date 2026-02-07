---
title: "Module homomorphism"
description: "A map preserving addition and scalar multiplication between modules."
---

Let $M,N$ be left $R$-{{< knowl id="module" text="modules" >}}. A **module homomorphism** is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:M\to N$ such that for all $m,m'\in M$ and $r\in R$,
\[
f(m+m')=f(m)+f(m') \quad\text{and}\quad f(rm)=r f(m).
\]
Equivalently, $f$ is a group homomorphism on underlying additive groups that is $R$-linear.

Module homomorphisms compose (see {{< knowl id="composition" section="shared-foundations" text="composition" >}}), and their basic invariants are the {{< knowl id="kernel-module" text="kernel" >}} and {{< knowl id="image-module" text="image" >}}, which control exactness and quotients.

**Examples:**
- For the $\mathbb Z$-module $\mathbb Z$, the map $f(n)=kn$ is a module homomorphism for any fixed $k\in\mathbb Z$.
- If $M=R^2$ and $N=R$, the map $f(a,b)=a+rb$ (for fixed $r\in R$) is $R$-linear.
- (Edge case) A ring homomorphism need not be a module homomorphism unless one views the codomain as a module in the appropriate way.
