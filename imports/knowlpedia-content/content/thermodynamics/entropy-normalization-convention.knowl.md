+++
id = "thermodynamics/entropy-normalization-convention"
title = "Entropy normalization convention"
kind = "knowl"
summary = "Specifies the units and reference point for entropy, and its link to information-theoretic entropy."
aliases = ["entropy-normalization-convention", "Entropy normalization convention"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/entropy-normalization-convention.md"
+++

## Definition and what “normalization” fixes

The [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] $S$ is a [[thermodynamics/state-function|state function]] determined (macroscopically) by the [[thermodynamics/second-law-thermodynamics|second law]] up to choices that do not affect measurable entropy *changes*. An “entropy normalization” convention fixes:

1. **Units / scale factor** (whether $S$ is dimensional or scaled by a constant), and
2. **Additive constant** (the reference point for “absolute” entropy).

## Convention used in this blog

- **Logarithm choice:** we use the natural logarithm as stated in [[thermodynamics/logarithm-convention-natural|the logarithm convention]]. Changing the log base rescales entropy by a constant factor.

- **Boltzmann constant explicit by default:** entropy is treated as a physical quantity with units of energy per temperature, keeping [[thermodynamics/boltzmann-constant|$k_B$]] explicit unless [[thermodynamics/natural-units-convention|natural units]] are declared.

- **Statistical-mechanical normalization (discrete states):** for microstates with probabilities $p_i$, we take the Gibbs/Shannon-form normalization
  $$
  S = -k_B \sum_i p_i \ln p_i.
  $$

  The dimensionless quantity $-\sum_i p_i \ln p_i$ is the [[probability/shannon-entropy|Shannon entropy]] (in nats under our log choice), and the thermodynamic entropy is obtained by multiplying by $k_B$.

  In the microcanonical special case ($p_i=1/\Omega$ on $\Omega$ accessible states), this reduces to the Boltzmann form $S=k_B \ln \Omega$.

- **Absolute reference (third law):** to fix the additive constant, we adopt the [[thermodynamics/third-law-thermodynamics|third-law]] convention: for a perfect crystal with a nondegenerate ground state, $S\to 0$ as $T\to 0$. More generally, a residual ground-state degeneracy $g$ corresponds to $S(T\to 0)=k_B \ln g$.

## Key implications and useful checks

- **Only differences matter in most thermodynamics:** statements like the [[thermodynamics/clausius-inequality|Clausius inequality]] constrain $\Delta S$ and do not depend on the absolute constant.

- **Dimensionless entropy in natural units:** if [[thermodynamics/natural-units-convention|$k_B=1$ units]] are used, $S$ becomes dimensionless and temperature has energy units; the [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta$ is then simply $1/T$.

- **Connection to relative entropy:** with this normalization, entropy differences and free-energy inequalities can often be expressed using [[probability/relative-entropy-kl-divergence|Kullback–Leibler divergence]] (a dimensionless measure), with factors of $k_B$ restoring thermodynamic units.
