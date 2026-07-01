+++
id = "thermodynamics/extensive-variable"
title = "Extensive variable"
kind = "knowl"
summary = "A state variable that scales proportionally with system size and is (approximately) additive over weakly interacting subsystems."
aliases = ["extensive-variable", "Extensive variable"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/extensive-variable.md"
+++

An **extensive variable** is a [[thermodynamics/state-variable|state variable]] $X$ of a [[thermodynamics/thermodynamic-system|thermodynamic system]] that measures “how much” of the system is present: if you combine two weakly interacting subsystems, the total is (approximately) the sum, and if you scale the system up by a factor, $X$ scales by the same factor.

Let $X$ be a [[thermodynamics/state-variable|state variable]] defined on the [[thermodynamics/thermodynamic-state|thermodynamic state]]. We call $X$ **extensive** if it satisfies (to thermodynamic accuracy) the following two equivalent size-scaling properties:

1. **Additivity (composition):** for two macroscopic subsystems $A$ and $B$ that are non-overlapping and interact only weakly across the [[thermodynamics/system-boundary|boundary]],
   $$
   X(A \cup B) \approx X(A) + X(B).
   $$
   This formalizes the [[thermodynamics/additivity-postulate|additivity postulate]].

2. **Homogeneity of degree one (scaling):** if you replicate the system by a factor $\lambda>0$ while keeping intensive control parameters fixed, then
   $$
   X(\lambda S,\lambda V,\lambda N,\dots) = \lambda\, X(S,V,N,\dots),
   $$

   i.e. $X$ is a [[thermodynamics/homogeneous-function-degree-one|homogeneous function of degree one]] in the extensive arguments.

Typical extensive variables include [[thermodynamics/internal-energy-thermo|internal energy]] $U$, [[thermodynamics/volume-thermo|volume]] $V$, [[thermodynamics/thermodynamic-entropy|entropy]] $S$, and [[thermodynamics/particle-number|particle number]] $N$.

## Physical interpretation
Extensive variables quantify the size or amount of “stuff” in the system: doubling the amount of substance (at the same macroscopic conditions) doubles $U$, $S$, $V$, and $N$ up to small boundary/interface corrections. This scaling viewpoint is most precise in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] assumed by the [[thermodynamics/extensivity-postulate|extensivity postulate]].

## Key relations and consequences
- **Contrast with intensive variables:** Ratios of extensive variables often produce an [[thermodynamics/intensive-variable|intensive variable]]; this idea is formalized by [[thermodynamics/specific-quantity|specific quantities]] and by densities such as [[thermodynamics/number-density|number density]].

- **Euler relation (from extensivity):** For a simple one-component system, extensivity of $U(S,V,N)$ implies the [[thermodynamics/euler-relation-thermodynamics|Euler relation]]
  $$
  U = TS - pV + \mu N,
  $$

  where $T$, $p$, and $\mu$ are the conjugate [[thermodynamics/intensive-variable|intensive variables]] ([[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/chemical-potential-thermo|chemical potential]]).

- **Gibbs–Duhem constraint:** Because extensive thermodynamics has fewer independent intensive variables than extensive ones, the intensive conjugates are not independent; this is expressed by the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]].
