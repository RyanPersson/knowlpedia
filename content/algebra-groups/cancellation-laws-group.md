---
title: "Cancellation laws"
description: "Left and right cancellation hold in every group"
---

**Proposition (Cancellation laws).**
Let $G$ be a {{< knowl id="group" text="group" >}} and let $a,b,c\in G$.

- (**Left cancellation**) If $ab=ac$, then $b=c$.
- (**Right cancellation**) If $ba=ca$, then $b=c$.

Equivalently, for each fixed $a\in G$, the left-translation map $L_a:G\to G$, $L_a(x)=ax$, and the right-translation map $R_a:G\to G$, $R_a(x)=xa$, are injective.

**Context.**
Cancellation is the algebraic shadow of invertibility: you "cancel" by multiplying by $a^{-1}$ on the appropriate side. Uniqueness of inverses (see {{< knowl id="uniqueness-of-inverses-group" text="uniqueness of inverses" >}}) ensures $a^{-1}$ is well-defined.

**Proof sketch.**
If $ab=ac$, multiply on the left by $a^{-1}$ to get $b=c$. The right cancellation law is analogous.
