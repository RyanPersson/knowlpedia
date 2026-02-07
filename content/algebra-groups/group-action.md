---
title: "Group Action"
description: "A homomorphism from a group to permutations of a set, equivalently a compatible map G×X→X"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $X$ be a {{< knowl id="set" section="shared-foundations" text="set" >}}. A **(left) group action** of $G$ on $X$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $\alpha:G\times X\to X$ (usually written $\alpha(g,x)=g\cdot x$) such that:
1. $e\cdot x = x$ for all $x\in X$, where $e$ is the identity of $G$;
2. $(gh)\cdot x = g\cdot(h\cdot x)$ for all $g,h\in G$ and all $x\in X$.

Equivalently, an action is the same data as a {{< knowl id="group-homomorphism" text="group homomorphism" >}} from $G$ into the group of {{< knowl id="bijective-function" section="shared-foundations" text="bijective" >}} self-maps of $X$ (permutations), i.e. a {{< knowl id="permutation-representation" text="permutation representation" >}}. Actions organize many constructions (e.g. actions on cosets) and lead to the notions of {{< knowl id="orbit" text="orbits" >}} and {{< knowl id="stabilizer" text="stabilizers" >}}

**Examples:**
- (Left translation) $G$ acts on itself by $g\cdot x := gx$.
- (Action on cosets) If $H\le G$, then $G$ acts on the set of left cosets $G/H$ by $g\cdot (xH):=(gx)H$.
- (Conjugation) $G$ acts on itself by $g\cdot x := gxg^{-1}$.
