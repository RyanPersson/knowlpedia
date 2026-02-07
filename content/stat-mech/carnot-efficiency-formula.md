---
title: "Carnot efficiency formula"
description: "For a reversible heat engine operating between reservoirs at temperatures T_H and T_C, the efficiency is η = 1 − T_C/T_H (absolute temperature scale)."
---

## Statement

Let a **reversible** cyclic heat engine operate between a hot reservoir at temperature $T_H$ and a cold reservoir at temperature $T_C$, with $T_H>T_C>0$. If $Q_H>0$ is the heat absorbed from the hot reservoir per cycle and $Q_C>0$ is the heat rejected to the cold reservoir per cycle, then the efficiency is
$$
\eta_{\mathrm{rev}} = 1-\frac{Q_C}{Q_H}.
$$

On the absolute thermodynamic temperature scale, a reversible engine satisfies
$$
\frac{Q_C}{Q_H} = \frac{T_C}{T_H},
\qquad\text{hence}\qquad
\eta_{\mathrm{rev}} = 1-\frac{T_C}{T_H}.
$$

## Key hypotheses and conclusions

**Hypotheses**
- The engine is reversible (no entropy production; it can be run backward as a refrigerator without additional dissipation).
- Heat exchange occurs only with two reservoirs at fixed temperatures $T_H$ and $T_C$.
- Temperatures are interpreted as {{< knowl id="temperature-thermo" section="thermodynamics" text="thermodynamic temperatures" >}} on an absolute scale (see below).

**Conclusions**
- The reversible efficiency depends only on the temperature ratio $T_C/T_H$.
- By {{< knowl id="carnot-theorem" text="Carnot’s theorem" >}}, every engine between the same reservoirs satisfies $\eta\le 1-T_C/T_H$.

## Cross-links to definitions

- Reservoir temperatures: {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- Second-law input: {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law of thermodynamics" >}}.
- Universality/maximality: {{< knowl id="carnot-theorem" text="Carnot theorem" >}}.
- Entropy formulation: {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}} and {{< knowl id="clausius-theorem-entropy" section="thermodynamics" text="Clausius’ theorem" >}}.
- Absolute scale consequence: {{< knowl id="corollary-carnot-absolute-temperature" section="thermodynamics" text="Carnot absolute temperature corollary" >}}.

**Significance.** This is the canonical “thermodynamic limit” on efficiency: it quantifies why making $T_C$ small and $T_H$ large is the only way (even ideally) to improve efficiency, and it pins down the operational meaning of the absolute temperature scale.
