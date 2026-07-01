+++
id = "algebra-modules/projective-module"
title = "Projective module"
kind = "knowl"
summary = "A module with the lifting property against surjections; equivalently, a direct summand of a free module."
aliases = ["projective-module", "Projective module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/projective-module.md"
+++

An $R$-module $P$ is **projective** if for every [[shared-foundations/surjective-function|surjective]] homomorphism $f:M\to N$ and every homomorphism $g:P\to N$ (see [[algebra-modules/module-homomorphism|module homomorphisms]]), there exists a homomorphism $h:P\to M$ such that $f\circ h=g$.

Equivalently, $P$ is projective iff it is a direct summand of a [[algebra-modules/free-module|free module]]; see [[algebra-modules/projective-summand-of-free|projective is a summand of free]]. Projectivity can also be detected via splitting of short exact sequences ending in $P$ (a standard criterion is [[algebra-modules/projective-ses-criterion|the projective short-exact-sequence criterion]]), linking it to [[algebra-modules/short-exact-sequence|short exact sequences]].

**Examples:**
- Every free module is projective (take lifts coordinatewise).
- Any direct summand of a free module (e.g. $R^n \cong P\oplus Q$) is projective.
- (Nonexample) As a $\mathbb Z$-module, $\mathbb Z/n\mathbb Z$ is not projective for $n>1$.
