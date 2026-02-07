---
title: "Root space decomposition"
description: "Decomposition of a semisimple Lie algebra into a Cartan subalgebra plus root spaces for the adjoint action."
---

Let $\mathfrak g$ be a finite-dimensional complex semisimple Lie algebra (see {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebra" >}}) and let $\mathfrak h\subset\mathfrak g$ be a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}. For each $\alpha\in\mathfrak h^*$ define the weight space
\[
\mathfrak g_\alpha=\{X\in\mathfrak g:[H,X]=\alpha(H)X\ \text{for all }H\in\mathfrak h\},
\]
and let $\Phi\subset\mathfrak h^*$ be the set of nonzero $\alpha$ with $\mathfrak g_\alpha\neq 0$ (the {{< knowl id="root-lie-algebra" text="roots" >}}).

The **root space decomposition** (sometimes called the Cartan decomposition of $\mathfrak g$) is the direct sum decomposition
\[
\mathfrak g \;=\; \mathfrak h \;\oplus\; \bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
\]
Conceptually, it is the simultaneous eigenspace decomposition for the commuting family of endomorphisms $\{\mathrm{ad}(H)\}_{H\in\mathfrak h}$ coming from the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}}.

Two structural bracket relations are fundamental:

- $[\mathfrak h,\mathfrak g_\alpha]\subseteq \mathfrak g_\alpha$ with the eigenvalue rule $[H,X]=\alpha(H)X$;
- $[\mathfrak g_\alpha,\mathfrak g_\beta]\subseteq \mathfrak g_{\alpha+\beta}$ (with the convention $\mathfrak g_{\gamma}=0$ if $\gamma$ is not a weight), as explained in {{< knowl id="root-space" text="root spaces" >}}.

With the inner product induced by the {{< knowl id="killing-form" text="Killing form" >}}, the set $\Phi$ satisfies the axioms of a {{< knowl id="root-system" text="root system" >}}. Choosing a {{< knowl id="positive-root" text="positive system" >}} refines this into a triangular decomposition and is the starting point for Dynkin diagram combinatorics (see {{< knowl id="dynkin-diagram" text="Dynkin diagrams" >}}).
