+++
id = "thermodynamics/chemical-work-convention"
title = "Chemical work convention"
kind = "knowl"
summary = "Fixes the sign of the chemical potential term in the energy balance for open systems."
aliases = ["chemical-work-convention", "Chemical work convention"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/chemical-work-convention.md"
+++

## Definition and physical meaning

For an [[thermodynamics/open-system|open thermodynamic system]], the [[thermodynamics/particle-number|particle number]] $N$ can change as matter crosses the [[thermodynamics/system-boundary|boundary]]. The energetic effect of this exchange is governed by the [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$.

In the differential form of the [[thermodynamics/fundamental-relation-energy|fundamental energy relation]] for a single-component simple system, the reversible change in internal energy includes the term $\mu\,dN$:
$$
dU = T\,dS - P\,dV + \mu\, dN.
$$

Physically, $\mu$ is the energy change associated with adding particles to the system at fixed entropy and volume (for the reversible/quasistatic setting).

## Convention used in this blog

We keep the [[thermodynamics/work-sign-convention|same work sign convention]] as for mechanical work: $\delta W>0$ means **work done by the system**. With that choice, it is often convenient to treat particle exchange as a kind of generalized work and define the **chemical work (by the system)** as
- **Single species:** $\delta W_{\mathrm{chem}} := -\mu\, dN$,
- **Multiple species:** $\delta W_{\mathrm{chem}} := -\sum_i \mu_i\, dN_i$.

This definition is chosen so that when particles enter the system ($dN>0$), the system receives energy and the work *done by the system* is negative: $\delta W_{\mathrm{chem}}<0$.

With pressure–volume work included via the [[thermodynamics/pressure-volume-work-sign-convention|$P\,dV$ convention]], the [[thermodynamics/first-law-thermodynamics|first law]] can be written in the “work by the system” form as
$$
dU = \delta Q - \bigl(\delta W_{PV} + \delta W_{\mathrm{chem}}\bigr)
     = \delta Q - P_{\mathrm{ext}}\, dV + \sum_i \mu_i\, dN_i.
$$

## Key relations and common consequences

- **Grand potential sign check:** with [[thermodynamics/grand-potential|grand potential]] $\Omega := U - TS - \sum_i \mu_i N_i$, this convention leads to
  $$
  d\Omega = -S\, dT - P\, dV - \sum_i N_i\, d\mu_i
  $$

  for reversible variations, matching the natural variables $(T,V,\mu_i)$ used in the [[thermodynamics/grand-canonical-ensemble-convention|grand-canonical setting]].

- **Translation to “work on the system” convention:** if instead one writes $dU=\delta Q+\delta W^{(\mathrm{on})}$, then the chemical contribution is typically taken as $\delta W^{(\mathrm{on})}_{\mathrm{chem}}=+\sum_i \mu_i\, dN_i$.

- **Interpretation as reservoir exchange:** the $\mu\,dN$ term corresponds to energy transferred with matter from a particle reservoir (sometimes informally called a “chemical reservoir”), just as $T\,dS$ corresponds to exchange with a [[thermodynamics/thermal-reservoir|thermal reservoir]].
