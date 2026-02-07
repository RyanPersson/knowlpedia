---
title: "Cartan subalgebra"
description: "A maximal nilpotent, self-normalizing subalgebra; in the semisimple case, a maximal toral subalgebra."
---

Let $\mathfrak{g}$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}} over an algebraically closed field of characteristic $0$ (typically $\mathbb{C}$).

**Definition.** A subalgebra $\mathfrak{h}\subset \mathfrak{g}$ is a **Cartan subalgebra** if:
1. $\mathfrak{h}$ is {{< knowl id="nilpotent-lie-algebra" text="nilpotent" >}} as a Lie algebra, and
2. $\mathfrak{h}$ is self-normalizing in $\mathfrak{g}$, i.e. $N_{\mathfrak{g}}(\mathfrak{h})=\mathfrak{h}$ (compare {{< knowl id="cartan-subalgebra-self-normalizing-lemma" text="the self-normalizing lemma" >}}).

Here $N_{\mathfrak{g}}(\mathfrak{h})=\{X\in\mathfrak{g}:[X,\mathfrak{h}]\subset \mathfrak{h}\}$ is the normalizer Lie subalgebra.

**Semisimple refinement.** If $\mathfrak{g}$ is {{< knowl id="semisimple-lie-algebra" text="semisimple" >}}, Cartan subalgebras can be characterized as maximal abelian subalgebras consisting of semisimple endomorphisms in the adjoint representation. With such an $\mathfrak{h}$, $\mathfrak{g}$ admits the {{< knowl id="root-space-decomposition" text="root space decomposition" >}}
$$
\mathfrak{g}=\mathfrak{h}\oplus \bigoplus_{\alpha\in \Phi}\mathfrak{g}_\alpha,
$$

where $\Phi\subset \mathfrak{h}^*$ is the {{< knowl id="root-lie-algebra" text="root set" >}} and $\mathfrak{g}_\alpha$ are the {{< knowl id="root-space" text="root spaces" >}}.

**Motivation.** Cartan subalgebras are the “coordinate axes” for semisimple structure: weights of representations live in $\mathfrak{h}^*$ (see {{< knowl id="weights-in-dual-cartan" text="weights in the dual Cartan" >}}), and the choice of $\mathfrak{h}$ underlies Dynkin-diagram data such as the {{< knowl id="cartan-matrix" text="Cartan matrix" >}}.
