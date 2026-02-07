---
title: "Normal Lie subgroup"
description: "A Lie subgroup invariant under conjugation; infinitesimally, it corresponds to an ideal."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}.

A {{< knowl id="lie-subgroup" text="Lie subgroup" >}} $N\subseteq G$ is **normal** if
$$
gNg^{-1}=N \quad \text{for all } g\in G,
$$

i.e. $N$ is invariant under the {{< knowl id="conjugation-action-of-a-lie-group" text="conjugation action" >}} of $G$ on itself.

## Infinitesimal characterization
Let $\mathfrak g=\operatorname{Lie}(G)$ and $\mathfrak n=\operatorname{Lie}(N)$ (viewed inside $\mathfrak g$ using {{< knowl id="lie-algebra-of-subgroup-lemma" text="the subgroup Lie algebra lemma" >}}). Then:
- If $N$ is normal in $G$, $\mathfrak n$ is an {{< knowl id="ideal-lie-algebra" text="ideal" >}} in $\mathfrak g$.
- Conversely, if $G$ is connected and $\mathfrak n$ is an ideal, then the connected subgroup integrating $\mathfrak n$ (via the {{< knowl id="lie-correspondence" text="Lie correspondence" >}}) is normal in $G$.

## Quotients
If $N$ is **closed** and normal, then the quotient set $G/N$ carries a natural structure of {{< knowl id="quotient-lie-group" text="Lie group quotient" >}}, and its Lie algebra is the {{< knowl id="quotient-lie-algebra" text="quotient Lie algebra" >}}
$$
\operatorname{Lie}(G/N)\cong \mathfrak g/\mathfrak n.
$$

## Context
Normal Lie subgroups are the geometric mechanism for building new Lie groups from old ones by quotienting, while ideals play the parallel role on the Lie algebra side.
