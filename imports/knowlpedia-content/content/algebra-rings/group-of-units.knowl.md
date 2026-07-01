+++
id = "algebra-rings/group-of-units"
title = "Group of units"
kind = "knowl"
summary = "The multiplicative group consisting of all units in a unital ring."
aliases = ["group-of-units", "Group of units"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/group-of-units.md"
+++

For a unital ring $R$, the **group of units** is
\[
R^\times=\{u\in R: u \text{ is a unit}\}
\]
with operation given by multiplication in $R$. This is a [[algebra-groups/group|group]], and it consists exactly of the [[algebra-rings/unit|units]] of $R$.

The unit group is functorial: a unital ring homomorphism sends units to units. In noncommutative settings, unit groups encode significant structure (e.g. general linear groups).

**Examples:**
- $\mathbb Z^\times=\{\pm 1\}$.
- $(\mathbb Z/n\mathbb Z)^\times$ is the group of residue classes coprime to $n$.
- $M_n(k)^\times$ is the group $\mathrm{GL}_n(k)$ of invertible matrices.
