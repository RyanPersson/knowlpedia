+++
id = "fiber-bundles/construction-induced-connection-on-an-associated-bundle-using-horizontals"
title = "Induced connection on an associated bundle via horizontals"
kind = "knowl"
summary = "Construction of an Ehresmann connection on an associated bundle from a principal connection on P."
aliases = ["construction-induced-connection-on-an-associated-bundle-using-horizontals", "Induced connection on an associated bundle via horizontals"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-induced-connection-on-an-associated-bundle-using-horizontals.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with [[fiber-bundles/principal-connection|principal connection]] $\omega$, and let $E=P\times_G F$ be the [[fiber-bundles/construction-associated-bundle-p-g-f-from-a-left-g-space-f|associated bundle]] for a left $G$-space $F$. Write $q:P\times F\to E$ for the quotient map and denote by $\pi_E:E\to M$ the bundle projection.

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

In the vector bundle case (fiber a vector space), this induced connection coincides with the usual notion of [[fiber-bundles/connection-on-a-vector-bundle|connection on a vector bundle]].

## Examples
1. For $E=P\times_G G$ with left multiplication, the induced connection recovers the original principal connection under the identification $E\cong P$.
2. For $E=\mathrm{Ad}(P)$, the construction produces a natural connection on the adjoint bundle used in gauge theory to differentiate gauge parameters.
3. If $P$ is trivial over $U$ and $A$ is the local gauge potential, the induced horizontals on $U\times F$ are determined by $A$ acting through the infinitesimal action of $\mathfrak g$ on $F$.
