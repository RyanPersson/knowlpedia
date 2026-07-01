+++
id = "algebra-modules/rcf-from-structure-theorem"
title = "Rational canonical form from the structure theorem"
kind = "knowl"
summary = "Rational canonical form arises by viewing (V,T) as a module over F[x] and applying the PID structure theorem."
aliases = ["rcf-from-structure-theorem", "Rational canonical form from the structure theorem"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/rcf-from-structure-theorem.md"
+++

**Rational canonical form from the structure theorem**: Let $V$ be a finite-dimensional vector space over a field $F$ and let $T:V\to V$ be linear. Then there exists a basis of $V$ for which the matrix of $T$ is in rational canonical form; equivalently, viewing $V$ as an $F[x]$-module via $x\cdot v = T(v)$, there is an isomorphism
\[
V \cong \bigoplus_{j=1}^k F[x]/(f_j(x))
\]
with monic polynomials $f_1\mid f_2\mid\cdots\mid f_k$ (the invariant factors of $T$).

This is an application of the [[algebra-modules/structure-theorem-pid|structure theorem over a PID]] to the [[algebra-rings/polynomial-ring|polynomial ring]] $F[x]$ (with $F$ a [[algebra-rings/field|field]]), after encoding a [[linear-algebra/linear-map|linear map]] on a [[linear-algebra/vector-space|vector space]] as a [[algebra-modules/module|module]] structure; see [[algebra-modules/rational-canonical-form-theorem|rational canonical form theorem]].
