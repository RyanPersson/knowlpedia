---
title: "Zeroth law of thermodynamics"
description: "Thermal equilibrium is transitive, enabling temperature to be defined as a state variable."
---

The **zeroth law** formalizes the idea that “being in thermal equilibrium” is a consistent notion across many systems, and it provides the conceptual foundation for defining {{< knowl id="temperature-thermo" text="temperature" >}}.

**Definition (transitivity of thermal equilibrium).** If system $A$ is in {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} with system $B$, and $B$ is in thermal equilibrium with system $C$, then $A$ is in thermal equilibrium with $C$.

This is often summarized as: thermal equilibrium is **transitive**.

**Physical interpretation.** The zeroth law justifies thermometry: if a thermometer (system $B$) reaches thermal equilibrium with a system of interest ($A$), and the same thermometer reading is obtained when it equilibrates with another system ($C$), then $A$ and $C$ are mutually in thermal equilibrium. Operationally, this means a single scalar label—temperature—can characterize the “thermal state” shared by systems in mutual thermal equilibrium.

**Equivalence-class viewpoint.** Define a relation “$\sim$” on equilibrium states by declaring $A\sim B$ if they are in thermal equilibrium. The zeroth law asserts that, on equilibrium states, this relation behaves like an {{< knowl id="equivalence-relation" section="shared-foundations" text="equivalence relation" >}} (in particular, it is transitive). The corresponding classes are sometimes emphasized explicitly as {{< knowl id="zeroth-law-equivalence" text="zeroth-law equivalence classes" >}}.

**Consequences in thermodynamics.**
- **Temperature as a state variable.** The zeroth law supports the existence of a state variable $T$ that is equal for systems in mutual thermal equilibrium, fitting into the general framework of {{< knowl id="thermodynamic-state" text="thermodynamic state" >}} descriptions.
- **Thermal contact and walls.** Whether two systems can approach thermal equilibrium depends on the {{< knowl id="system-boundary" text="boundary" >}}: a {{< knowl id="diathermal-wall" text="diathermal wall" >}} permits energy exchange as heat, while an {{< knowl id="adiabatic-wall" text="adiabatic wall" >}} blocks it.
- **Reservoir idealization.** A {{< knowl id="thermal-reservoir" text="thermal reservoir" >}} is an ideal system whose temperature is effectively unchanged by exchanges, making the zeroth-law notion of “same $T$” especially operational.

To turn “equal temperature” into a specific numerical scale requires additional structure; see {{< knowl id="absolute-temperature-scale" text="absolute temperature scale" >}}.
