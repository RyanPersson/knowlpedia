---
title: "Rational canonical form from the structure theorem"
description: "Rational canonical form arises by viewing (V,T) as a module over F[x] and applying the PID structure theorem."
---

**Rational canonical form from the structure theorem**: Let $V$ be a finite-dimensional vector space over a field $F$ and let $T:V\to V$ be linear. Then there exists a basis of $V$ for which the matrix of $T$ is in rational canonical form; equivalently, viewing $V$ as an $F[x]$-module via $x\cdot v = T(v)$, there is an isomorphism
\[
V \cong \bigoplus_{j=1}^k F[x]/(f_j(x))
\]
with monic polynomials $f_1\mid f_2\mid\cdots\mid f_k$ (the invariant factors of $T$).

This is an application of the {{< knowl id="structure-theorem-pid" text="structure theorem over a PID" >}} to the {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial ring" >}} $F[x]$ (with $F$ a {{< knowl id="field" section="algebra-rings" text="field" >}}), after encoding a {{< knowl id="linear-map" section="analysis" text="linear map" >}} on a {{< knowl id="vector-space" section="shared-linear-algebra" text="vector space" >}} as a {{< knowl id="module" text="module" >}} structure; see {{< knowl id="rational-canonical-form-theorem" text="rational canonical form theorem" >}}.
