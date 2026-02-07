---
title: "TFAE: Formulations of the Second Law"
description: "Equivalent statements of the second law: Kelvin–Planck, Clausius, entropy, Clausius inequality, and Carathéodory."
---

Fix a {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}} that can exchange heat and work with ideal reservoirs, and interpret “cyclic process” as one returning the system to its initial state. The following statements are equivalent (under the standard axioms of classical thermodynamics).

1. **Kelvin–Planck statement (no 100% conversion from one bath).**  
   No cyclic engine can extract heat $Q>0$ from a *single* heat bath at temperature $T$ and convert it completely into net work $W>0$ with no other changes in the environment.  
   (Equivalently: no “perpetual motion machine of the second kind.”)

2. **Clausius statement (no spontaneous heat flow uphill).**  
   No cyclic device can have the *sole* effect of transferring heat from a colder bath to a hotter bath.  
   In particular, heat does not flow spontaneously from cold to hot without compensation.

3. **Clausius inequality for cycles.**  
   For every cyclic process,
   $$
   \oint \frac{\delta Q}{T} \le 0,
   $$
   with equality if and only if the cycle is reversible.  
   (See {{< knowl id="clausius-inequality" section="thermodynamics" text="Clausius inequality" >}}.)

4. **Existence of entropy as a state function.**  
   There exists a state function $S$ ({{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}) such that for any reversible process
   $$
   dS = \frac{\delta Q_{\mathrm{rev}}}{T},
   $$

   and for any process between equilibrium states $1 \to 2$,
   $$
   \Delta S \ge \int_{1}^{2} \frac{\delta Q}{T},
   $$
   with equality if and only if the process is reversible.

5. **Entropy increase for isolated systems.**  
   If the system is isolated (no heat or work exchange), then in any spontaneous evolution between equilibrium states,
   $$
   \Delta S \ge 0,
   $$
   with equality if and only if the evolution is reversible.  
   In particular, {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="equilibrium" >}} corresponds to an entropy maximum at fixed conserved quantities.

6. **Carathéodory principle (adiabatic inaccessibility).**  
   In every neighborhood of any equilibrium state there exist states that cannot be reached from it by adiabatic processes.  
   This is equivalent to the existence of an integrating factor for $\delta Q$ and hence to the existence of $S$ and $T$ ({{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}) satisfying $dS=\delta Q_{\mathrm{rev}}/T$.

Prerequisites and context: {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law" >}}, {{< knowl id="clausius-inequality" section="thermodynamics" text="Clausius inequality" >}}, {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}}, {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
