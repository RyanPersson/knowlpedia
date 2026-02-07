---
title: "Convention: Ad(P) uses the conjugation action on G"
description: "Notation convention that the adjoint bundle is formed using the conjugation action of the structure group on itself"
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. In this project we reserve the notation $\operatorname{Ad}(P)$ for the associated bundle with fiber the group $G$ itself, where $G$ acts on $G$ by conjugation.

## Convention
We define the **adjoint bundle**
\[
\operatorname{Ad}(P):=P\times_G G
\]
using the {{< knowl id="conjugation-action-of-a-lie-group-on-itself" text="conjugation action" >}} of $G$ on itself:
\[
g\cdot h := ghg^{-1}\qquad (g,h\in G),
\]
together with the general convention that {{< knowl id="convention-associated-bundles-use-a-left-g-action-on-the-fiber-f" text="associated bundles use a left G-action on the fiber" >}} while $P$ carries a right principal action (see {{< knowl id="convention-principal-bundles-use-a-right-g-action-on-p" text="right action convention" >}}).

This is compatible with the construction in {{< knowl id="construction-adjoint-bundle-ad" text="construction of the adjoint bundle" >}}, and it is distinct from the **adjoint Lie algebra bundle**
\[
\operatorname{ad}(P):=P\times_G \mathfrak g,
\]
which uses the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation on the Lie algebra" section="lie-groups">}}; see {{< knowl id="construction-adjoint-lie-algebra-bundle-ad" text="construction of ad(P)" >}}.

Because conjugation is by group automorphisms, $\operatorname{Ad}(P)$ is a bundle of Lie groups (fiberwise multiplication is well-defined). In particular, the {{< knowl id="gauge-group" text="gauge group" >}} can be identified with the smooth sections of $\operatorname{Ad}(P)$ once this convention is fixed.

## Examples
1. **Trivial principal bundle.**  
   If $P\cong M\times G$, then $\operatorname{Ad}(P)\cong M\times G$ as a bundle of groups (choosing the obvious global section produces the identification).

2. **Frame bundle interpretation.**  
   If $E\to M$ is a rank $n$ vector bundle and $P=\operatorname{Fr}(E)$ is its {{< knowl id="construction-frame-bundle-fr-of-a-vector-bundle-e" text="frame bundle" >}}, then
   \[
   \operatorname{Ad}(P)=\operatorname{Fr}(E)\times_{GL(n)}GL(n)
   \]
   can be identified with the bundle $\operatorname{Aut}(E)\to M$ of fiberwise linear automorphisms of $E$ (conjugation is exactly change-of-basis for matrices).

3. **Abelian structure group.**  
   If $G$ is abelian, conjugation is trivial, so $\operatorname{Ad}(P)\cong M\times G$ canonically. For instance, for the {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}} as a principal $U(1)$-bundle, the adjoint bundle is $S^2\times U(1)$.
