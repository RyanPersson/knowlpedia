---
title: "Exactness properties of Hom and tensor"
description: "Hom is left exact and tensor is right exact; flatness, projectivity, and injectivity are exactly the conditions that make these functors exact."
---

Let \(R\) be a ring and consider the functors on \(R\)-modules:
- \(\operatorname{Hom}_R(M,-)\) (covariant in the second variable),
- \(-\otimes_R N\),
- \(\operatorname{Hom}_R(-,N)\) (contravariant in the first variable).

## Basic exactness statements

### Hom is left exact
For any fixed \(M\), the functor \(\operatorname{Hom}_R(M,-)\) is {{< knowl id="hom-left-exact" text="left exact" >}}:
from a short exact sequence \(0\to A\to B\to C\to 0\) one gets an exact sequence
\[
0 \to \operatorname{Hom}_R(M,A)\to \operatorname{Hom}_R(M,B)\to \operatorname{Hom}_R(M,C),
\]
but surjectivity of \(\operatorname{Hom}_R(M,B)\to \operatorname{Hom}_R(M,C)\) can fail in general.

**Projectivity criterion.** \(\operatorname{Hom}_R(M,-)\) is exact (i.e. also right exact) iff \(M\) is {{< knowl id="projective-module" section="algebra-modules" text="projective" >}}.

### Tensor is right exact
For any fixed \(N\), the functor \(-\otimes_R N\) is {{< knowl id="tensor-right-exact" text="right exact" >}}:
from \(A\to B\to C\to 0\) exact one gets
\[
A\otimes_R N \to B\otimes_R N \to C\otimes_R N \to 0
\]
exact, but injectivity of \(A\otimes_R N\to B\otimes_R N\) can fail.

**Flatness criterion.** \(-\otimes_R N\) is exact (i.e. also left exact) iff \(N\) is {{< knowl id="flat-module" section="algebra-modules" text="flat" >}}.

### Contravariant Hom is left exact (in the contravariant sense)
For fixed \(N\), the functor \(\operatorname{Hom}_R(-,N)\) sends short exact sequences
\(0\to A\to B\to C\to 0\) to exact sequences
\[
0 \to \operatorname{Hom}_R(C,N)\to \operatorname{Hom}_R(B,N)\to \operatorname{Hom}_R(A,N),
\]
again with possible failure of surjectivity on the right.

**Injectivity criterion.** \(\operatorname{Hom}_R(-,N)\) is exact (i.e. also right exact in this contravariant direction) iff \(N\) is {{< knowl id="injective-module" section="algebra-modules" text="injective" >}}.

## Link to Ext and Tor
Because Hom and tensor are only one-sided exact in general, their derived functors measure the obstruction:
- \(\operatorname{Ext}\) are derived from Hom,
- \(\operatorname{Tor}\) are derived from tensor.
See {{< knowl id="ext-tor-derived-functors" text="Ext and Tor as derived functors" >}} and {{< knowl id="ext-tor-derived-functors" text="derived-functor definitions" >}}.

## Examples

### Example 1 (tensor is not left exact over \(\mathbb Z\))
In \(\mathbf{Ab}\), take the injection \(0\to \mathbb Z \xrightarrow{\cdot n} \mathbb Z\).
Tensor with \(\mathbb Z/n\):
\[
\mathbb Z\otimes \mathbb Z/n \xrightarrow{\cdot n} \mathbb Z\otimes \mathbb Z/n
\]
becomes
\[
\mathbb Z/n \xrightarrow{0} \mathbb Z/n,
\]
which is not injective. The “missing” left exactness is measured by
\[
\operatorname{Tor}_1^\mathbb Z(\mathbb Z/n,\mathbb Z/n)\cong \mathbb Z/n
\]
(see {{< knowl id="tor" text="Tor" >}}).

### Example 2 (flat module: \(\mathbb Q\) over \(\mathbb Z\))
The \(\mathbb Z\)-module \(\mathbb Q\) is flat (localization of \(\mathbb Z\)). Hence tensoring any short exact sequence of abelian groups with \(\mathbb Q\) preserves exactness.
In particular,
\[
\operatorname{Tor}_1^\mathbb Z(\mathbb Q, A)=0
\]
for every abelian group \(A\).

### Example 3 (Hom is not right exact unless the source is projective)
Consider the short exact sequence
\[
0\to \mathbb Z \xrightarrow{\cdot n} \mathbb Z \to \mathbb Z/n\to 0.
\]
Apply \(\operatorname{Hom}_\mathbb Z(\mathbb Z/n,-)\). The resulting map
\[
\operatorname{Hom}(\mathbb Z/n,\mathbb Z)\to \operatorname{Hom}(\mathbb Z/n,\mathbb Z/n)
\]
fails to be surjective (indeed \(\operatorname{Hom}(\mathbb Z/n,\mathbb Z)=0\), while \(\operatorname{Hom}(\mathbb Z/n,\mathbb Z/n)\cong \mathbb Z/n\)).
The obstruction is exactly
\[
\operatorname{Ext}^1_\mathbb Z(\mathbb Z/n,\mathbb Z)\cong \mathbb Z/n,
\]
illustrating that \(\mathbb Z/n\) is not projective over \(\mathbb Z\) (see {{< knowl id="ext" text="Ext" >}}).
