---
title: "Projective module"
description: "A module with the lifting property against surjections; equivalently, a direct summand of a free module."
---

An $R$-module $P$ is **projective** if for every {{< knowl id="surjective-function" text="surjective" >}} homomorphism $f:M\to N$ and every homomorphism $g:P\to N$ (see {{< knowl id="module-homomorphism" text="module homomorphisms" >}}), there exists a homomorphism $h:P\to M$ such that $f\circ h=g$.

Equivalently, $P$ is projective iff it is a direct summand of a {{< knowl id="free-module" text="free module" >}}; see {{< knowl id="projective-summand-of-free" text="projective is a summand of free" >}}. Projectivity can also be detected via splitting of short exact sequences ending in $P$ (a standard criterion is {{< knowl id="projective-ses-criterion" text="the projective short-exact-sequence criterion" >}}), linking it to {{< knowl id="short-exact-sequence" text="short exact sequences" >}}.

**Examples:**
- Every free module is projective (take lifts coordinatewise).
- Any direct summand of a free module (e.g. $R^n \cong P\oplus Q$) is projective.
- (Nonexample) As a $\mathbb Z$-module, $\mathbb Z/n\mathbb Z$ is not projective for $n>1$.
