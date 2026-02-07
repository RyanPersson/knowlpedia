---
title: "Orbit of a group action"
description: "The set of points reachable from a given point under a group action."
---

Consider a {{< knowl id="smooth-action-of-a-lie-group-on-a-manifold" text="smooth action" >}} of a Lie group $G$ on a manifold $M$.

For $x\in M$, the **orbit** of $x$ (under the action of $G$) is the subset
\[
G\cdot x := \{ g\cdot x \mid g\in G\}\subseteq M.
\]
Equivalently, $G\cdot x$ is the image of the {{< knowl id="orbit-map" text="orbit map" >}} $\Phi^x:G\to M$, $g\mapsto g\cdot x$.

Two points $x,y\in M$ lie in the same orbit if and only if there exists $g\in G$ with $y=g\cdot x$; this is an equivalence relation whose equivalence classes are precisely the orbits, and the corresponding quotient is the {{< knowl id="quotient-space-of-an-action" text="orbit space" >}} $M/G$.

## Examples
1. **Rotations in the plane.** For the $SO(2)$-action on $\mathbb{R}^2$, the orbit of a nonzero vector is a circle of radius $\|x\|$, while the orbit of $0$ is $\{0\}$.
2. **Conjugacy classes.** For the conjugation action of $G$ on itself, $g\cdot h := ghg^{-1}$, the orbit of $h$ is its conjugacy class.
3. **Linear actions.** For the natural $GL(n,\mathbb{R})$-action on $\mathbb{R}^n$, the orbit of any nonzero vector is $\mathbb{R}^n\setminus\{0\}$, and the orbit of $0$ is $\{0\}$.
