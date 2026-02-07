---
title: "Permutation Representation"
description: "A homomorphism from a group into bijections of a set"
---

A **permutation representation** of a {{< knowl id="group" text="group" >}} $G$ on a set $X$ is a {{< knowl id="group-homomorphism" text="group homomorphism" >}}
$$
\rho: G \to \mathrm{Sym}(X),
$$

where $\mathrm{Sym}(X)$ denotes the group of all {{< knowl id="bijective-function" section="shared-foundations" text="bijective" >}} maps $X\to X$ under composition. Giving such a homomorphism is equivalent to giving a {{< knowl id="group-action" text="group action" >}} via $g\cdot x := \rho(g)(x)$.

The kernel of $\rho$ is exactly the {{< knowl id="kernel-of-action" text="kernel of the action" >}}. In particular, $\rho$ is injective iff the action is {{< knowl id="faithful-action" text="faithful" >}}, and {{< knowl id="cayleys-theorem" text="Cayley's theorem" >}} says every group has a faithful permutation representation (on itself by left multiplication).

**Examples:**
- (Left regular representation) $\rho(g)$ is the permutation $x\mapsto gx$ of the underlying set of $G$.
- (Action on cosets) For $H\le G$, the action on $G/H$ gives a homomorphism $G\to \mathrm{Sym}(G/H)$.
- (Conjugation) The conjugation action gives a homomorphism $G\to \mathrm{Sym}(G)$.
