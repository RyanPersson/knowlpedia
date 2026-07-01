+++
id = "algebra-modules/free-module-universal-property"
title = "Free module universal property"
kind = "knowl"
summary = "A free module on a set represents functions out of that set by unique linear extension."
aliases = ["free-module-universal-property", "Free module universal property"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/free-module-universal-property.md"
+++

**Free module universal property**: Let $X$ be a set and let $F$ be a free $R$-module on $X$, equipped with a function $\eta:X\to F$. For any $R$-module $M$ and any function $g:X\to M$, there exists a unique $R$-module homomorphism $\tilde g:F\to M$ such that $\tilde g\circ \eta=g$.

This universal property characterizes [[algebra-modules/free-module|free modules]] as the “linearizations” of [[shared-foundations/set|sets]], turning [[shared-foundations/function|functions]] into [[algebra-modules/module-homomorphism|module homomorphisms]] by unique extension.
