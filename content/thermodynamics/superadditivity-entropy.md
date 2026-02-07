---
title: "Superadditivity of Entropy"
description: "Entropy of a composite system is at least the sum of the entropies of its parts (with matching conserved quantities), expressing extensivity and leading to concavity."
---

This lemma is most naturally formulated for the {{< knowl id="boltzmann-entropy-microcanonical" section="stat-mech" text="microcanonical (Boltzmann) entropy" >}}, and it encodes the thermodynamic intuition behind {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} being extensive.

## Statement (microcanonical form)
Consider two subsystems with disjoint degrees of freedom (e.g. two disjoint regions $\Lambda_1,\Lambda_2$) whose Hamiltonian is additive when they are decoupled:
$$
H_{\Lambda_1\cup\Lambda_2} = H_{\Lambda_1}+H_{\Lambda_2}.
$$

Let $\Omega_\Lambda(E,\Delta)$ denote the number (or volume, in phase space) of microstates in an energy window $[E,E+\Delta]$, and define the windowed microcanonical entropy
$$
S_\Lambda(E,\Delta)=\log \Omega_\Lambda(E,\Delta).
$$

Then for any $E_1,E_2$ and any $\Delta>0$,
$$
\Omega_{\Lambda_1\cup\Lambda_2}(E_1+E_2,\Delta)
\;\ge\;
\Omega_{\Lambda_1}(E_1,\Delta)\,\Omega_{\Lambda_2}(E_2,\Delta),
$$
and therefore
$$
S_{\Lambda_1\cup\Lambda_2}(E_1+E_2,\Delta)
\;\ge\;
S_{\Lambda_1}(E_1,\Delta)+S_{\Lambda_2}(E_2,\Delta).
$$

## Key hypotheses and conclusions
**Hypotheses**
- The two subsystems are independent/decoupled so that the composite Hamiltonian is additive.
- Entropy is defined by logarithmic counting/volume of microstates (Boltzmann form).

**Conclusions**
- **Superadditivity:** the entropy of the union is at least the sum of entropies of parts at matching conserved totals.
- By optimizing over the split $E=E_1+E_2$, one obtains the familiar inequality
  $S_{\Lambda_1\cup\Lambda_2}(E,\Delta)\ge \sup_{E_1+E_2=E}\big(S_{\Lambda_1}(E_1,\Delta)+S_{\Lambda_2}(E_2,\Delta)\big)$,
  which is a precursor to concavity of the entropy density.

## significance
If $x_1$ is a microstate of subsystem 1 with energy in $[E_1,E_1+\Delta]$ and $x_2$ is a microstate of subsystem 2 with energy in $[E_2,E_2+\Delta]$, then the product state $(x_1,x_2)$ is a microstate of the composite system with energy in $[E_1+E_2,E_1+E_2+\Delta]$. This injective map from pairs of microstates to composite microstates gives the multiplicative lower bound on $\Omega$, and taking $\log$ yields superadditivity.

For weakly interacting short-range systems, a variant holds **up to boundary corrections** (analogous to {{< knowl id="subadditivity-partition-function" text="subadditivity for the partition function" >}}): interactions across an interface contribute only $O(|\partial|)$ to the energy accounting, which is negligible per unit volume in the thermodynamic limit.

Superadditivity (or approximate superadditivity) is a standard route to existence of an entropy density via the superadditive form of {{< knowl id="fekete-lemma" section="stat-mech" text="Fekete's lemma" >}}, and it underlies the concavity/stability properties expected of equilibrium entropy.

