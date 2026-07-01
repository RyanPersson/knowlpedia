+++
id = "fiber-bundles/exponential-map-lie-group-exponential"
title = "Exponential Map of a Lie Group"
kind = "knowl"
summary = "The map _G:g G sending X to the time-1 value of the unique one-parameter subgroup with velocity X at the identity."
aliases = ["exponential-map-lie-group-exponential", "Exponential Map of a Lie Group"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/exponential-map-lie-group-exponential.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with identity element \(e\), and let \(\mathfrak g=T_eG\) be its [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]].

**Definition (Lie group exponential).**
For each \(X\in \mathfrak g\), there exists a unique smooth group homomorphism
\[
\gamma_X:(\mathbb R,+)\longrightarrow G
\]
such that \(\gamma_X(0)=e\) and \(\gamma_X'(0)=X\) (viewing \(X\) as a tangent vector in \(T_eG\)). The **exponential map** of \(G\) is the smooth map
\[
\exp_G:\mathfrak g\longrightarrow G,\qquad \exp_G(X)=\gamma_X(1).
\]
Equivalently, \(\gamma_X(t)=\exp_G(tX)\) is the integral curve through \(e\) of the [[lie-groups/left-invariant-vector-field|left-invariant vector field]] determined by \(X\), defined using [[fiber-bundles/left-translation-l-g|left translations]].

**Basic properties.**
- \(\exp_G(0)=e\) and \((d\exp_G)_0=\mathrm{id}_{\mathfrak g}\).
- The curve \(t\mapsto \exp_G(tX)\) is a one-parameter subgroup: \(\exp_G((s+t)X)=\exp_G(sX)\exp_G(tX)\).
- If \(X,Y\in\mathfrak g\) commute (i.e. \([X,Y]=0\) for the [[fiber-bundles/lie-bracket|Lie bracket]]), then \(\exp_G(X+Y)=\exp_G(X)\exp_G(Y)\).
- If \(\varphi:G\to H\) is a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]], then \(\varphi\) intertwines exponentials via the induced [[fiber-bundles/differential-of-a-lie-group-homomorphism-lie-algebra-homomorphism|Lie algebra homomorphism]]:
  \[
  \varphi(\exp_G(X))=\exp_H(d\varphi_e(X)).
  \]

### Examples

1. **Additive group \((\mathbb R^n,+)\).**
   Here \(G=\mathbb R^n\) is a Lie group under addition, \(\mathfrak g\cong \mathbb R^n\), and the one-parameter subgroup with velocity \(X\) is \(\gamma_X(t)=tX\). Thus \(\exp_G(X)=X\) (the identity map).

2. **Circle group \(S^1\subset \mathbb C\).**
   With multiplication in \(\mathbb C\), \(G=S^1\) has Lie algebra \(\mathfrak g=T_1S^1=i\mathbb R\). The exponential map is the usual complex exponential restricted to \(i\mathbb R\):
   \[
   \exp_{S^1}(i\theta)=e^{i\theta}.
   \]

3. **Matrix Lie groups.**
   If \(G\subseteq GL(n,\mathbb R)\) is a matrix Lie group, then \(\mathfrak g\subseteq M_n(\mathbb R)\), and \(\exp_G\) is given by the matrix exponential:
   \[
   \exp_G(A)=\sum_{k=0}^{\infty}\frac{A^k}{k!}.
   \]
   For example, in \(SO(2)\) this recovers rotations, and in \(GL(n,\mathbb R)\) it produces invertible matrices for all \(A\).
