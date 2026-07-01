+++
id = "thermodynamics/cyclic-process"
title = "Cyclic process"
kind = "knowl"
summary = "A process that returns a system to its initial thermodynamic state after a sequence of transformations."
aliases = ["cyclic-process", "Cyclic process"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/cyclic-process.md"
+++

A **cyclic process** is a [[thermodynamics/thermodynamic-process|thermodynamic process]] in which the system undergoes a sequence of changes and finally returns to its initial [[thermodynamics/thermodynamic-state|thermodynamic state]]. In state space, the path is closed.

## Physical interpretation
Cycles model devices designed for repeated operation—heat engines, refrigerators, and heat pumps—where the working substance returns to its starting state each run while exchanging energy with reservoirs and delivering (or consuming) net work. The logical constraints of the [[thermodynamics/second-law-thermodynamics|second law]] on such devices are often phrased as the [[thermodynamics/kelvin-planck-statement|Kelvin–Planck statement]] and the [[thermodynamics/clausius-statement-second-law|Clausius statement]].

## Key properties and relations
Because the initial and final states coincide, every [[thermodynamics/state-function|state function]] has zero net change over a cycle:
$$
\oint dX = 0.
$$

In particular, for the [[thermodynamics/internal-energy-thermo|internal energy]] $U$,
$$
\oint dU = 0.
$$
Combining this with the differential form of the [[thermodynamics/first-law-thermodynamics|first law]] yields the net balance between heat and work over a cycle:
$$
\oint \delta Q = \oint \delta W,
$$

with the sign of $\delta W$ determined by the [[thermodynamics/work-sign-convention|work sign convention]].

Since heat and work are [[thermodynamics/path-function|path functions]], their cyclic integrals need not vanish even though the system returns to its original state.

If the cycle is [[thermodynamics/quasistatic-process|quasistatic]] and the only mechanical work is boundary work, the net work can be written in terms of the [[thermodynamics/pressure-thermo|pressure]] $P$ and [[thermodynamics/volume-thermo|volume]] $V$ as
$$
W = \oint P\,dV,
$$

interpreted with the [[thermodynamics/pressure-volume-work-sign-convention|$P\,dV$ sign convention]]; geometrically, this equals the signed area enclosed by the loop in the $P$–$V$ plane.

## Second-law constraint on cycles
For any cyclic process, the [[thermodynamics/clausius-inequality|Clausius inequality]] implies
$$
\oint \frac{\delta Q}{T_{\mathrm{b}}} \le 0,
$$
with equality if and only if the cycle is [[thermodynamics/reversible-process|reversible]]. Strict inequality signals an [[thermodynamics/irreversible-process|irreversible]] cycle with positive net entropy production in the combined system and environment.
