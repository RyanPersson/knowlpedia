---
title: "Equivalent conditions for triviality of a principal bundle"
description: "A principal G bundle is trivial exactly when it has a global section, or equivalently when its transition cocycle is cohomologous to the identity."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $G$.

## Theorem (TFAE: principal bundle triviality)
The following are equivalent:

1. (**Bundle isomorphism with the product**)  
   $P$ is trivial, i.e. there exists a {{< knowl id="principal-bundle-isomorphism" text="principal bundle isomorphism" >}}
   \[
   \Phi:P \stackrel{\cong}{\longrightarrow} M\times G
   \]
   commuting with the projections to $M$ and intertwining the right $G$-actions (see {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}}).

2. (**Existence of a global section**)  
   $P$ admits a smooth global section $s:M\to P$ with $\pi\circ s=\mathrm{id}_M$ (see {{< knowl id="section-of-ad" text="section" >}} for the general notion of section, and compare the principal-bundle criterion {{< knowl id="trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial" text="global section implies triviality" >}} together with its converse {{< knowl id="converse-triviality-criterion-trivial-principal-bundle-admits-a-global-section" text="trivial bundles admit sections" >}}).

3. (**Transition functions can be made trivial**)  
   There exists a bundle atlas for $P$ whose transition functions are all the identity element of $G$ on overlaps. Equivalently, the transition cocycle is {{< knowl id="equivalence-of-cocycles" text="equivalent (cohomologous) to the trivial cocycle" >}} (see {{< knowl id="principal-bundle-transition-function" text="transition functions" >}} and {{< knowl id="cocycle-condition-for-transition-functions" text="cocycle condition" >}}).

4. (**A global equivariant trivialization map**)  
   There exists a smooth map $f:P\to G$ such that
   \[
   f(pg)=g^{-1}f(p)\qquad\text{for all }p\in P,\ g\in G.
   \]
   (This is the condition that $f$ is equivariant for the right action on $P$ and the right-translation action on $G$; compare {{< knowl id="equivariant-map" text="equivariant maps" >}}.)

The equivalence (1) $\Leftrightarrow$ (2) is the most frequently used in practice: a global section picks a preferred point in each fiber, and translating that point by $G$ produces the explicit trivialization.

## Examples
1. **Hopf bundle is not trivial.**  
   The Hopf fibration $S^3\to S^2$ is a nontrivial principal $U(1)$-bundle (see {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}}). By the theorem, it admits no global section; this is a standard instance of {{< knowl id="counterexample-nontrivial-principal-bundle-admitting-no-global-section" text="a nontrivial principal bundle with no global section" >}}.

2. **Triviality from a global gauge choice on a trivial bundle.**  
   On $P=M\times G$, the map $s(x)=(x,e)$ is a global section, so the theorem recovers triviality immediately. In this case, choosing a section is exactly choosing a global “gauge,” and it identifies principal connections with $\mathfrak g$-valued $1$-forms on $M$ (compare {{< knowl id="flat-connection-a0-on-a-trivial-bundle" text="flat connection on a trivial bundle" >}} and {{< knowl id="pure-gauge-connection-ag-1dg-on-a-trivial-bundle" text="pure gauge connections" >}}).

3. **Principal bundles over the circle for connected groups.**  
   If $G$ is connected, every principal $G$-bundle over $S^1$ is trivial, hence admits a global section. This aligns with the clutching description in {{< knowl id="principal-bundle-over-s1-defined-by-a-clutching-function" text="principal bundles over S1 via clutching" >}}, where all clutching data become equivalent to the identity when $G$ has a single connected component.
