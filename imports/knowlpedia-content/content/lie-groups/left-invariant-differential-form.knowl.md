+++
id = "lie-groups/left-invariant-differential-form"
title = "Left-invariant differential form"
kind = "knowl"
summary = "A differential form on a Lie group fixed by all left translations."
aliases = ["left-invariant-differential-form", "Left-invariant differential form"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/left-invariant-differential-form.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]], and let $L_g:G\to G$ denote [[lie-groups/left-translation|left translation]] by $g$.

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
where $\mathfrak g=T_eG$ is the [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]]: a left-invariant form is uniquely determined by its value on $T_eG$, and any alternating form on $\mathfrak g$ extends uniquely to a left-invariant form by left translation. This extension can be written succinctly using the [[lie-groups/left-maurer-cartan-form|left Maurer–Cartan form]].

**Context.**
Left-invariant forms reduce many global computations on $G$ to multilinear algebra on $\mathfrak g$ and interact naturally with the [[lie-groups/maurer-cartan-equation|Maurer–Cartan equation]]. Analogous notions include [[lie-groups/right-invariant-differential-form|right-invariant]] and [[lie-groups/bi-invariant-differential-form|bi-invariant]] forms.
