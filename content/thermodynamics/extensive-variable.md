---
title: "Extensive variable"
description: "A state variable that scales proportionally with system size and is (approximately) additive over weakly interacting subsystems."
---

An **extensive variable** is a {{< knowl id="state-variable" text="state variable" >}} $X$ of a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} that measures “how much” of the system is present: if you combine two weakly interacting subsystems, the total is (approximately) the sum, and if you scale the system up by a factor, $X$ scales by the same factor.

Let $X$ be a {{< knowl id="state-variable" text="state variable" >}} defined on the {{< knowl id="thermodynamic-state" text="thermodynamic state" >}}. We call $X$ **extensive** if it satisfies (to thermodynamic accuracy) the following two equivalent size-scaling properties:

1. **Additivity (composition):** for two macroscopic subsystems $A$ and $B$ that are non-overlapping and interact only weakly across the {{< knowl id="system-boundary" text="boundary" >}},  
   $$
   X(A \cup B) \approx X(A) + X(B).
   $$
   This formalizes the {{< knowl id="additivity-postulate" text="additivity postulate" >}}.

2. **Homogeneity of degree one (scaling):** if you replicate the system by a factor $\lambda>0$ while keeping intensive control parameters fixed, then  
   $$
   X(\lambda S,\lambda V,\lambda N,\dots) = \lambda\, X(S,V,N,\dots),
   $$

   i.e. $X$ is a {{< knowl id="homogeneous-function-degree-one" text="homogeneous function of degree one" >}} in the extensive arguments.

Typical extensive variables include {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="volume-thermo" text="volume" >}} $V$, {{< knowl id="thermodynamic-entropy" text="entropy" >}} $S$, and {{< knowl id="particle-number" text="particle number" >}} $N$.

## Physical interpretation
Extensive variables quantify the size or amount of “stuff” in the system: doubling the amount of substance (at the same macroscopic conditions) doubles $U$, $S$, $V$, and $N$ up to small boundary/interface corrections. This scaling viewpoint is most precise in the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}} assumed by the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}}.

## Key relations and consequences
- **Contrast with intensive variables:** Ratios of extensive variables often produce an {{< knowl id="intensive-variable" text="intensive variable" >}}; this idea is formalized by {{< knowl id="specific-quantity" text="specific quantities" >}} and by densities such as {{< knowl id="number-density" text="number density" >}}.

- **Euler relation (from extensivity):** For a simple one-component system, extensivity of $U(S,V,N)$ implies the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}}
  $$
  U = TS - pV + \mu N,
  $$

  where $T$, $p$, and $\mu$ are the conjugate {{< knowl id="intensive-variable" text="intensive variables" >}} ({{< knowl id="temperature-thermo" text="temperature" >}}, {{< knowl id="pressure-thermo" text="pressure" >}}, {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}).

- **Gibbs–Duhem constraint:** Because extensive thermodynamics has fewer independent intensive variables than extensive ones, the intensive conjugates are not independent; this is expressed by the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}.
