---
title: "Left-invariant vector fields form the Lie algebra"
description: "Left-invariant vector fields are closed under bracket and identify with T_eG."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. A smooth vector field $X$ on $G$ is **left-invariant** if $(L_g)_*X = X$ for all $g\in G$, where $L_g$ is {{< knowl id="left-translation" text="left translation" >}}.

**Lemma.**  

1. The space $\mathfrak X_L(G)$ of left-invariant vector fields is closed under the usual Lie bracket of vector fields, hence is a Lie algebra.
2. Evaluation at the identity defines a Lie algebra isomorphism
   \[
   \mathfrak X_L(G)\;\xrightarrow{\ \cong\ }\; T_eG,
   \]
   where $T_eG$ is the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of G" >}}.
   Explicitly, for $v\in T_eG$, the corresponding left-invariant field is
   \[
   X_v(g)=(dL_g)_e(v).
   \]

**Idea of proof.**  
Left-invariance is preserved by brackets because pushforward by a diffeomorphism commutes with the vector-field bracket. The map $v\mapsto X_v$ is inverse to evaluation at $e$ by construction, and the induced bracket on $T_eG$ matches the Lie algebra bracket (compare {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}}).

**Context.**  
This lemma is the conceptual bridge from global group structure to infinitesimal structure and underlies constructions such as the {{< knowl id="exponential-map-lie-group" text="exponential map" >}}, where one exponentiates elements of $T_eG$.
