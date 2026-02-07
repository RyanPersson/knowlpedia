---
title: "Theorem: Principal connections are equivalent to splittings of the Atiyah sequence"
description: "A principal connection is the same as a vector bundle splitting of the Atiyah sequence of a principal bundle."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure {{< knowl id="lie-group" text="Lie group" >}} $G$ and Lie algebra $\mathfrak g$.

The Atiyah sequence is the short exact sequence of vector bundles over $M$
\[
0\longrightarrow \operatorname{ad}(P)\longrightarrow TP/G \xrightarrow{\,a\,} TM \longrightarrow 0,
\]
where $a$ is induced by $d\pi$.

## Theorem

There is a natural bijection between:

- {{< knowl id="principal-connection" text="principal connections" >}} on $P$, and  
- vector bundle maps $s:TM\to TP/G$ such that $a\circ s=\mathrm{id}_{TM}$ (i.e. splittings of the Atiyah sequence).

Under this bijection:

- Given a principal connection with horizontal distribution $H\subset TP$, the splitting is the map $s_\omega$ obtained by taking horizontal lifts and passing to $TP/G$ (constructed in {{< knowl id="construction-splitting-of-atiyah-sequence-from-a-principal-connection" text="splitting from a principal connection" >}}).

- Given a splitting $s$, the corresponding horizontal distribution at $p\in P_x$ is the unique subspace $H_p\subset T_pP$ projecting isomorphically to $T_xM$ and representing the class $s(T_xM)\subset (TP/G)_x$; $G$-equivariance of $H$ follows from the definition of $TP/G$.

## Examples

1. **Trivial bundle.** For $P=M\times G$, the Atiyah algebroid is $TP/G\cong TM\oplus(M\times\mathfrak g)$. A splitting is a bundle map $TM\to TM\oplus(M\times\mathfrak g)$ of the form $v\mapsto (v,-A(v))$, hence corresponds to a $\mathfrak g$-valued $1$-form $A$, i.e. a connection.

2. **Frame bundle.** For $P=\mathrm{Fr}(E)$, splittings of the Atiyah sequence correspond to covariant derivatives on $E$ via the equivalence between principal connections on $\mathrm{Fr}(E)$ and vector bundle connections.

3. **Geometry via horizontals.** Interpreting a splitting as horizontals in $TP$ makes the existence/uniqueness of horizontal lifts and the construction of parallel transport immediate consequences of basic ODE theory on the principal bundle.
