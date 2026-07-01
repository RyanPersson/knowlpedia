+++
id = "lie-groups/right-invariant-differential-form"
title = "Right-invariant differential form"
kind = "knowl"
summary = "A differential form on a Lie group fixed by all right translations, determined by its value at the identity."
aliases = ["right-invariant-differential-form", "Right-invariant differential form"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/right-invariant-differential-form.md"
+++

Let $G$ be a Lie group. A differential $k$-form $\omega\in\Omega^k(G)$ is **right-invariant** if
\[
(R_g)^*\omega=\omega\qquad\text{for all }g\in G,
\]
where $R_g$ denotes [[lie-groups/right-translation|right translation]] by $g$.

Right-invariant forms are completely determined by their value at the identity element $e\in G$. Concretely, if $\omega$ is right-invariant, then for $g\in G$ and $v_1,\dots,v_k\in T_gG$,
\[
\omega_g(v_1,\dots,v_k)=\omega_e\big((dR_{g^{-1}})_g v_1,\dots,(dR_{g^{-1}})_g v_k\big).
\]
Thus evaluation at $e$ gives a vector space isomorphism
\[
\Omega^k(G)^{G\text{-right}}\;\cong\;\Lambda^k(\mathfrak g^*),
\]
where $\mathfrak g=\mathrm{Lie}(G)$ (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]).

Right-invariant forms are the natural home for the [[lie-groups/right-maurer-cartan-form|right Maurer–Cartan form]], and many identities (including the [[lie-groups/maurer-cartan-equation|Maurer–Cartan equation]]) can be expressed neatly in terms of invariant forms. Compare also with [[lie-groups/left-invariant-differential-form|left-invariant forms]] and the special case of [[lie-groups/bi-invariant-differential-form|bi-invariant forms]].
