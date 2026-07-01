+++
id = "thermodynamics/fundamental-relation-entropy"
title = "Fundamental relation (entropy representation)"
kind = "knowl"
summary = "The entropy function S(U,V,N,...) that encodes all equilibrium thermodynamics via its derivatives and concavity."
aliases = ["fundamental-relation-entropy", "Fundamental relation (entropy representation)"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/fundamental-relation-entropy.md"
+++

In the **entropy representation**, the **fundamental relation** is the equilibrium entropy expressed as a function of the extensive variables:
$S = S(U,V,N,\dots)$,
where $U$ is [[thermodynamics/internal-energy-thermo|internal energy]], $V$ is [[thermodynamics/volume-thermo|volume]], and $N$ is [[thermodynamics/particle-number|particle number]] (and possibly other conserved extensive quantities). This single state function determines the equations of state and all response functions for systems in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]].

**Physical interpretation.** The function $S(U,V,N,\dots)$ counts (macroscopically) how many microscopic configurations are compatible with macroscopic constraints; its derivatives define the intensive “forces” that drive exchange with the [[thermodynamics/surroundings-environment|surroundings]].

**Generating derivatives.** The differential form of the fundamental relation is
$$
dS = \frac{1}{T}\,dU + \frac{P}{T}\,dV - \frac{\mu}{T}\,dN + \cdots ,
$$
which *defines* the intensive variables as partial derivatives:
- $\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N,\dots}$ with [[thermodynamics/temperature-thermo|temperature]]
- $\frac{P}{T} = \left(\frac{\partial S}{\partial V}\right)_{U,N,\dots}$ with [[thermodynamics/pressure-thermo|pressure]]
- $-\frac{\mu}{T} = \left(\frac{\partial S}{\partial N}\right)_{U,V,\dots}$ with [[thermodynamics/chemical-potential-thermo|chemical potential]]

From these, one can obtain an [[thermodynamics/equation-of-state|equation of state]] such as $P=P(T,V,N)$ by eliminating $U$ in favor of $(T,V,N)$ using the derivative relation for $T$.

**Key properties.**
- **Extensivity as homogeneity.** For additive systems away from long-range interaction effects, the entropy is extensive and (ideally) [[thermodynamics/homogeneous-function-degree-one|homogeneous of degree one]] in $(U,V,N,\dots)$, which underlies the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] and [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]].
- **Concavity and stability.** Stability in the entropy representation corresponds to concavity of $S$ in its extensive arguments, linking to [[thermodynamics/entropy-concavity-stability|entropy concavity (stability)]] and constraining [[thermodynamics/response-function-thermo|response functions]] (e.g., positive heat capacities in typical regimes).
- **Second-law compatibility.** The entropy fundamental relation is consistent with the [[thermodynamics/second-law-thermodynamics|second law]] and the [[thermodynamics/clausius-inequality|Clausius inequality]] for irreversible processes.
