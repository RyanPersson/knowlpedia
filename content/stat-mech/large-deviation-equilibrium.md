---
title: "Equilibrium as a large-deviation minimizer"
description: "If macroscopic variables satisfy a large-deviation principle, equilibrium states are characterized as minimizers of the rate function (or maximizers of an entropy functional)."
---

## Statement (LDP characterization of equilibrium)
Let $(M_N)_{N\ge 1}$ be a sequence of macroscopic observables (order parameters, empirical measures, energy density, etc.) taking values in a topological space $\mathcal M$. Suppose under a sequence of probability measures $(\mathbb P_N)$ (e.g. finite-volume Gibbs measures) the variables $M_N$ satisfy a {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}} with speed $N$ and good {{< knowl id="rate-function" section="large-deviations" text="rate function" >}} $I:\mathcal M\to[0,\infty]$:
\[
\mathbb P_N(M_N\in B)\approx \exp\big(-N\inf_{m\in B} I(m)\big).
\]

Then:
1. Any limit point of $M_N$ (in probability) lies in the set of global minimizers of $I$.
2. If $I$ has a unique minimizer $m^*$, then $M_N\to m^*$ in probability and equilibrium is unique at the macroscopic level.
3. Multiple minimizers of $I$ correspond to macroscopic coexistence (possible symmetry breaking / phase coexistence).

In canonical settings, if the LDP can be written in the form
\[
I_\beta(m)=\beta\,\Phi(m)-S(m)+\text{constant},
\]
then equilibrium macrostates maximize $S(m)-\beta\Phi(m)$ (a “maximum entropy minus energy” principle), matching the variational structure of the {{< knowl id="gibbs-variational-principle" text="Gibbs variational principle" >}}.

## Key hypotheses
- Existence of an LDP for $M_N$ under the measures of interest.
- Exponential tightness / compactness conditions ensuring a good rate function.
- When using the variational representation of thermodynamic potentials: applicability of {{< knowl id="varadhans-lemma" section="large-deviations" text="Varadhan’s lemma" >}} (or an appropriate Laplace principle).

## Conclusions
- **Equilibrium = minimizers:** typical macrostates are precisely the minimizers of the rate function.
- **Fluctuation scale:** deviations away from equilibrium have probabilities decaying like $\exp(-N\times\text{cost})$.
- **Phase transitions (macro):** nonuniqueness or non-smooth changes in minimizers signal phase transitions.

## Cross-links to definitions
- Large deviations: {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}}, {{< knowl id="rate-function" section="large-deviations" text="rate function" >}}, {{< knowl id="varadhans-lemma" section="large-deviations" text="Varadhan’s lemma" >}}.
- Statistical mechanics context: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="free-energy-statistical" section="stat-mech" text="free energy (statistical)" >}}.

