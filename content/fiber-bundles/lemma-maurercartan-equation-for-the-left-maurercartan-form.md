---
title: "Maurer–Cartan equation for the left Maurer–Cartan form"
description: "The left Maurer–Cartan form on a Lie group satisfies the structure equation dθ + 1/2[θ∧θ] = 0."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} with {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak g$. The **left Maurer–Cartan form** is the $\mathfrak g$-valued $1$-form $\theta_L\in\Omega^1(G;\mathfrak g)$ defined by
\[
(\theta_L)_g := (dL_{g^{-1}})_g : T_gG \to T_eG\cong \mathfrak g.
\]

**Lemma (Maurer–Cartan equation).** The form $\theta_L$ satisfies
\[
d\theta_L + \tfrac12[\theta_L\wedge\theta_L]=0,
\]
where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} and $[\theta_L\wedge\theta_L]$ uses the {{< knowl id="lie-bracket" text="Lie bracket" >}} on $\mathfrak g$.

This is the curvature-zero structure equation for the canonical flat connection on $G$, and it is the algebraic reason that “pure gauge” potentials have vanishing curvature.

## Examples
1. **Matrix groups.** If $G\subset \mathrm{GL}(n,\mathbb C)$ is a matrix Lie group, then $\theta_L=g^{-1}dg$, and the identity becomes
   \[
   d(g^{-1}dg) + (g^{-1}dg)\wedge (g^{-1}dg)=0.
   \]
2. **Abelian groups.** For $G=\mathbb R^n$ (additive), the bracket on $\mathfrak g$ is zero and $\theta_L$ is constant, so the equation reduces to $d\theta_L=0$.
3. **Pure gauge curvature.** If $A=g^{-1}dg$ on an open set $U$, then substituting into the {{< knowl id="local-curvature-formula-f-da-aa" text="local curvature formula" >}} gives $F=0$ exactly because of the Maurer–Cartan equation.
