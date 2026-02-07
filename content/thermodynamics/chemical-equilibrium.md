---
title: "Chemical equilibrium"
description: "Equilibrium with respect to matter exchange and reactions: no net particle flow and chemical potentials satisfy the appropriate equalities."
---

A {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} is in **chemical equilibrium** when there is no spontaneous tendency for its composition to change through matter transfer or chemical reaction, given the allowed exchanges with its {{< knowl id="surroundings-environment" text="environment" >}} and its constraints.

Two common cases are:

1. **Particle exchange (diffusive equilibrium).** If two systems can exchange {{< knowl id="particle-number" text="particles" >}} through a permeable boundary, chemical equilibrium requires equality of the {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} for each exchanged species:
   $$
   \mu_i^{(1)} = \mu_i^{(2)} \quad \text{for each species } i.
   $$

2. **Chemical reactions.** For a reaction with stoichiometric coefficients $\nu_i$, chemical equilibrium requires that the reaction has no net driving force. In terms of chemical potentials this can be written as
   $$
   \sum_i \nu_i \mu_i = 0,
   $$
   with the sum over all species participating in the reaction.

Chemical equilibrium is a necessary component of {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}, alongside {{< knowl id="mechanical-equilibrium" text="mechanical" >}} and {{< knowl id="thermal-equilibrium" text="thermal" >}} equilibrium.

## Physical interpretation
Chemical potential measures the “escaping tendency” of particles (or, more generally, how the system’s free energy changes with composition). If two regions have different chemical potentials for a species, matter transfer or reaction progress can increase total entropy (or decrease the appropriate free-energy potential), so a net change occurs until the chemical potentials satisfy the equilibrium condition.

In practice, chemical equilibrium is what makes composition stable: once reached, the system may still exchange energy as {{< knowl id="heat-inexact-differential" text="heat" >}} or perform {{< knowl id="work-inexact-differential" text="work" >}} (depending on constraints), but it has no net tendency to change its particle content or reaction extent.

## Key relations and thermodynamic potentials
**Entropy maximization with particle exchange.** For two subsystems that can exchange particles (but not volume) with fixed totals, maximizing total entropy implies
$$
\left(\frac{\partial S_1}{\partial N_1}\right)_{U_1,V_1}
={}
\left(\frac{\partial S_2}{\partial N_2}\right)_{U_2,V_2}.
$$

Using the identity from equilibrium thermodynamics
$$
\left(\frac{\partial S}{\partial N}\right)_{U,V} = -\frac{\mu}{T},
$$

this yields $\mu_1/T_1 = \mu_2/T_2$. When the subsystems are also in {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} so that $T_1=T_2$, it reduces to $\mu_1=\mu_2$.

**Equivalent definitions of chemical potential.** For a single-component system,
$$
\mu = \left(\frac{\partial U}{\partial N}\right)_{S,V}
= \left(\frac{\partial F}{\partial N}\right)_{T,V}
= \left(\frac{\partial G}{\partial N}\right)_{T,P},
$$

linking $\mu$ to derivatives of {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} $F$, and {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} $G$ in the natural variables of each potential.

**Open systems and reservoirs.** A system that can exchange particles with a reservoir is an {{< knowl id="open-system" text="open system" >}}; at fixed $(T,V,\mu)$ the equilibrium state minimizes the {{< knowl id="grand-potential" text="grand potential" >}}.
