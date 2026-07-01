+++
id = "fiber-bundles/converse-triviality-criterion-trivial-principal-bundle-admits-a-global-section"
title = "Theorem: A trivial principal bundle admits a global section"
kind = "knowl"
summary = "Any principal bundle isomorphic to a product bundle has a canonical global section."
aliases = ["converse-triviality-criterion-trivial-principal-bundle-admits-a-global-section", "Theorem: A trivial principal bundle admits a global section"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/converse-triviality-criterion-trivial-principal-bundle-admits-a-global-section.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure [[fiber-bundles/lie-group|Lie group]] $G$.

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

Equivalently, triviality of $P$ is characterized by the existence of a global section, together with [[fiber-bundles/trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial|the converse implication]].

## Examples

1. **Canonical section of the product.** For $P=M\times G$, the section $x\mapsto (x,e)$ is smooth and globally defined.

2. **Trivializations differ by gauge transformations.** If $\Psi$ and $\Psi'$ are two trivializations, the associated sections differ by right multiplication by a smooth map $M\to G$.

3. **Pullback of a trivial bundle.** If $f:N\to M$ is a [[fiber-bundles/smooth-map|smooth map]] and $P\cong M\times G$, then the pullback bundle $f^*P$ is trivial and inherits a global section by pulling back $x\mapsto(x,e)$.
