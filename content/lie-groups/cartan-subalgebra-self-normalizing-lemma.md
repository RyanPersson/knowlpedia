---
title: "Cartan subalgebras are self-normalizing"
description: "If h is a Cartan subalgebra, then its normalizer in g equals h."
---

Let $\mathfrak{g}$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}} over an algebraically closed field of characteristic $0$, and let $\mathfrak{h}\subset \mathfrak{g}$ be a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}.

**Lemma.** The normalizer of $\mathfrak{h}$ in $\mathfrak{g}$ is $\mathfrak{h}$ itself:
$$
N_{\mathfrak{g}}(\mathfrak{h})=\{X\in\mathfrak{g}:[X,\mathfrak{h}]\subset \mathfrak{h}\}=\mathfrak{h}.
$$

Equivalently, if $X\in\mathfrak{g}$ satisfies $[X,H]\in \mathfrak{h}$ for every $H\in\mathfrak{h}$, then $X\in \mathfrak{h}$.

**Context.** This property ensures that $\mathfrak{h}$ is as large as possible among nilpotent subalgebras compatible with its own adjoint action: anything that stabilizes $\mathfrak{h}$ by commutators is already inside $\mathfrak{h}$. In semisimple Lie theory, self-normalizing is what makes the {{< knowl id="root-space-decomposition" text="root decomposition" >}} relative to $\mathfrak{h}$ behave rigidly, and it underlies the definition of the {{< knowl id="weyl-group" text="Weyl group" >}} as a quotient of a group normalizer by a centralizer.
