---
title: "Open system"
description: "A thermodynamic system that can exchange both energy and matter with its environment."
---

An **open system** is a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} whose {{< knowl id="system-boundary" text="boundary" >}} is permeable to matter, so that particles (or chemical species) may cross between the system and the {{< knowl id="surroundings-environment" text="surroundings" >}}. Consequently, quantities like the {{< knowl id="particle-number" text="particle number" >}} (and composition) are not fixed by definition.

This contrasts with a {{< knowl id="closed-system" text="closed system" >}}, which exchanges energy but not matter, and an {{< knowl id="isolated-system" text="isolated system" >}}, which exchanges neither. The open/closed/isolated classification is about **matter exchange**; independently, the boundary may be an {{< knowl id="adiabatic-wall" text="adiabatic wall" >}} or a {{< knowl id="diathermal-wall" text="diathermal wall" >}} with respect to heat flow.

**Physical interpretation.** Typical open systems include a control volume around a turbine with inlet/outlet flows, a container exchanging vapor with a large reservoir, or a membrane-permeable compartment exchanging solute. An open system may reach {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}} if the environment fixes appropriate intensive conditions (e.g. temperature and chemical potential); otherwise it may sustain fluxes and remain out of equilibrium.

**Equilibrium differential including matter exchange.** For a simple compressible system that can exchange entropy, volume, and species amounts, the fundamental differential can be written as
$$
dU = T\,dS - P\,dV + \sum_i \mu_i\, dN_i,
$$

where $U$ is {{< knowl id="internal-energy-thermo" text="internal energy" >}}, $S$ is {{< knowl id="thermodynamic-entropy" text="entropy" >}}, $T$ is {{< knowl id="temperature-thermo" text="temperature" >}}, $P$ is {{< knowl id="pressure-thermo" text="pressure" >}}, $V$ is {{< knowl id="volume-thermo" text="volume" >}}, and $\mu_i$ are {{< knowl id="chemical-potential-thermo" text="chemical potentials" >}} for species amounts $N_i$. The term $\sum_i \mu_i\,dN_i$ is the energetic contribution carried by matter transfer (often grouped under “chemical work”; conventions are summarized under {{< knowl id="chemical-work-convention" text="chemical-work convention" >}}).

When an open system is simultaneously in contact with a {{< knowl id="thermal-reservoir" text="thermal reservoir" >}} and particle reservoir(s) fixing $(T,\mu_i)$, the natural equilibrium potential is the {{< knowl id="grand-potential" text="grand potential" >}}.
