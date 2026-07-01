+++
id = "lie-groups/simple-root"
title = "Simple root"
kind = "knowl"
summary = "A minimal positive root; simple roots form a basis for the root system and generate all positive roots."
aliases = ["simple-root", "Simple root"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/simple-root.md"
+++

Fix a root system $\Phi\subset V$ (see [[lie-groups/root-system|root system]]) together with a choice of [[lie-groups/positive-root|positive roots]] $\Phi^+\subset\Phi$.

A root $\alpha\in\Phi^+$ is called **simple** if it cannot be written as a sum of two positive roots:
\[
\alpha \neq \beta+\gamma \quad\text{for all }\beta,\gamma\in\Phi^+.
\]
The set of simple roots is usually denoted $\Delta\subset\Phi^+$.

Key structural facts (standard in root system theory):

- $\Delta$ is a basis of $V$ (in particular, the simple roots are linearly independent).
- Every positive root is a nonnegative integer combination of simple roots:
  \[
  \Phi^+ \subset \Big\{\sum_{\alpha\in\Delta} n_\alpha\,\alpha \;:\; n_\alpha\in\mathbb Z_{\ge 0}\Big\}.
  \]

In semisimple Lie theory (see [[lie-groups/root-lie-algebra|roots of a Lie algebra]] and [[lie-groups/root-space-decomposition|root space decomposition]]), choosing $\Delta$ is the combinatorial input for building the [[lie-groups/cartan-matrix|Cartan matrix]] and [[lie-groups/dynkin-diagram|Dynkin diagram]]. In representation theory, simple roots control highest weights (see [[lie-groups/highest-weight|highest weight]] and [[lie-groups/highest-weight-theorem|highest weight theorem]]).
