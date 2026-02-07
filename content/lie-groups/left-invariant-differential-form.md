---
title: "Left-invariant differential form"
description: "A differential form on a Lie group fixed by all left translations."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}, and let $L_g:G\to G$ denote {{< knowl id="left-translation" text="left translation" >}} by $g$.

**Definition (Left-invariant form).**  
A differential $k$-form $\omega\in \Omega^k(G)$ is **left-invariant** if
\[
L_g^*\omega=\omega \quad\text{for all } g\in G.
\]

**Identification with alternating forms on the Lie algebra.**  
Evaluation at the identity defines an isomorphism
\[
\Omega^k(G)^{G\text{-left}} \;\cong\; \Lambda^k(\mathfrak g^*),
\]
where $\mathfrak g=T_eG$ is the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" >}}: a left-invariant form is uniquely determined by its value on $T_eG$, and any alternating form on $\mathfrak g$ extends uniquely to a left-invariant form by left translation. This extension can be written succinctly using the {{< knowl id="left-maurer-cartan-form" text="left Maurer–Cartan form" >}}.

**Context.**  
Left-invariant forms reduce many global computations on $G$ to multilinear algebra on $\mathfrak g$ and interact naturally with the {{< knowl id="maurer-cartan-equation" text="Maurer–Cartan equation" >}}. Analogous notions include {{< knowl id="right-invariant-differential-form" text="right-invariant" >}} and {{< knowl id="bi-invariant-differential-form" text="bi-invariant" >}} forms.
