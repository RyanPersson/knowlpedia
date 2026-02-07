---
title: "Equivariant map associated to a section of an associated bundle"
description: "How a section of an associated bundle corresponds to an equivariant map from the principal bundle to the fiber"
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}, written using the standard convention that $P$ carries a right $G$-action (see {{< knowl id="convention-principal-bundles-use-a-right-g-action-on-p" text="the principal bundle action convention" >}}). Let $F$ be a smooth manifold with a left $G$-action, as in {{< knowl id="convention-associated-bundles-use-a-left-g-action-on-the-fiber-f" text="the associated bundle fiber action convention" >}}.

Form the {{< knowl id="associated-bundle" text="associated bundle" >}}
\[
E := P\times_G F \;\longrightarrow\; M,
\]
as in {{< knowl id="construction-associated-bundle-p-g-f-from-a-left-g-space-f" text="the construction of associated bundles" >}}.

### Construction: section gives an equivariant map
Let $s:M\to E$ be a smooth section. Define a map $\Phi_s:P\to F$ by the rule:
- given $p\in P$ with $\pi(p)=x$, write the point $s(x)\in E_x$ as an equivalence class $[p,f]$, and set $\Phi_s(p):=f$.

This is well-defined and smooth, and it satisfies the equivariance condition
\[
\Phi_s(p\cdot g) = g^{-1}\cdot \Phi_s(p)
\qquad\text{for all }p\in P,\ g\in G,
\]
i.e. $\Phi_s$ is an {{< knowl id="equivariant-map" text="equivariant map" >}} with respect to the right action on $P$ and the given left action on $F$.

### Converse: equivariant map gives a section
Conversely, if $\Phi:P\to F$ is smooth and satisfies $\Phi(p\cdot g)=g^{-1}\cdot \Phi(p)$, then
\[
s_\Phi(x) := [p,\Phi(p)]\in E_x
\]
is independent of the choice of $p\in P_x$ and defines a smooth section $s_\Phi:M\to E$.

Together, these constructions give a natural bijection
\[
\Gamma(E)\ \cong\ \{\,\Phi:P\to F\text{ smooth} \mid \Phi(p\cdot g)=g^{-1}\cdot \Phi(p)\,\}.
\]

## Examples
1. **Trivial principal bundle reduces equivariance to an ordinary map.**  
   If $P=M\times G$ is {{< knowl id="trivial-principal-bundle-mgm" text="trivial" >}}, then any section of $E=(M\times G)\times_G F \cong M\times F$ is the same as a smooth map $u:M\to F$. The corresponding equivariant map is
   \[
   \Phi_u(x,g) = g^{-1}\cdot u(x).
   \]

2. **Associated line bundle and equivariant complex-valued functions.**  
   Take $G=U(1)$ acting on $F=\mathbb C$ by scalar multiplication, and let $E=P\times_{U(1)}\mathbb C$ be the associated complex line bundle (see {{< knowl id="associated-vector-bundle" text="associated vector bundles" >}} for the general vector-bundle case). A section of $E$ corresponds to a smooth function $\Phi:P\to\mathbb C$ satisfying
   \[
   \Phi(p\cdot e^{i\theta}) = e^{-i\theta}\,\Phi(p).
   \]
   This is the standard “equivariant function” description of sections of a line bundle.

3. **Adjoint bundle: sections as conjugation-equivariant maps.**  
   Let $F=G$ with the conjugation action, so $E=P\times_G G$ is the {{< knowl id="adjoint-bundle-p-g-g-with-conjugation-action" text="adjoint bundle" >}}. A section then corresponds to a map $\Phi:P\to G$ satisfying
   \[
   \Phi(p\cdot g)=g^{-1}\Phi(p)g.
   \]
   Interpreting such sections as bundle automorphisms recovers the usual identification of the {{< knowl id="gauge-group" text="gauge group" >}} with sections of the adjoint bundle (compare {{< knowl id="gauge-transformation" text="gauge transformations" >}}).
