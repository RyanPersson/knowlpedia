---
title: "Carnot theorem"
description: "No heat engine operating between two reservoirs can be more efficient than a reversible one; all reversible engines between the same reservoirs have the same efficiency."
---

## Statement

Consider a cyclic heat engine that exchanges heat only with two thermal reservoirs, a hot reservoir and a cold reservoir, at fixed temperatures $T_H>T_C$. Let $Q_H>0$ be the heat absorbed from the hot reservoir per cycle, $Q_C>0$ the heat rejected to the cold reservoir per cycle, and $W=Q_H-Q_C$ the work output per cycle. The efficiency is
$$
\eta := \frac{W}{Q_H} = 1-\frac{Q_C}{Q_H}.
$$

**Carnot theorem** asserts:

1. **Maximality of reversible efficiency.** For any (possibly irreversible) engine operating between the same two reservoirs,
   $$
   \eta \le \eta_{\mathrm{rev}}(T_H,T_C),
   $$

   where $\eta_{\mathrm{rev}}(T_H,T_C)$ is the efficiency of a reversible engine between those reservoirs.

2. **Universality among reversible engines.** Any two reversible engines operating between the same two reservoirs have the same efficiency. Equivalently, $\eta_{\mathrm{rev}}$ depends only on the reservoir temperatures (and not on the working substance or details of the cycle).

## Key hypotheses and conclusions

**Hypotheses**
- A cyclic device (engine) interacting with exactly two reservoirs at fixed temperatures (hot and cold).
- The engine’s working body is always in (or can be idealized as passing through) {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}} states.
- The {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law of thermodynamics" >}} holds (in any standard formulation; see equivalence below).

**Conclusions**
- No engine between $(T_H,T_C)$ can exceed the efficiency of a reversible one.
- Reversible efficiency is a function only of $(T_H,T_C)$; this underlies the absolute temperature scale and leads to the explicit {{< knowl id="carnot-efficiency-formula" text="Carnot efficiency formula" >}}.

## Cross-links to definitions

- Reservoir temperatures use the thermodynamic notion of {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- The directionality constraint is encoded by the {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law" >}}, and the equivalence of standard formulations is summarized in {{< knowl id="kelvin-planck-clausius-equivalence" section="thermodynamics" text="Kelvin–Planck–Clausius equivalence" >}}.
- The entropy viewpoint connects via {{< knowl id="clausius-theorem-entropy" section="thermodynamics" text="Clausius’ theorem (entropy)" >}} and the {{< knowl id="clausius-inequality" section="thermodynamics" text="Clausius inequality" >}}.
- The induced absolute scale is captured in {{< knowl id="corollary-carnot-absolute-temperature" section="thermodynamics" text="Carnot’s corollary on absolute temperature" >}}.

**Significance.** Carnot’s theorem isolates a universal performance bound for heat engines, independent of microscopic details, and is the starting point for defining absolute temperature and entropy in macroscopic thermodynamics.