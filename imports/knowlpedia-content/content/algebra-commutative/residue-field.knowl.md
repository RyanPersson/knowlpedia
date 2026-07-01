+++
id = "algebra-commutative/residue-field"
title = "Residue field"
kind = "knowl"
summary = "For a local ring (R,m), the field R/m obtained by modding out by the maximal ideal."
aliases = ["residue-field", "Residue field"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/residue-field.md"
+++

Let $(R,\mathfrak m)$ be a [[algebra-commutative/local-ring|local ring]]. The **residue field** of $R$ is the quotient ring
\[
k(R):=R/\mathfrak m.
\]
Because $\mathfrak m$ is maximal (see [[algebra-commutative/maximal-ideal-local-ring|maximal ideal of a local ring]]), the quotient $R/\mathfrak m$ is a [[algebra-rings/field|field]].

The canonical surjection
\[
R \twoheadrightarrow R/\mathfrak m
\]
is sometimes called the **residue map**.

More generally, for a prime ideal $\mathfrak p\subset R$ one often sets
\[
\kappa(\mathfrak p):=R_{\mathfrak p}/\mathfrak pR_{\mathfrak p},
\]
where $R_{\mathfrak p}$ is the [[algebra-commutative/localization-at-prime|localization at p]]; this recovers the same construction after passing to that local ring.

### Examples

1. **$\mathbb Z_{(p)}$.** For the local ring $\mathbb Z_{(p)}$, the maximal ideal is $p\mathbb Z_{(p)}$, and
   \[
   \mathbb Z_{(p)}/p\mathbb Z_{(p)}\cong \mathbb F_p.
   \]

2. **$k[x]_{(x)}$.** In $R=k[x]_{(x)}$, the maximal ideal is $(x)R$, so
   \[
   k[x]_{(x)}/(x)\ \cong\ k
   \]
   via evaluation at $x=0$.

3. **$k[x,y]_{(x,y)}$.** In the local ring $k[x,y]_{(x,y)}$, the maximal ideal is $(x,y)$, and the residue field is again $k$.
