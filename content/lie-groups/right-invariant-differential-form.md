---
title: "Right-invariant differential form"
description: "A differential form on a Lie group fixed by all right translations, determined by its value at the identity."
---

Let $G$ be a Lie group. A differential $k$-form $\omega\in\Omega^k(G)$ is **right-invariant** if
\[
(R_g)^*\omega=\omega\qquad\text{for all }g\in G,
\]
where $R_g$ denotes {{< knowl id="right-translation" text="right translation" >}} by $g$.

Right-invariant forms are completely determined by their value at the identity element $e\in G$. Concretely, if $\omega$ is right-invariant, then for $g\in G$ and $v_1,\dots,v_k\in T_gG$,
\[
\omega_g(v_1,\dots,v_k)=\omega_e\big((dR_{g^{-1}})_g v_1,\dots,(dR_{g^{-1}})_g v_k\big).
\]
Thus evaluation at $e$ gives a vector space isomorphism
\[
\Omega^k(G)^{G\text{-right}}\;\cong\;\Lambda^k(\mathfrak g^*),
\]
where $\mathfrak g=\mathrm{Lie}(G)$ (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}).

Right-invariant forms are the natural home for the {{< knowl id="right-maurer-cartan-form" text="right Maurer–Cartan form" >}}, and many identities (including the {{< knowl id="maurer-cartan-equation" text="Maurer–Cartan equation" >}}) can be expressed neatly in terms of invariant forms. Compare also with {{< knowl id="left-invariant-differential-form" text="left-invariant forms" >}} and the special case of {{< knowl id="bi-invariant-differential-form" text="bi-invariant forms" >}}.
