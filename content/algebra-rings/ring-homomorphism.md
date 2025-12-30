---
title: "Ring homomorphism"
description: "A function between rings preserving addition and multiplication."
---

A **ring homomorphism** is a {{< knowl id="function" text="function" >}} $\varphi:R\to S$ between {{< knowl id="ring" text="rings" >}} such that for all $a,b\in R$,
\[
\varphi(a+b)=\varphi(a)+\varphi(b),\qquad \varphi(ab)=\varphi(a)\varphi(b).
\]
If $R,S$ are unital, one often additionally requires $\varphi(1_R)=1_S$ (a *unital* homomorphism).

Homomorphisms organize rings into a category; they compose via {{< knowl id="composition" text="composition" >}}. Two fundamental invariants are the {{< knowl id="kernel-ring" text="kernel" >}} and image, which control quotients and embeddings.

**Examples:**
- The reduction map $\mathbb Z\to \mathbb Z/n\mathbb Z$, $a\mapsto \overline a$, is a ring homomorphism.
- The inclusion $\mathbb Z\hookrightarrow \mathbb Q$ is a ring homomorphism.
- Evaluation at $c\in k$ gives a homomorphism $k[x]\to k$, $f\mapsto f(c)$.