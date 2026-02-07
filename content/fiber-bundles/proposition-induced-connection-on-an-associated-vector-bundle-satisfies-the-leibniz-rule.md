---
title: "Leibniz rule for induced connections on associated bundles"
description: "The induced covariant derivative on an associated vector bundle is a derivation with respect to multiplying sections by functions."
---

Let \(\pi:P\to M\) be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group \(G\), and let \(\omega\) be a {{< knowl id="principal-connection" text="principal connection" >}} on \(P\). Given a representation \(\rho:G\to \mathrm{GL}(V)\), form the associated vector bundle \(E:=P\times_\rho V\to M\). The connection \(\omega\) induces a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} (covariant derivative)
\[
\nabla:\Gamma(E)\to \Omega^1(M;E),
\]
characterized by the usual horizontal-lift construction (or equivalently by local connection 1-forms obtained from \(\omega\) in trivializations).

## Proposition (Leibniz rule)
For every smooth function \(f\in C^\infty(M)\) and every section \(s\in \Gamma(E)\), the induced covariant derivative satisfies
\[
\nabla(fs) \;=\; df\otimes s \;+\; f\,\nabla s.
\]
Equivalently, for every {{< knowl id="vector-field" text="vector field" >}} \(X\) on \(M\),
\[
\nabla_X(fs) \;=\; X(f)\,s \;+\; f\,\nabla_X s.
\]

In particular, the induced \(\nabla\) is a bona fide connection on \(E\) in the standard sense: it is \(\mathbb R\)-linear in \(s\) and is a first-order differential operator over multiplication by functions.

## Examples
1. **Trivial bundle with matrix-valued 1-form.** If \(P=M\times G\) and \(E=M\times V\), the induced connection can be written as \(\nabla = d + \rho_*(A)\) for a \(\mathfrak g\)-valued 1-form \(A\). Then
   \[
   \nabla(fs)=d(fs)+\rho_*(A)\,fs=(df)s+f(ds+\rho_*(A)s),
   \]
   which is exactly the Leibniz rule.
2. **Associated line bundle.** For a principal \(U(1)\)-bundle and the standard 1-dimensional representation, \(\nabla\) is the usual connection on a complex line bundle; the Leibniz identity reduces to the familiar product rule for covariant differentiation of functions times sections.
3. **Tangent bundle from the frame bundle.** If \(P\) is the frame bundle of \(TM\) and \(\omega\) is a principal connection on \(P\), the associated bundle for the defining representation is \(TM\). The resulting \(\nabla\) on \(TM\) satisfies \(\nabla_X(fY)=X(f)Y+f\nabla_XY\).
