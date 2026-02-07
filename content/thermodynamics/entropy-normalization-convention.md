---
title: "Entropy normalization convention"
description: "Specifies the units and reference point for entropy, and its link to information-theoretic entropy."
---

## Definition and what “normalization” fixes

The {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}} $S$ is a {{< knowl id="state-function" text="state function" >}} determined (macroscopically) by the {{< knowl id="second-law-thermodynamics" text="second law" >}} up to choices that do not affect measurable entropy *changes*. An “entropy normalization” convention fixes:

1. **Units / scale factor** (whether $S$ is dimensional or scaled by a constant), and  
2. **Additive constant** (the reference point for “absolute” entropy).

## Convention used in this blog

- **Logarithm choice:** we use the natural logarithm as stated in {{< knowl id="logarithm-convention-natural" text="the logarithm convention" >}}. Changing the log base rescales entropy by a constant factor.

- **Boltzmann constant explicit by default:** entropy is treated as a physical quantity with units of energy per temperature, keeping {{< knowl id="boltzmann-constant" text="$k_B$" >}} explicit unless {{< knowl id="natural-units-convention" text="natural units" >}} are declared.

- **Statistical-mechanical normalization (discrete states):** for microstates with probabilities $p_i$, we take the Gibbs/Shannon-form normalization
  $$
  S = -k_B \sum_i p_i \ln p_i.
  $$

  The dimensionless quantity $-\sum_i p_i \ln p_i$ is the {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}} (in nats under our log choice), and the thermodynamic entropy is obtained by multiplying by $k_B$.

  In the microcanonical special case ($p_i=1/\Omega$ on $\Omega$ accessible states), this reduces to the Boltzmann form $S=k_B \ln \Omega$.

- **Absolute reference (third law):** to fix the additive constant, we adopt the {{< knowl id="third-law-thermodynamics" text="third-law" >}} convention: for a perfect crystal with a nondegenerate ground state, $S\to 0$ as $T\to 0$. More generally, a residual ground-state degeneracy $g$ corresponds to $S(T\to 0)=k_B \ln g$.

## Key implications and useful checks

- **Only differences matter in most thermodynamics:** statements like the {{< knowl id="clausius-inequality" text="Clausius inequality" >}} constrain $\Delta S$ and do not depend on the absolute constant.

- **Dimensionless entropy in natural units:** if {{< knowl id="natural-units-convention" text="$k_B=1$ units" >}} are used, $S$ becomes dimensionless and temperature has energy units; the {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}} $\beta$ is then simply $1/T$.

- **Connection to relative entropy:** with this normalization, entropy differences and free-energy inequalities can often be expressed using {{< knowl id="relative-entropy-kl-divergence" section="probability" text="Kullback–Leibler divergence" >}} (a dimensionless measure), with factors of $k_B$ restoring thermodynamic units.
