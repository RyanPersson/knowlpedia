---
title: "Nontrivial principal bundle with no global section"
description: "Illustration of the fact that a principal bundle is trivial exactly when it admits a global smooth section."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}.

## Triviality criterion via sections
A smooth global section $s:M\to P$ (so $\pi\circ s=\mathrm{id}_M$) trivializes $P$:

- Define
  \[
  \Phi:M\times G\to P,\qquad \Phi(x,g):=s(x)\cdot g.
  \]
- Then $\Phi$ is a $G$-equivariant diffeomorphism covering $\mathrm{id}_M$.
- Hence $P$ is isomorphic to the {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}} $M\times G$.

Conversely, the trivial bundle $M\times G\to M$ always has the canonical section $x\mapsto(x,e)$.

So:
\[
P \text{ is trivial } \Longleftrightarrow P \text{ admits a global smooth section.}
\]

## Counterexample (no global section)
The Hopf bundle $\pi:S^3\to S^2$ is a principal $U(1)$-bundle that admits **no** global smooth section, and therefore is nontrivial. Concretely, a section would give a $U(1)$-equivariant identification $S^3\cong S^2\times U(1)$, contradicting the known topology of $S^3$ and the nontrivial clutching of the bundle.

## Examples
1. **Hopf fibration.**  
   The {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}} has no global section, so it is not isomorphic to $S^2\times U(1)$.

2. **Circle base with disconnected structure group.**  
   Using the {{< knowl id="principal-bundle-over-s1-defined-by-a-clutching-function" text="clutching construction over the circle" >}} with $G=\mathrm{O}(1)=\{\pm1\}$ and gluing element $-1$ produces a nontrivial principal bundle over $S^1$; it has no global section.

3. **Trivial bundles always have sections.**  
   For any $M$ and $G$, the section $x\mapsto(x,e)$ exhibits $M\times G\to M$ as trivial.
