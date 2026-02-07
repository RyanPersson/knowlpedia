---
title: "Induced connection on an associated bundle via horizontals"
description: "Construction of an Ehresmann connection on an associated bundle from a principal connection on P."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with {{< knowl id="principal-connection" text="principal connection" >}} $\omega$, and let $E=P\times_G F$ be the {{< knowl id="construction-associated-bundle-p-g-f-from-a-left-g-space-f" text="associated bundle" >}} for a left $G$-space $F$. Write $q:P\times F\to E$ for the quotient map and denote by $\pi_E:E\to M$ the bundle projection.

**Construction (horizontal distribution on E).** For $[p,u]\in E$, define the horizontal subspace
\[
H^E_{[p,u]} := dq_{(p,u)}(H_p \times \{0\}) \subset T_{[p,u]}E,
\]
where $H_p=\ker(\omega_p)\subset T_pP$ is the horizontal subspace of $P$ and $0\in T_uF$ is the zero vector. This is well-defined (independent of the representative $(p,u)$) because $H$ is $G$-equivariant and the quotient identifies $(pg,g^{-1}u)$ with $(p,u)$.

Then $TE$ splits as
\[
T_{[p,u]}E = H^E_{[p,u]} \oplus \ker(d\pi_E)_{[p,u]},
\]
giving an Ehresmann connection on $E$.

In the vector bundle case (fiber a vector space), this induced connection coincides with the usual notion of {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}}.

## Examples
1. For $E=P\times_G G$ with left multiplication, the induced connection recovers the original principal connection under the identification $E\cong P$.
2. For $E=\mathrm{Ad}(P)$, the construction produces a natural connection on the adjoint bundle used in gauge theory to differentiate gauge parameters.
3. If $P$ is trivial over $U$ and $A$ is the local gauge potential, the induced horizontals on $U\times F$ are determined by $A$ acting through the infinitesimal action of $\mathfrak g$ on $F$.
