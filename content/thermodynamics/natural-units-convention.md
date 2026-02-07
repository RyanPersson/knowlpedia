---
title: "Natural units convention"
description: "Convention (often ) that measures temperature in energy units and treats entropy as dimensionless, simplifying statistical-mechanical formulas."
---

## Definition (and physical meaning)

The **natural units convention** in thermodynamics/statistical mechanics is the choice of units in which the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} is set to unity:
$$
k_B = 1.
$$

With this convention, {{< knowl id="temperature-thermo" text="temperature" >}} has the same units as energy, and the thermodynamic {{< knowl id="thermodynamic-entropy" text="entropy" >}} is naturally treated as a **dimensionless** quantity (because it is really $S/k_B$ that appears as a logarithm).

**Physical interpretation:** the constant $k_B$ is not “removed” from physics; it is absorbed into the unit choice so that thermal energy scales are measured directly in temperature units (or vice versa).

## Practical consequences

- **Inverse temperature simplifies.** The {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}} becomes
  $$
  \beta=\frac{1}{T}.
  $$

- **Entropy is a pure number.** Statements like “entropy is the logarithm of the number of accessible microstates” become literally true in formulas: $S=\ln \Omega$ (rather than $S=k_B\ln\Omega$). Restoring SI units is done by multiplying by $k_B$ at the end.

- **Free energies and partition functions look cleaner.** For example, the canonical relation
  $$
  F=-k_B T\ln Z
  $$

  becomes simply $F=-T\ln Z$.

## Conventions you must keep consistent

Natural units are usually paired with a specific logarithm convention, often {{< knowl id="logarithm-convention-natural" text="natural logarithms" >}} so that entropies are in “nats.” If you instead use $\log_2$, then restoring thermodynamic units requires an extra factor of $\ln 2$, consistent with the chosen {{< knowl id="entropy-normalization-convention" text="entropy normalization convention" >}}.

## Restoring dimensions (rule of thumb)

If a formula in natural units contains $T$ multiplying an entropy-like quantity, reinsert $k_B$ so that $k_B T$ carries units of energy and $S$ carries units of J/K in conventional thermodynamics.
