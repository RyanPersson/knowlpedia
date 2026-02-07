---
title: "Local connection 1-form"
description: "A Lie algebra valued 1-form on an open set obtained by pulling back a principal connection along a local section"
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with Lie algebra $\mathfrak g$, and let $\omega\in\Omega^1(P;\mathfrak g)$ be a {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}} representing a {{< knowl id="principal-connection" text="principal connection" >}}.

Given a local section $s:U\to P$ over an open set $U\subseteq M$, the **local connection 1-form** (also called the gauge potential in that trivialization) is the $\mathfrak g$-valued 1-form
\[
A:=s^*\omega \in \Omega^1(U;\mathfrak g).
\]
This is the local representative of the global connection in the trivialization determined by $s$ (compare {{< knowl id="construction-local-trivialization-from-a-local-section" text="local trivialization from a local section" >}}).

### Change of section (local gauge transformation)
If $s'(x)=s(x)\cdot g(x)$ for a smooth map $g:U\to G$ (a {{< knowl id="local-gauge-transformation" text="local gauge transformation" >}}), then the pulled-back forms satisfy the standard transformation law
\[
A' = g^{-1} A g + g^{-1}dg,
\]
as recorded in {{< knowl id="lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg" text="the local gauge transformation law" >}}.

### On overlaps
If $\{s_i:U_i\to P\}$ is a system of local sections and $g_{ij}:U_i\cap U_j\to G$ are the associated transition functions defined by $s_j=s_i\,g_{ij}$ (see {{< knowl id="construction-transition-functions-g-iju-iu-jg-from-local-sections" text="transition functions from local sections" >}}), then on $U_i\cap U_j$ the local forms obey
\[
A_j = g_{ij}^{-1} A_i g_{ij} + g_{ij}^{-1}dg_{ij}.
\]

The corresponding local curvature 2-form is
\[
F:=dA + A\wedge A,
\]
as in {{< knowl id="local-curvature-formula-f-da-aa" text="the local curvature formula" >}}, and it transforms by conjugation (see {{< knowl id="lemma-local-curvature-transformation-law-fg-g-1fg" text="local curvature transformation law" >}}).

## Examples
1. **Trivial principal bundle.**  
   If $P\cong M\times G$ is trivial, choosing the global section $s(x)=(x,e)$ identifies a principal connection with a single global $\mathfrak g$-valued 1-form $A$ on $M$. The {{< knowl id="flat-connection-a0-on-a-trivial-bundle" text="flat connection" >}} corresponds to $A=0$, while a {{< knowl id="pure-gauge-connection-ag-1dg-on-a-trivial-bundle" text="pure gauge" >}} connection has the form $A=g^{-1}dg$.

2. **Dirac monopole on the Hopf bundle.**  
   For the {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}} as a principal $U(1)$-bundle, the {{< knowl id="dirac-monopole-connection-on-the-hopf-bundle" text="Dirac monopole connection" >}} is described by two local connection 1-forms $A_N$ and $A_S$ on the northern and southern charts of $S^2$, related on the overlap by a $U(1)$-valued gauge function.

3. **Levi-Civita connection in a local frame.**  
   For a Riemannian manifold, the {{< knowl id="levicivita-connection-connection" text="Levi-Civita connection" >}} can be viewed as a principal connection on the {{< knowl id="orthonormal-frame-bundle-o-of-a-riemannian-manifold" text="orthonormal frame bundle" >}}. Choosing a local orthonormal frame gives a matrix-valued local connection 1-form whose entries are the usual connection coefficients; its curvature is the matrix of curvature 2-forms in that frame (see {{< knowl id="curvature-2-form-in-a-frame" text="curvature 2-form in a frame" >}}).
