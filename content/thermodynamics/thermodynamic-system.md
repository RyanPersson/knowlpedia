---
title: "Thermodynamic system"
description: "A chosen portion of the universe whose macroscopic behavior is described with thermodynamic variables and laws."
---

A **thermodynamic system** is the portion of the physical world selected for study, treated as a well-defined entity that can (in general) exchange energy and/or matter with its {{< knowl id="surroundings-environment" text="surroundings" >}} across a {{< knowl id="system-boundary" text="system boundary" >}}.

The “system” may be a material body (e.g., a gas in a cylinder), a region of space (e.g., a control volume in fluid flow), or a composite object (e.g., two phases plus an interface), provided the boundary and allowed exchanges are specified.

## Physical interpretation
Choosing the system is a modeling step: it decides what you call “inside” and “outside,” and therefore what counts as energy transfer *into* the system as {{< knowl id="heat-inexact-differential" text="heat" >}} or {{< knowl id="work-inexact-differential" text="work" >}}. Once the system is fixed, its macroscopic condition at equilibrium is summarized by a {{< knowl id="thermodynamic-state" text="thermodynamic state" >}} described by {{< knowl id="state-variable" text="state variables" >}} (e.g., $T$, $p$, $V$, $N$), and its changes are described as a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}}.

## Key classifications (set by exchanges across the boundary)
The system type is determined by what can cross the boundary:
- **No matter or energy exchange:** {{< knowl id="isolated-system" text="isolated system" >}}.
- **Energy exchange but no matter exchange:** {{< knowl id="closed-system" text="closed system" >}}.
- **Matter (and typically energy) exchange:** {{< knowl id="open-system" text="open system" >}}.

These distinctions are not intrinsic “properties of the material” but of the *system + boundary choice*.

## Core relation to energy bookkeeping
For any thermodynamic system, the energy accounting is organized around {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$ (a {{< knowl id="state-function" text="state function" >}}) and transfers across the boundary as heat and work (both {{< knowl id="path-function" text="path functions" >}}). This is the content formalized by the {{< knowl id="first-law-thermodynamics" text="first law of thermodynamics" >}}.
