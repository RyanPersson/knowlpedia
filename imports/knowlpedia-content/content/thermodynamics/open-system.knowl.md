+++
id = "thermodynamics/open-system"
title = "Open system"
kind = "knowl"
summary = "A thermodynamic system that can exchange both energy and matter with its environment."
aliases = ["open-system", "Open system"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/open-system.md"
+++

An **open system** is a [[thermodynamics/thermodynamic-system|thermodynamic system]] whose [[thermodynamics/system-boundary|boundary]] is permeable to matter, so that particles (or chemical species) may cross between the system and the [[thermodynamics/surroundings-environment|surroundings]]. Consequently, quantities like the [[thermodynamics/particle-number|particle number]] (and composition) are not fixed by definition.

This contrasts with a [[thermodynamics/closed-system|closed system]], which exchanges energy but not matter, and an [[thermodynamics/isolated-system|isolated system]], which exchanges neither. The open/closed/isolated classification is about **matter exchange**; independently, the boundary may be an [[thermodynamics/adiabatic-wall|adiabatic wall]] or a [[thermodynamics/diathermal-wall|diathermal wall]] with respect to heat flow.

**Physical interpretation.** Typical open systems include a control volume around a turbine with inlet/outlet flows, a container exchanging vapor with a large reservoir, or a membrane-permeable compartment exchanging solute. An open system may reach [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]] if the environment fixes appropriate intensive conditions (e.g. temperature and chemical potential); otherwise it may sustain fluxes and remain out of equilibrium.

**Equilibrium differential including matter exchange.** For a simple compressible system that can exchange entropy, volume, and species amounts, the fundamental differential can be written as
$$
dU = T\,dS - P\,dV + \sum_i \mu_i\, dN_i,
$$

where $U$ is [[thermodynamics/internal-energy-thermo|internal energy]], $S$ is [[thermodynamics/thermodynamic-entropy|entropy]], $T$ is [[thermodynamics/temperature-thermo|temperature]], $P$ is [[thermodynamics/pressure-thermo|pressure]], $V$ is [[thermodynamics/volume-thermo|volume]], and $\mu_i$ are [[thermodynamics/chemical-potential-thermo|chemical potentials]] for species amounts $N_i$. The term $\sum_i \mu_i\,dN_i$ is the energetic contribution carried by matter transfer (often grouped under “chemical work”; conventions are summarized under [[thermodynamics/chemical-work-convention|chemical-work convention]]).

When an open system is simultaneously in contact with a [[thermodynamics/thermal-reservoir|thermal reservoir]] and particle reservoir(s) fixing $(T,\mu_i)$, the natural equilibrium potential is the [[thermodynamics/grand-potential|grand potential]].
