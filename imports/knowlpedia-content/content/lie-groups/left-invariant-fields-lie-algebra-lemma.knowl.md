+++
id = "lie-groups/left-invariant-fields-lie-algebra-lemma"
title = "Left-invariant vector fields form the Lie algebra"
kind = "knowl"
summary = "Left-invariant vector fields are closed under bracket and identify with T_eG."
aliases = ["left-invariant-fields-lie-algebra-lemma", "Left-invariant vector fields form the Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/left-invariant-fields-lie-algebra-lemma.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]]. A smooth vector field $X$ on $G$ is **left-invariant** if $(L_g)_*X = X$ for all $g\in G$, where $L_g$ is [[lie-groups/left-translation|left translation]].

**Lemma.**

1. The space $\mathfrak X_L(G)$ of left-invariant vector fields is closed under the usual Lie bracket of vector fields, hence is a Lie algebra.
2. Evaluation at the identity defines a Lie algebra isomorphism
   \[
   \mathfrak X_L(G)\;\xrightarrow{\ \cong\ }\; T_eG,
   \]
   where $T_eG$ is the [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of G]].
   Explicitly, for $v\in T_eG$, the corresponding left-invariant field is
   \[
   X_v(g)=(dL_g)_e(v).
   \]

**Idea of proof.**
Left-invariance is preserved by brackets because pushforward by a diffeomorphism commutes with the vector-field bracket. The map $v\mapsto X_v$ is inverse to evaluation at $e$ by construction, and the induced bracket on $T_eG$ matches the Lie algebra bracket (compare [[fiber-bundles/lie-bracket|Lie bracket]]).

**Context.**
This lemma is the conceptual bridge from global group structure to infinitesimal structure and underlies constructions such as the [[lie-groups/exponential-map-lie-group|exponential map]], where one exponentiates elements of $T_eG$.
