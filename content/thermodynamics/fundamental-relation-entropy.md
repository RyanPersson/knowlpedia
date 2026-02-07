---
title: "Fundamental relation (entropy representation)"
description: "The entropy function S(U,V,N,...) that encodes all equilibrium thermodynamics via its derivatives and concavity."
---

In the **entropy representation**, the **fundamental relation** is the equilibrium entropy expressed as a function of the extensive variables:
$S = S(U,V,N,\dots)$,
where $U$ is {{< knowl id="internal-energy-thermo" text="internal energy" >}}, $V$ is {{< knowl id="volume-thermo" text="volume" >}}, and $N$ is {{< knowl id="particle-number" text="particle number" >}} (and possibly other conserved extensive quantities). This single state function determines the equations of state and all response functions for systems in {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}.

**Physical interpretation.** The function $S(U,V,N,\dots)$ counts (macroscopically) how many microscopic configurations are compatible with macroscopic constraints; its derivatives define the intensive “forces” that drive exchange with the {{< knowl id="surroundings-environment" text="surroundings" >}}.

**Generating derivatives.** The differential form of the fundamental relation is
$$
dS = \frac{1}{T}\,dU + \frac{P}{T}\,dV - \frac{\mu}{T}\,dN + \cdots ,
$$
which *defines* the intensive variables as partial derivatives:
- $\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N,\dots}$ with {{< knowl id="temperature-thermo" text="temperature" >}}
- $\frac{P}{T} = \left(\frac{\partial S}{\partial V}\right)_{U,N,\dots}$ with {{< knowl id="pressure-thermo" text="pressure" >}}
- $-\frac{\mu}{T} = \left(\frac{\partial S}{\partial N}\right)_{U,V,\dots}$ with {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}

From these, one can obtain an {{< knowl id="equation-of-state" text="equation of state" >}} such as $P=P(T,V,N)$ by eliminating $U$ in favor of $(T,V,N)$ using the derivative relation for $T$.

**Key properties.**
- **Extensivity as homogeneity.** For additive systems away from long-range interaction effects, the entropy is extensive and (ideally) {{< knowl id="homogeneous-function-degree-one" text="homogeneous of degree one" >}} in $(U,V,N,\dots)$, which underlies the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} and {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}.
- **Concavity and stability.** Stability in the entropy representation corresponds to concavity of $S$ in its extensive arguments, linking to {{< knowl id="entropy-concavity-stability" text="entropy concavity (stability)" >}} and constraining {{< knowl id="response-function-thermo" text="response functions" >}} (e.g., positive heat capacities in typical regimes).
- **Second-law compatibility.** The entropy fundamental relation is consistent with the {{< knowl id="second-law-thermodynamics" text="second law" >}} and the {{< knowl id="clausius-inequality" text="Clausius inequality" >}} for irreversible processes.
