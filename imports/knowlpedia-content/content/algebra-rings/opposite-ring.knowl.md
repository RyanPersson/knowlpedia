+++
id = "algebra-rings/opposite-ring"
title = "Opposite ring"
kind = "knowl"
summary = "The ring with the same underlying abelian group but reversed multiplication."
aliases = ["opposite-ring", "Opposite ring"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/opposite-ring.md"
+++

Let $R$ be a [[algebra-rings/ring|ring]]. The **opposite ring** $R^{\mathrm{op}}$ is defined to have the same underlying additive group as $R$, but with multiplication given by
\[
a\cdot_{\mathrm{op}} b := ba.
\]

The construction is functorial and reverses multiplication: a homomorphism $R\to S$ induces $R^{\mathrm{op}}\to S^{\mathrm{op}}$. The identity map identifies $R$ with $R^{\mathrm{op}}$ exactly when $R$ is [[algebra-rings/commutative-ring|commutative]], and the [[algebra-rings/center-of-ring|center]] is unchanged by passing to the opposite ring.

**Examples:**
- If $R$ is commutative (e.g. $\mathbb{Z}$), then $R^{\mathrm{op}}=R$ as rings.
- For the [[algebra-rings/matrix-ring|matrix ring]] $M_n(R)$, transposition gives an isomorphism $(M_n(R))^{\mathrm{op}}\cong M_n(R^{\mathrm{op}})$.
- If $R$ is the ring of upper-triangular $2\times 2$ matrices over a field, then $R^{\mathrm{op}}$ is naturally isomorphic to the ring of lower-triangular matrices.
