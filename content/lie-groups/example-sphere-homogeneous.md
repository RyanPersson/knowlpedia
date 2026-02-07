---
title: "Example: the sphere as a homogeneous space"
description: "The -sphere is a homogeneous space via the standard transitive action."
---

Consider the standard action of {{< knowl id="special-orthogonal-group" text="$SO(n{+}1)$" >}} on $\mathbb R^{n+1}$, hence on the unit sphere
\[
S^n=\{x\in\mathbb R^{n+1}:\|x\|=1\}.
\]
This is a smooth {{< knowl id="smooth-action-lie-group" text="Lie group action" >}}.

## Transitivity and stabilizer (explicit)
Fix the “north pole” $p=e_{n+1}=(0,\dots,0,1)$. For any $x\in S^n$, there exists $g\in SO(n{+}1)$ with $g\cdot p=x$ (choose an orthonormal basis sending $e_{n+1}$ to $x$), so the action is {{< knowl id="transitive-action-lie" text="transitive" >}}.

The stabilizer of $p$ consists of rotations preserving the orthogonal complement $p^\perp\cong\mathbb R^n$, hence
\[
\mathrm{Stab}(p)\cong SO(n),
\]
as an embedded {{< knowl id="lie-subgroup" text="Lie subgroup" >}} (see {{< knowl id="stabilizer-lie-group" text="stabilizer" >}}).

## Identification with a coset space
Define
\[
\Phi: SO(n{+}1)/SO(n) \longrightarrow S^n,\qquad \Phi(g\,SO(n)):=g\cdot p.
\]
This is well-defined because elements of $SO(n)$ fix $p$. It is bijective by transitivity and the stabilizer description, and it is a diffeomorphism once we use the standard smooth structure on the {{< knowl id="coset-space" text="coset space" >}} $SO(n{+}1)/SO(n)$ (which exists because $SO(n)$ is closed; compare the {{< knowl id="closed-subgroup-theorem" text="Closed Subgroup Theorem" >}}). Thus
\[
S^n \cong SO(n{+}1)/SO(n)
\]
as a {{< knowl id="homogeneous-space" text="homogeneous space" >}}.

## Dimension check (concrete calculation)
Using $\dim SO(m)=\frac{m(m-1)}{2}$,
\[
\dim\bigl(SO(n{+}1)/SO(n)\bigr)
=\frac{(n{+}1)n}{2}-\frac{n(n-1)}{2}=n=\dim S^n,
\]
consistent with the identification.

**Special case.** For $n=2$, this reads $S^2\cong SO(3)/SO(2)$, connecting directly to {{< knowl id="example-so3" text="the $SO(3)$ example" >}}.
