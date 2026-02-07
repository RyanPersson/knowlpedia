---
title: "Simple root"
description: "A minimal positive root; simple roots form a basis for the root system and generate all positive roots."
---

Fix a root system $\Phi\subset V$ (see {{< knowl id="root-system" text="root system" >}}) together with a choice of {{< knowl id="positive-root" text="positive roots" >}} $\Phi^+\subset\Phi$.

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

In semisimple Lie theory (see {{< knowl id="root-lie-algebra" text="roots of a Lie algebra" >}} and {{< knowl id="root-space-decomposition" text="root space decomposition" >}}), choosing $\Delta$ is the combinatorial input for building the {{< knowl id="cartan-matrix" text="Cartan matrix" >}} and {{< knowl id="dynkin-diagram" text="Dynkin diagram" >}}. In representation theory, simple roots control highest weights (see {{< knowl id="highest-weight" text="highest weight" >}} and {{< knowl id="highest-weight-theorem" text="highest weight theorem" >}}).
