---
title: "Bounded Operator on a Hilbert Space"
description: "A linear operator whose action does not increase vector norms by more than a fixed constant; equivalently, a continuous linear map."
---

Let \(H\) be a (complex) Hilbert space. A linear operator \(A:H\to H\) is **bounded** if there exists a constant \(C\ge 0\) such that
\[
\|Ax\|\le C\|x\| \quad \text{for all } x\in H.
\]
The smallest such constant is the **operator norm**
\[
\|A\| := \sup_{\|x\|=1}\|Ax\|.
\]

Bounded operators are the standard class of operators used to model physical transformations and observables in many finite-dimensional quantum settings.

## Equivalent characterizations
For linear maps between normed vector spaces (in particular, Hilbert spaces), the following are equivalent:

- \(A\) is bounded.
- \(A\) is continuous (everywhere).
- \(A\) is continuous at \(0\).

In finite dimension (e.g. on a {{< knowl id="complex-hilbert-space-finite" text="complex Hilbert space" >}}), **every** {{< knowl id="linear-map" section="linear-algebra" text="linear operator" >}} is bounded.

## Adjoint and basic properties
If \(A\) is bounded on a Hilbert space, then there exists a unique bounded **adjoint** \(A^\ast\) such that
\[
\langle x,Ay\rangle = \langle A^\ast x,y\rangle \quad \text{for all } x,y\in H.
\]
Key norm identities/inequalities:

- \(\|A^\ast\|=\|A\|\).
- \(\|AB\|\le \|A\|\,\|B\|\).
- \(\|A\|^2 = \|A^\ast A\|\).

An operator \(A\) is {{< knowl id="self-adjoint-operator-observable" text="self-adjoint" >}} when \(A=A^\ast\).

## Example (matrices)
On \(H=\mathbb{C}^n\), every matrix \(A\in \mathbb{C}^{n\times n}\) defines a bounded operator, and \(\|A\|\) is the induced norm
\[
\|A\|=\sup_{x\ne 0}\frac{\|Ax\|_2}{\|x\|_2},
\]
equal to the largest singular value of \(A\).
