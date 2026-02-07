---
title: "Heisenberg group"
description: "The basic nonabelian nilpotent Lie group, central extension of an abelian group."
---

For $n\ge 1$, the (real) **Heisenberg group** $H_n$ can be realized as $\mathbb R^{2n}\times \mathbb R$ with elements written $(x,y,z)$ where $x,y\in\mathbb R^n$ and $z\in\mathbb R$, and group law
\[
(x,y,z)\cdot(x',y',z')=\Big(x+x',\,y+y',\,z+z' + \tfrac12(x\cdot y' - y\cdot x')\Big).
\]
This makes $H_n$ a connected {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} of dimension $2n+1$. Its Lie algebra is the Heisenberg Lie algebra (compare {{< knowl id="example-heisenberg-algebra" text="the Heisenberg algebra example" >}}), which is {{< knowl id="nilpotent-lie-algebra" text="nilpotent" >}}.

**Concrete calculation: commutator and center.**  
Let $p=(x,y,z)$ and $q=(x',y',z')$. Using the group law and the inverse
\[
(x,y,z)^{-1}=(-x,-y,-z),
\]
one computes the commutator
\[
[p,q]=pqp^{-1}q^{-1}=(0,0,\,x\cdot y' - y\cdot x').
\]
In particular, the commutator always lies in the “$z$-axis,” which is the {{< knowl id="center-of-a-lie-group" text="center" >}}:
\[
Z(H_n)=\{(0,0,z): z\in\mathbb R\}.
\]
Thus $H_n/Z(H_n)\cong \mathbb R^{2n}$ is abelian, and $H_n$ is 2-step nilpotent (compare {{< knowl id="lower-central-series-lie-algebra" text="lower central series" >}} for the analogous Lie-algebra notion).

**Exponential/BCH viewpoint.**  
Because $H_n$ is nilpotent, the {{< knowl id="exponential-map-lie-group" text="exponential map" >}} is a global diffeomorphism and the multiplication law is governed by a truncated {{< knowl id="baker-campbell-hausdorff-formula" text="BCH formula" >}}, reflecting that iterated brackets vanish after length 2.
