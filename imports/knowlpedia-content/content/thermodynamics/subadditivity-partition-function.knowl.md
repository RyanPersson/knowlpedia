+++
id = "thermodynamics/subadditivity-partition-function"
title = "Subadditivity of the Partition Function (up to boundary terms)"
kind = "knowl"
summary = "Upper bound relating the finite-volume partition function of a union to the product of partition functions of parts, with a boundary correction."
aliases = ["subadditivity-partition-function", "Subadditivity of the Partition Function (up to boundary terms)"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/subadditivity-partition-function.md"
+++

This lemma concerns the finite-volume partition function associated with a [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]] and the corresponding [[stat-mech-lattice/partition-function-lattice|lattice partition function]].

## Statement
Let $\Lambda_1,\Lambda_2\subset \mathbb{Z}^d$ be **disjoint** finite regions. Write the finite-volume Hamiltonian on $\Lambda_1\cup\Lambda_2$ as
$$
H_{\Lambda_1\cup\Lambda_2}(\sigma)
= H_{\Lambda_1}(\sigma) + H_{\Lambda_2}(\sigma) + H_{\mathrm{cross}}(\sigma),
$$

where $H_{\mathrm{cross}}$ contains the interaction terms that involve sites in both $\Lambda_1$ and $\Lambda_2$.

Assume there is a constant $C\ge 0$ such that for all configurations $\sigma$,
$$
H_{\mathrm{cross}}(\sigma)\ge -\, C\,|\partial(\Lambda_1,\Lambda_2)|,
$$

where $|\partial(\Lambda_1,\Lambda_2)|$ counts the interaction terms (e.g. edges/plaquettes/hyperedges, depending on the model) that “cross” between $\Lambda_1$ and $\Lambda_2$.

Then for every inverse temperature $\beta\ge 0$,
$$
\log Z_{\Lambda_1\cup\Lambda_2}(\beta)
\le \log Z_{\Lambda_1}(\beta) + \log Z_{\Lambda_2}(\beta) + \beta C\,|\partial(\Lambda_1,\Lambda_2)|.
$$

Equivalently,
$$
Z_{\Lambda_1\cup\Lambda_2}(\beta)
\le e^{\beta C|\partial(\Lambda_1,\Lambda_2)|}\, Z_{\Lambda_1}(\beta)\, Z_{\Lambda_2}(\beta).
$$

## Key hypotheses and conclusions
**Hypotheses**
- $\Lambda_1,\Lambda_2$ are disjoint finite volumes.
- The interaction across the interface is uniformly bounded from below by a constant times a boundary size:
  $H_{\mathrm{cross}}(\sigma)\ge -C|\partial(\Lambda_1,\Lambda_2)|$.
  (This holds, for example, for finite-range, uniformly bounded interactions.)

**Conclusions**
- $\log Z_\Lambda$ is **subadditive up to a boundary correction**.
- For “regular” shapes (e.g. cubes), $|\partial(\Lambda_1,\Lambda_2)|$ grows like surface area, so the correction is lower order compared to volume.
This estimate is a standard input to proving existence of the thermodynamic limit of the lattice pressure
([[stat-mech-lattice/pressure-lattice|pressure]])
via subadditivity arguments and [[stat-mech/fekete-lemma|Fekete's lemma]],
as used in [[thermodynamics/thermodynamic-limit-pressure-existence|existence of the thermodynamic pressure]].
