---
title: "Differential of a Lie Group Homomorphism"
description: "The induced linear map on Lie algebras d_e:g associated to a Lie group homomorphism :G H."
---

Let \(G\) and \(H\) be {{< knowl id="lie-group" text="Lie groups" >}} with identity elements \(e_G\) and \(e_H\), and let \(\varphi:G\to H\) be a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" section="lie-groups">}}. Since \(\varphi\) is a {{< knowl id="smooth-map" text="smooth map" >}}, it has a {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward)" >}} at every point; in particular at the identity:
\[
d\varphi_{e_G}:T_{e_G}G\longrightarrow T_{e_H}H.
\]
Using the standard identification of the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" section="lie-groups">}} of a Lie group with the tangent space at the identity, we view this as a linear map
\[
d\varphi_{e_G}:\mathfrak g\to\mathfrak h.
\]

**Theorem (Lie algebra homomorphism induced by \(\varphi\)).**  
Let \(\varphi:G\to H\) be a Lie group homomorphism. Then the differential at the identity
\(d\varphi_{e_G}:\mathfrak g\to\mathfrak h\) is a homomorphism of Lie algebras, meaning it preserves the {{< knowl id="lie-bracket" text="Lie bracket" >}}:
\[
d\varphi_{e_G}([X,Y])=[d\varphi_{e_G}(X),\,d\varphi_{e_G}(Y)] \quad \text{for all } X,Y\in\mathfrak g.
\]
Moreover, it intertwines the {{< knowl id="exponential-map-lie-group-exponential" text="exponential maps" >}}:
\[
\varphi(\exp_G(X))=\exp_H(d\varphi_{e_G}(X)) \quad \text{for all } X\in\mathfrak g.
\]
It is also functorial: if \(\psi:H\to K\) is another Lie group homomorphism, then
\[
d(\psi\circ\varphi)_{e_G}=d\psi_{e_H}\circ d\varphi_{e_G}.
\]

### Examples

1. **Inclusion of a Lie subgroup.**  
   If \(i:H\hookrightarrow G\) is the inclusion of a {{< knowl id="lie-subgroup" text="Lie subgroup" section="lie-groups">}}, then \(di_{e_H}:\mathfrak h\to\mathfrak g\) is the natural inclusion of tangent spaces at the identity. Concretely, it identifies \(\mathfrak h\) as a Lie subalgebra of \(\mathfrak g\).

2. **Determinant on \(GL(n,\mathbb R)\).**  
   The determinant is a Lie group homomorphism \(\det:GL(n,\mathbb R)\to \mathbb R^\times\). Identifying \(\mathfrak{gl}(n,\mathbb R)\cong M_n(\mathbb R)\), the induced map on Lie algebras is
   \[
   d(\det)_{I}(A)=\operatorname{tr}(A),
   \]
   and more generally \(d(\det)_B(V)=\det(B)\operatorname{tr}(B^{-1}V)\).

3. **Covering map \(\mathbb R\to S^1\).**  
   The map \(\varphi:\mathbb R\to S^1\subset\mathbb C\), \(\varphi(t)=e^{it}\), is a Lie group homomorphism (additive to multiplicative). Then \(d\varphi_0:\mathbb R\to T_1S^1\) sends \(a\mapsto ia\) (since \(\frac{d}{dt}e^{it}\big|_{t=0}=i\)). Under the common identification \(T_1S^1\cong \mathbb R\) via \(a\mapsto ia\), this differential is the identity.
