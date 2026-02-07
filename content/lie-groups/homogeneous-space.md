---
title: "Homogeneous space"
description: "A manifold with a transitive Lie group action; equivalently a quotient G/H by a stabilizer."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} acting smoothly on a manifold $M$ (see {{< knowl id="smooth-action-lie-group" text="smooth action" >}}).

**Definition (Homogeneous space).**  
$M$ is a **homogeneous space** for $G$ if the action is {{< knowl id="transitive-action-lie" text="transitive" >}}, i.e. for any $p,q\in M$ there exists $g\in G$ with $g\cdot p=q$.

Fix $p\in M$ and let $H=G_p$ be its {{< knowl id="stabilizer-lie-group" text="stabilizer" >}}. Then the orbit map $G\to M$, $g\mapsto g\cdot p$, induces a bijection
\[
G/H \;\longrightarrow\; M,
\]
where $G/H$ is the {{< knowl id="coset-space" text="coset space" >}}. If $H$ is a {{< knowl id="closed-subgroup-lie-group" text="closed" >}} subgroup, then $G/H$ carries a unique smooth manifold structure making the induced map a $G$-equivariant diffeomorphism (compare the {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}).

**Special case.**  
If the action is also {{< knowl id="free-action-lie" text="free" >}}, then $H$ is trivial and $M$ is (noncanonically) identified with $G$; in the free-and-transitive case, $M$ is a {{< knowl id="principal-homogeneous-space" text="principal homogeneous space" >}}.

**Context.**  
Homogeneous spaces provide the basic examples of manifolds built from Lie groups (spheres, Grassmannians, flag varieties), and their geometry is controlled by the subgroup $H$ and the induced action on tangent spaces.
