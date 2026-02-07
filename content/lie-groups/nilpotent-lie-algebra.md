---
title: "Nilpotent Lie algebra"
description: "A Lie algebra whose lower central series reaches zero after finitely many steps."
---

Let $\mathfrak g$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}}.

The **lower central series** $\gamma_\bullet(\mathfrak g)$ is defined by $\gamma_1(\mathfrak g)=\mathfrak g$ and
$\gamma_{k+1}(\mathfrak g)=[\mathfrak g,\gamma_k(\mathfrak g)]$ (see {{< knowl id="lower-central-series-lie-algebra" text="lower central series" >}}).

The Lie algebra $\mathfrak g$ is **nilpotent** if there exists $s\ge 1$ such that
$$
\gamma_{s+1}(\mathfrak g)=0.
$$

The smallest such $s$ is the **nilpotency class** (or step).

## Immediate consequences
- $\gamma_2(\mathfrak g)=[\mathfrak g,\mathfrak g]$ is the {{< knowl id="derived-subalgebra" text="derived subalgebra" >}}; repeated commutators strictly decrease in size until they vanish.
- In any nonzero nilpotent Lie algebra, the {{< knowl id="center-of-a-lie-algebra" text="center" >}} is nontrivial (a standard structural feature used in many inductive arguments).
- Nilpotent implies {{< knowl id="solvable-lie-algebra" text="solvable" >}}; see {{< knowl id="nilpotent-implies-solvable-lemma" text="nilpotent implies solvable" >}}.

## Examples
- The Heisenberg Lie algebra is nilpotent of step $2$; see {{< knowl id="example-heisenberg-algebra" text="the Heisenberg algebra" >}}.
- Strictly upper triangular matrices form a nilpotent Lie algebra under commutator; see {{< knowl id="example-strictly-upper-triangular" text="strictly upper triangular matrices" >}}.

## Context
Nilpotent Lie algebras are the infinitesimal counterparts of simply connected nilpotent Lie groups, where the {{< knowl id="exponential-map-lie-group" text="exponential map" >}} has especially strong global behavior and the {{< knowl id="baker-campbell-hausdorff-formula" text="BCH formula" >}} truncates after finitely many terms.
