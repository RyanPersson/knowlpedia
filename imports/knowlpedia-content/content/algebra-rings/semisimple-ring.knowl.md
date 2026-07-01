+++
id = "algebra-rings/semisimple-ring"
title = "Semisimple ring"
kind = "knowl"
summary = "A ring whose module theory is completely reducible; equivalently a finite product of matrix rings over division rings."
aliases = ["semisimple-ring", "Semisimple ring"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/semisimple-ring.md"
+++

A **semisimple ring** is a unital ring $R$ such that every left $R$-module is semisimple (i.e. a direct sum of simple modules). Equivalently, the left regular module ${}_RR$ is a direct sum of minimal left ideals.

In structural terms, semisimple rings are exactly those described by the [[algebra-rings/artin-wedderburn-theorem|Artin–Wedderburn theorem]]: they are finite products of [[algebra-rings/matrix-ring|matrix rings]] over [[algebra-rings/division-ring|division rings]]. A key obstruction to semisimplicity is the [[algebra-rings/jacobson-radical|Jacobson radical]], which vanishes for semisimple rings.

**Examples:**
- $M_n(k)$ is semisimple for any field $k$ and integer $n\ge 1$.
- $M_2(\mathbb{Q})\times \mathbb{Q}$ is semisimple.
- The ring $k[x]/(x^2)$ is not semisimple: the class of $x$ is nonzero but nilpotent, forcing a nontrivial Jacobson radical.
