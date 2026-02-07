---
title: "Theorem: A trivial principal bundle admits a global section"
description: "Any principal bundle isomorphic to a product bundle has a canonical global section."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure {{< knowl id="lie-group" text="Lie group" >}} $G$.

## Theorem

If $P$ is trivial, i.e. there exists a principal bundle isomorphism
\[
\Psi:P\xrightarrow{\cong} M\times G,
\]
then $P$ admits a smooth global section. Concretely, if $e\in G$ is the identity, then
\[
s(x):=\Psi^{-1}(x,e)
\]
defines a smooth section $s:M\to P$ with $\pi\circ s=\mathrm{id}_M$.

Equivalently, triviality of $P$ is characterized by the existence of a global section, together with {{< knowl id="trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial" text="the converse implication" >}}.

## Examples

1. **Canonical section of the product.** For $P=M\times G$, the section $x\mapsto (x,e)$ is smooth and globally defined.

2. **Trivializations differ by gauge transformations.** If $\Psi$ and $\Psi'$ are two trivializations, the associated sections differ by right multiplication by a smooth map $M\to G$.

3. **Pullback of a trivial bundle.** If $f:N\to M$ is a {{< knowl id="smooth-map" text="smooth map" >}} and $P\cong M\times G$, then the pullback bundle $f^*P$ is trivial and inherits a global section by pulling back $x\mapsto(x,e)$.
