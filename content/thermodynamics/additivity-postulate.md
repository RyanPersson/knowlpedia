---
title: "Additivity postulate"
description: "Postulate that for weakly interacting macroscopic subsystems, extensive quantities (including entropy) add when the subsystems are combined."
---

## Definition (and physical meaning)

The **additivity postulate** states that if a macroscopic {{< knowl id="thermodynamic-system" text="system" >}} can be decomposed into subsystems $A$ and $B$ separated by an effective {{< knowl id="system-boundary" text="boundary" >}} so that interaction energies and correlations across the boundary are negligible at the macroscopic level, then extensive state variables add:
- $E=E_A+E_B$ for {{< knowl id="internal-energy-thermo" text="internal energy" >}},
- $V=V_A+V_B$ for {{< knowl id="volume-thermo" text="volume" >}},
- $N=N_A+N_B$ for {{< knowl id="particle-number" text="particle number" >}},
and, crucially for equilibrium reasoning,
$$
S(E,V,N)=S_A(E_A,V_A,N_A)+S_B(E_B,V_B,N_B)
$$
(up to subextensive corrections due to the interface).

**Physical interpretation:** additivity is the macroscopic expression of “weak coupling at a distance.” Distant parts of a large system can be treated as contributing independently to bulk thermodynamic bookkeeping.

Additivity is closely tied to the existence of the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}} and underlies the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}} for short-range interacting matter.

## Equilibrium implications

Consider an {{< knowl id="isolated-system" text="isolated system" >}} composed of two additively coupled subsystems that can exchange energy. With $E=E_A+E_B$ fixed, additivity gives $S=S_A(E_A)+S_B(E_B)$, so maximizing total {{< knowl id="thermodynamic-entropy" text="entropy" >}} yields
$$
\frac{\partial S_A}{\partial E_A}=\frac{\partial S_B}{\partial E_B},
$$

which is exactly the condition for {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} (since $\partial S/\partial E = 1/T$ defines {{< knowl id="temperature-thermo" text="temperature" >}}). Analogous entropy-maximization arguments produce the conditions for {{< knowl id="mechanical-equilibrium" text="mechanical equilibrium" >}} and {{< knowl id="chemical-equilibrium" text="chemical equilibrium" >}}.

## Connection to information-theoretic additivity

In statistical mechanics, it is often useful to compare thermodynamic entropy to dimensionless entropies such as {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}}: both become additive when the underlying subsystems/variables are independent. The thermodynamic statement is physically grounded in negligible interfacial interactions and correlations, not merely a formal property of a formula.

## Where additivity can break down

Additivity can fail when interactions across the boundary contribute at the same order as bulk terms (long-range forces, strong interfacial coupling, or persistent correlations). In such cases, treating the total entropy as a sum can miss macroscopic “interaction entropy” terms, and standard equilibrium derivations must be revisited.
