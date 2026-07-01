+++
id = "thermodynamics/clausius-theorem-entropy"
title = "Clausius theorem and entropy"
kind = "knowl"
summary = "For reversible cycles, the cyclic integral ∮ δQ_rev/T vanishes, implying the existence of entropy as a state function with dS = δQ_rev/T."
aliases = ["clausius-theorem-entropy", "Clausius theorem and entropy"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/clausius-theorem-entropy.md"
+++

## Statement

For a system undergoing a **reversible** cyclic process through equilibrium states, the Clausius integral satisfies
$$
\oint \frac{\delta Q_{\mathrm{rev}}}{T} = 0.
$$

Consequently, there exists a state function $S$ (the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]]) such that for any two equilibrium states $A,B$ and any reversible path $\gamma$ from $A$ to $B$,
$$
S(B)-S(A) = \int_{\gamma} \frac{\delta Q_{\mathrm{rev}}}{T},
$$

so the integral is path independent among reversible paths and defines $S$ up to an additive constant.

More generally, for an arbitrary (possibly irreversible) cyclic process,
$$
\oint \frac{\delta Q}{T} \le 0,
$$
which is the [[thermodynamics/clausius-inequality|Clausius inequality]].

## Key hypotheses and conclusions

**Hypotheses**
- The process is quasi-static/reversible so that $T$ is well-defined along the path via [[thermodynamics/temperature-thermo|temperature]].
- The system passes through [[thermodynamics/thermodynamic-equilibrium|equilibrium]] states (so thermodynamic state variables are meaningful).
- The [[thermodynamics/second-law-thermodynamics|second law of thermodynamics]] holds.

**Conclusions**
- The differential form $\delta Q_{\mathrm{rev}}/T$ is an exact differential: $dS = \delta Q_{\mathrm{rev}}/T$ along reversible changes.
- Entropy differences are intrinsic to the endpoints (state function property).
- Irreversibility manifests as strict inequality in the cyclic Clausius integral and, equivalently, nonnegative entropy production.

## Cross-links to definitions

- Entropy: [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]].
- Temperature (integrating factor): [[thermodynamics/temperature-thermo|temperature]].
- Second-law context: [[thermodynamics/second-law-thermodynamics|second law]] and [[thermodynamics/kelvin-planck-clausius-equivalence|Kelvin–Planck–Clausius equivalence]].
- Mathematical structure (exactness/integrating factors): [[stat-mech/exact-differential-criterion|exact differential criterion]] and [[stat-mech/integrating-factor-lemma|integrating factor lemma]].
- Engine viewpoint connection: [[stat-mech/carnot-theorem|Carnot theorem]].
