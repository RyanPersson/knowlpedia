---
title: "Zeroth-law equivalence"
description: "The equivalence relation on equilibrium states induced by mutual thermal equilibrium, enabling a consistent definition of temperature."
---

Define a relation $\sim$ on equilibrium states as follows: for two systems (or two equilibrium states) $A$ and $B$, write $A \sim B$ if placing them in contact through a {{< knowl id="diathermal-wall" text="diathermal contact" >}} produces no net heat flow and no macroscopic change—i.e., they are in {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}}.

The {{< knowl id="zeroth-law-thermodynamics" text="zeroth law of thermodynamics" >}} asserts the transitivity of this relation: if $A \sim B$ and $B \sim C$, then $A \sim C$. Together with the physically evident symmetry and reflexivity, this makes “being in thermal equilibrium with” an {{< knowl id="equivalence-relation" section="shared-foundations" text="equivalence relation" >}} on the set of equilibrium states.

## Physical interpretation
Zeroth-law equivalence partitions equilibrium states into equivalence classes: all states in the same class are mutually in thermal equilibrium. The {{< knowl id="temperature-thermo" text="temperature" >}} is then understood as a scalar label for these classes: states have the same temperature exactly when they are equivalent under $\sim$.

This is the conceptual basis of thermometry. A thermometer is a system whose equilibrium state changes monotonically across equivalence classes; the zeroth law guarantees that when the thermometer equilibrates with a system, its reading depends only on the system’s temperature class, not on what other systems were involved. With an agreed calibration, this yields a consistent temperature scale, and with additional conventions one can define an {{< knowl id="absolute-temperature-scale" text="absolute temperature scale" >}}.

## Key properties
Interpreting $\sim$ as “is in thermal equilibrium with,” the zeroth-law structure can be summarized as:

- **Reflexive:** $A \sim A$ (a system is in thermal equilibrium with itself).
- **Symmetric:** if $A \sim B$ then $B \sim A$ (no preferred direction once equilibrium holds).
- **Transitive:** if $A \sim B$ and $B \sim C$ then $A \sim C$ (the substantive content of the {{< knowl id="zeroth-law-thermodynamics" text="zeroth law" >}}).

A standard consequence is the existence of an empirical temperature function $T$ on equilibrium states such that $A \sim B$ if and only if $T(A)=T(B)$; different monotone reparameterizations of $T$ correspond to different but equivalent temperature scales.
