---
title: "Free module universal property"
description: "A free module on a set represents functions out of that set by unique linear extension."
---

**Free module universal property**: Let $X$ be a set and let $F$ be a free $R$-module on $X$, equipped with a function $\eta:X\to F$. For any $R$-module $M$ and any function $g:X\to M$, there exists a unique $R$-module homomorphism $\tilde g:F\to M$ such that $\tilde g\circ \eta=g$.

This universal property characterizes {{< knowl id="free-module" text="free modules" >}} as the “linearizations” of {{< knowl id="set" section="shared-foundations" text="sets" >}}, turning {{< knowl id="function" section="shared-foundations" text="functions" >}} into {{< knowl id="module-homomorphism" text="module homomorphisms" >}} by unique extension.
