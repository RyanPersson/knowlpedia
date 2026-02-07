---
title: "Clausius theorem and entropy"
description: "For reversible cycles, the cyclic integral ∮ δQ_rev/T vanishes, implying the existence of entropy as a state function with dS = δQ_rev/T."
---

## Statement

For a system undergoing a **reversible** cyclic process through equilibrium states, the Clausius integral satisfies
$$
\oint \frac{\delta Q_{\mathrm{rev}}}{T} = 0.
$$

Consequently, there exists a state function $S$ (the {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}) such that for any two equilibrium states $A,B$ and any reversible path $\gamma$ from $A$ to $B$,
$$
S(B)-S(A) = \int_{\gamma} \frac{\delta Q_{\mathrm{rev}}}{T},
$$

so the integral is path independent among reversible paths and defines $S$ up to an additive constant.

More generally, for an arbitrary (possibly irreversible) cyclic process,
$$
\oint \frac{\delta Q}{T} \le 0,
$$
which is the {{< knowl id="clausius-inequality" section="thermodynamics" text="Clausius inequality" >}}.

## Key hypotheses and conclusions

**Hypotheses**
- The process is quasi-static/reversible so that $T$ is well-defined along the path via {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- The system passes through {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="equilibrium" >}} states (so thermodynamic state variables are meaningful).
- The {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law of thermodynamics" >}} holds.

**Conclusions**
- The differential form $\delta Q_{\mathrm{rev}}/T$ is an exact differential: $dS = \delta Q_{\mathrm{rev}}/T$ along reversible changes.
- Entropy differences are intrinsic to the endpoints (state function property).
- Irreversibility manifests as strict inequality in the cyclic Clausius integral and, equivalently, nonnegative entropy production.

## Cross-links to definitions

- Entropy: {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}.
- Temperature (integrating factor): {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- Second-law context: {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law" >}} and {{< knowl id="kelvin-planck-clausius-equivalence" text="Kelvin–Planck–Clausius equivalence" >}}.
- Mathematical structure (exactness/integrating factors): {{< knowl id="exact-differential-criterion" section="stat-mech" text="exact differential criterion" >}} and {{< knowl id="integrating-factor-lemma" section="stat-mech" text="integrating factor lemma" >}}.
- Engine viewpoint connection: {{< knowl id="carnot-theorem" section="stat-mech" text="Carnot theorem" >}}.

