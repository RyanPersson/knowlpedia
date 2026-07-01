+++
id = "lie-groups/normal-lie-subgroup"
title = "Normal Lie subgroup"
kind = "knowl"
summary = "A Lie subgroup invariant under conjugation; infinitesimally, it corresponds to an ideal."
aliases = ["normal-lie-subgroup", "Normal Lie subgroup"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/normal-lie-subgroup.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]].

A [[lie-groups/lie-subgroup|Lie subgroup]] $N\subseteq G$ is **normal** if
$$
gNg^{-1}=N \quad \text{for all } g\in G,
$$

i.e. $N$ is invariant under the [[lie-groups/conjugation-action-of-a-lie-group|conjugation action]] of $G$ on itself.

## Infinitesimal characterization
Let $\mathfrak g=\operatorname{Lie}(G)$ and $\mathfrak n=\operatorname{Lie}(N)$ (viewed inside $\mathfrak g$ using [[lie-groups/lie-algebra-of-subgroup-lemma|the subgroup Lie algebra lemma]]). Then:
- If $N$ is normal in $G$, $\mathfrak n$ is an [[lie-groups/ideal-lie-algebra|ideal]] in $\mathfrak g$.
- Conversely, if $G$ is connected and $\mathfrak n$ is an ideal, then the connected subgroup integrating $\mathfrak n$ (via the [[lie-groups/lie-correspondence|Lie correspondence]]) is normal in $G$.

## Quotients
If $N$ is **closed** and normal, then the quotient set $G/N$ carries a natural structure of [[lie-groups/quotient-lie-group|Lie group quotient]], and its Lie algebra is the [[lie-groups/quotient-lie-algebra|quotient Lie algebra]]
$$
\operatorname{Lie}(G/N)\cong \mathfrak g/\mathfrak n.
$$

## Context
Normal Lie subgroups are the geometric mechanism for building new Lie groups from old ones by quotienting, while ideals play the parallel role on the Lie algebra side.
