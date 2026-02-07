---
title: "Cyclic process"
description: "A process that returns a system to its initial thermodynamic state after a sequence of transformations."
---

A **cyclic process** is a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}} in which the system undergoes a sequence of changes and finally returns to its initial {{< knowl id="thermodynamic-state" text="thermodynamic state" >}}. In state space, the path is closed.

## Physical interpretation
Cycles model devices designed for repeated operation—heat engines, refrigerators, and heat pumps—where the working substance returns to its starting state each run while exchanging energy with reservoirs and delivering (or consuming) net work. The logical constraints of the {{< knowl id="second-law-thermodynamics" text="second law" >}} on such devices are often phrased as the {{< knowl id="kelvin-planck-statement" text="Kelvin–Planck statement" >}} and the {{< knowl id="clausius-statement-second-law" text="Clausius statement" >}}.

## Key properties and relations
Because the initial and final states coincide, every {{< knowl id="state-function" text="state function" >}} has zero net change over a cycle:
$$
\oint dX = 0.
$$

In particular, for the {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$,
$$
\oint dU = 0.
$$
Combining this with the differential form of the {{< knowl id="first-law-thermodynamics" text="first law" >}} yields the net balance between heat and work over a cycle:
$$
\oint \delta Q = \oint \delta W,
$$

with the sign of $\delta W$ determined by the {{< knowl id="work-sign-convention" text="work sign convention" >}}.

Since heat and work are {{< knowl id="path-function" text="path functions" >}}, their cyclic integrals need not vanish even though the system returns to its original state.

If the cycle is {{< knowl id="quasistatic-process" text="quasistatic" >}} and the only mechanical work is boundary work, the net work can be written in terms of the {{< knowl id="pressure-thermo" text="pressure" >}} $P$ and {{< knowl id="volume-thermo" text="volume" >}} $V$ as
$$
W = \oint P\,dV,
$$

interpreted with the {{< knowl id="pressure-volume-work-sign-convention" text="$P\,dV$ sign convention" >}}; geometrically, this equals the signed area enclosed by the loop in the $P$–$V$ plane.

## Second-law constraint on cycles
For any cyclic process, the {{< knowl id="clausius-inequality" text="Clausius inequality" >}} implies
$$
\oint \frac{\delta Q}{T_{\mathrm{b}}} \le 0,
$$
with equality if and only if the cycle is {{< knowl id="reversible-process" text="reversible" >}}. Strict inequality signals an {{< knowl id="irreversible-process" text="irreversible" >}} cycle with positive net entropy production in the combined system and environment.
