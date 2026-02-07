---
title: "Gibbs free energy"
description: "A thermodynamic potential that governs equilibrium and spontaneity at fixed and ."
---

## Definition and physical meaning

For a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} with {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="pressure-thermo" text="pressure" >}} $p$, {{< knowl id="volume-thermo" text="volume" >}} $V$, {{< knowl id="temperature-thermo" text="temperature" >}} $T$, and {{< knowl id="thermodynamic-entropy" text="entropy" >}} $S$, the **Gibbs free energy** is the {{< knowl id="state-function" text="state function" >}}
$$
G \equiv U + pV - TS.
$$

Equivalently, it is $G = H - TS$ in terms of {{< knowl id="enthalpy" text="enthalpy" >}} $H$. It is the natural potential when a system can exchange heat and volume with its environment so that $T$ and $p$ are effectively controlled (common in laboratory and chemical settings).

## Differential form and natural variables

For a simple compressible single-component system,
$$
dG = -S\,dT + V\,dp + \mu\,dN,
$$

where $\mu$ is the {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} and $N$ the {{< knowl id="particle-number" text="particle number" >}}.

Thus $G$ is naturally a function of $(T,p,N)$, and it generates the key derivatives:
- $S = -\left(\partial G/\partial T\right)_{p,N}$,
- $V = \left(\partial G/\partial p\right)_{T,N}$,
- $\mu = \left(\partial G/\partial N\right)_{T,p}$.

For multicomponent systems, the last relation generalizes to $\mu_i = (\partial G/\partial N_i)_{T,p,N_{j\neq i}}$.

## Spontaneity and maximum non-expansion work

At fixed $(T,p,N)$, the {{< knowl id="second-law-thermodynamics" text="second law" >}} implies that a spontaneous change satisfies
$$
\Delta G \le 0,
$$
with equality at {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}.

With the {{< knowl id="work-sign-convention" text="standard sign convention for work" >}}, the maximum work obtainable from the system *other than* $p\,dV$ expansion work in a process at constant $T$ and $p$ is
$$
W_{\text{non-}pV,\max} = -\Delta G,
$$
again achieved in a {{< knowl id="reversible-process" text="reversible process" >}}.

## Extensivity link: $G$ and the chemical potential

If the system satisfies the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}} so that the fundamental relation is a {{< knowl id="homogeneous-function-degree-one" text="homogeneous function of degree one" >}}, the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} gives (single component)
$$
U = TS - pV + \mu N.
$$

Substituting into the definition of $G$ yields
$$
G = \mu N,
$$

highlighting that $G$ is the extensive quantity conjugate to the intensive $\mu$.

Consistency among intensive variables is then encoded by the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}, which constrains how $T$, $p$, and $\mu$ can vary for a single-component system.
