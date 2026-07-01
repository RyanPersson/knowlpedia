+++
id = "thermodynamics/particle-number"
title = "Particle number"
kind = "knowl"
summary = "An extensive state variable counting the amount of matter, conjugate to chemical potential and central to chemical exchange."
aliases = ["particle-number", "Particle number"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/particle-number.md"
+++

## Definition and physical interpretation

The **particle number** $N$ is an [[thermodynamics/extensive-variable|extensive state variable]] that quantifies the amount of matter in a system by counting particles (or, more generally, counting moles up to a fixed conversion). In equilibrium thermodynamics, $N$ is treated as a macroscopic coordinate alongside [[thermodynamics/volume-thermo|volume]] and [[thermodynamics/thermodynamic-entropy|entropy]] for a single-component simple system.

Physically, changes in $N$ represent **matter exchange** with the [[thermodynamics/surroundings-environment|environment]] across the [[thermodynamics/system-boundary|boundary]]. Accordingly:
- In a [[thermodynamics/closed-system|closed system]], $N$ is fixed.
- In an [[thermodynamics/open-system|open system]], $N$ can change via particle flow.
- In an [[thermodynamics/isolated-system|isolated system]], $N$ is fixed and there is no exchange of matter or energy.

## Appearance in the fundamental differential

For a simple compressible single-component system, the energy representation $U=U(S,V,N)$ implies
$$
dU = T\,dS - p\,dV + \mu\,dN.
$$

The coefficient of $dN$ defines the [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$, showing that $N$ is the extensive variable conjugate to $\mu$.

In this sense, variations in $N$ contribute an energy change even when mechanical work ($p\,dV$) and heat flow ($T\,dS$) are absent; this is the thermodynamic “cost” of adding/removing matter.

## Additivity, mixtures, and conservation remarks

- **Additivity:** Under the [[thermodynamics/additivity-postulate|additivity postulate]], $N$ is additive across subsystems that interact weakly: combining two subsystems gives $N=N_1+N_2$.

- **Multiple species:** For mixtures, one uses a set $\{N_i\}$ and corresponding chemical potentials $\{\mu_i\}$; chemical exchange and [[thermodynamics/chemical-equilibrium|chemical equilibrium]] then require matching the appropriate $\mu_i$ across phases or subsystems.

- **Conservation:** In many settings $N$ is conserved by the allowed processes, but thermodynamics itself allows $N$ to vary whenever particle exchange is permitted. In statistical mechanics this distinction is reflected by choosing, for example, the [[thermodynamics/canonical-ensemble-convention|canonical ensemble]] (fixed $N$) versus the [[thermodynamics/grand-canonical-ensemble-convention|grand canonical ensemble]] (fluctuating $N$ at fixed $\mu$).

## Densities and the thermodynamic limit

In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], it is often natural to keep intensive densities finite, especially the [[thermodynamics/number-density|number density]] $n=N/V$. Many macroscopic constitutive relations are more naturally expressed in terms of $n$ rather than $N$ and $V$ separately.
