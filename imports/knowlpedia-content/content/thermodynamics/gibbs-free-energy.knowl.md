+++
id = "thermodynamics/gibbs-free-energy"
title = "Gibbs free energy"
kind = "knowl"
summary = "A thermodynamic potential that governs equilibrium and spontaneity at fixed and ."
aliases = ["gibbs-free-energy", "Gibbs free energy"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/gibbs-free-energy.md"
+++

## Definition and physical meaning

For a [[thermodynamics/thermodynamic-system|thermodynamic system]] with [[thermodynamics/internal-energy-thermo|internal energy]] $U$, [[thermodynamics/pressure-thermo|pressure]] $p$, [[thermodynamics/volume-thermo|volume]] $V$, [[thermodynamics/temperature-thermo|temperature]] $T$, and [[thermodynamics/thermodynamic-entropy|entropy]] $S$, the **Gibbs free energy** is the [[thermodynamics/state-function|state function]]
$$
G \equiv U + pV - TS.
$$

Equivalently, it is $G = H - TS$ in terms of [[thermodynamics/enthalpy|enthalpy]] $H$. It is the natural potential when a system can exchange heat and volume with its environment so that $T$ and $p$ are effectively controlled (common in laboratory and chemical settings).

## Differential form and natural variables

For a simple compressible single-component system,
$$
dG = -S\,dT + V\,dp + \mu\,dN,
$$

where $\mu$ is the [[thermodynamics/chemical-potential-thermo|chemical potential]] and $N$ the [[thermodynamics/particle-number|particle number]].

Thus $G$ is naturally a function of $(T,p,N)$, and it generates the key derivatives:
- $S = -\left(\partial G/\partial T\right)_{p,N}$,
- $V = \left(\partial G/\partial p\right)_{T,N}$,
- $\mu = \left(\partial G/\partial N\right)_{T,p}$.

For multicomponent systems, the last relation generalizes to $\mu_i = (\partial G/\partial N_i)_{T,p,N_{j\neq i}}$.

## Spontaneity and maximum non-expansion work

At fixed $(T,p,N)$, the [[thermodynamics/second-law-thermodynamics|second law]] implies that a spontaneous change satisfies
$$
\Delta G \le 0,
$$
with equality at [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]].

With the [[thermodynamics/work-sign-convention|standard sign convention for work]], the maximum work obtainable from the system *other than* $p\,dV$ expansion work in a process at constant $T$ and $p$ is
$$
W_{\text{non-}pV,\max} = -\Delta G,
$$
again achieved in a [[thermodynamics/reversible-process|reversible process]].

## Extensivity link: $G$ and the chemical potential

If the system satisfies the [[thermodynamics/extensivity-postulate|extensivity postulate]] so that the fundamental relation is a [[thermodynamics/homogeneous-function-degree-one|homogeneous function of degree one]], the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] gives (single component)
$$
U = TS - pV + \mu N.
$$

Substituting into the definition of $G$ yields
$$
G = \mu N,
$$

highlighting that $G$ is the extensive quantity conjugate to the intensive $\mu$.

Consistency among intensive variables is then encoded by the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]], which constrains how $T$, $p$, and $\mu$ can vary for a single-component system.
