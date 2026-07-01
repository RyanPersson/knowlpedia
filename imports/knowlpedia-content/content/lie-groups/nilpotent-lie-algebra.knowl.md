+++
id = "lie-groups/nilpotent-lie-algebra"
title = "Nilpotent Lie algebra"
kind = "knowl"
summary = "A Lie algebra whose lower central series reaches zero after finitely many steps."
aliases = ["nilpotent-lie-algebra", "Nilpotent Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/nilpotent-lie-algebra.md"
+++

Let $\mathfrak g$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]].

The **lower central series** $\gamma_\bullet(\mathfrak g)$ is defined by $\gamma_1(\mathfrak g)=\mathfrak g$ and
$\gamma_{k+1}(\mathfrak g)=[\mathfrak g,\gamma_k(\mathfrak g)]$ (see [[lie-groups/lower-central-series-lie-algebra|lower central series]]).

The Lie algebra $\mathfrak g$ is **nilpotent** if there exists $s\ge 1$ such that
$$
\gamma_{s+1}(\mathfrak g)=0.
$$

The smallest such $s$ is the **nilpotency class** (or step).

## Immediate consequences
- $\gamma_2(\mathfrak g)=[\mathfrak g,\mathfrak g]$ is the [[lie-groups/derived-subalgebra|derived subalgebra]]; repeated commutators strictly decrease in size until they vanish.
- In any nonzero nilpotent Lie algebra, the [[lie-groups/center-of-a-lie-algebra|center]] is nontrivial (a standard structural feature used in many inductive arguments).
- Nilpotent implies [[lie-groups/solvable-lie-algebra|solvable]]; see [[lie-groups/nilpotent-implies-solvable-lemma|nilpotent implies solvable]].

## Examples
- The Heisenberg Lie algebra is nilpotent of step $2$; see [[lie-groups/example-heisenberg-algebra|the Heisenberg algebra]].
- Strictly upper triangular matrices form a nilpotent Lie algebra under commutator; see [[lie-groups/example-strictly-upper-triangular|strictly upper triangular matrices]].

## Context
Nilpotent Lie algebras are the infinitesimal counterparts of simply connected nilpotent Lie groups, where the [[lie-groups/exponential-map-lie-group|exponential map]] has especially strong global behavior and the [[lie-groups/baker-campbell-hausdorff-formula|BCH formula]] truncates after finitely many terms.
