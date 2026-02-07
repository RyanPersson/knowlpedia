---
title: "Opposite ring"
description: "The ring with the same underlying abelian group but reversed multiplication."
---

Let $R$ be a {{< knowl id="ring" text="ring" >}}. The **opposite ring** $R^{\mathrm{op}}$ is defined to have the same underlying additive group as $R$, but with multiplication given by
\[
a\cdot_{\mathrm{op}} b := ba.
\]

The construction is functorial and reverses multiplication: a homomorphism $R\to S$ induces $R^{\mathrm{op}}\to S^{\mathrm{op}}$. The identity map identifies $R$ with $R^{\mathrm{op}}$ exactly when $R$ is {{< knowl id="commutative-ring" text="commutative" >}}, and the {{< knowl id="center-of-ring" text="center" >}} is unchanged by passing to the opposite ring.

**Examples:**
- If $R$ is commutative (e.g. $\mathbb{Z}$), then $R^{\mathrm{op}}=R$ as rings.
- For the {{< knowl id="matrix-ring" text="matrix ring" >}} $M_n(R)$, transposition gives an isomorphism $(M_n(R))^{\mathrm{op}}\cong M_n(R^{\mathrm{op}})$.
- If $R$ is the ring of upper-triangular $2\times 2$ matrices over a field, then $R^{\mathrm{op}}$ is naturally isomorphic to the ring of lower-triangular matrices.