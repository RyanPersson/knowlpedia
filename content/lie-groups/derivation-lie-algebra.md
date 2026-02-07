---
title: "Derivation of a Lie algebra"
description: "A linear map with ; derivations form a Lie algebra containing the inner derivations."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}} over a field of characteristic $0$ (typically $\mathbb R$ or $\mathbb C$).

A **derivation** of $\mathfrak g$ is a linear map $D:\mathfrak g\to\mathfrak g$ such that for all $x,y\in\mathfrak g$,
\[
D([x,y]) \;=\; [D x, y] + [x, D y].
\]
The space of derivations is denoted $\mathrm{Der}(\mathfrak g)$.

## Lie algebra structure
With bracket given by the commutator of endomorphisms,
\[
[D_1,D_2] := D_1\circ D_2 - D_2\circ D_1,
\]
the space $\mathrm{Der}(\mathfrak g)$ is a Lie subalgebra of $\mathfrak{gl}(\mathfrak g)$.

## Inner vs. outer
For each $x\in\mathfrak g$, the adjoint map $\mathrm{ad}_x:\mathfrak g\to\mathfrak g$, $\mathrm{ad}_x(y)=[x,y]$, is a derivation; these are the **inner derivations** (see {{< knowl id="inner-derivation" text="inner derivation" >}}). The assignment $x\mapsto \mathrm{ad}_x$ is the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}}.

Derivations not of the form $\mathrm{ad}_x$ are called **outer** (see {{< knowl id="outer-derivation" text="outer derivation" >}}); they measure failure of $\mathrm{ad}(\mathfrak g)$ to exhaust all infinitesimal symmetries.

## Motivation
Derivations are the infinitesimal analog of {{< knowl id="lie-algebra-automorphism" text="Lie algebra automorphisms" >}}: if $\varphi_t$ is a smooth 1-parameter family of automorphisms with $\varphi_0=\mathrm{id}$, then $\frac{d}{dt}\big|_{t=0}\varphi_t$ is a derivation.
