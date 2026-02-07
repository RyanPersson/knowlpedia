---
title: "Peierls–Bogoliubov inequality"
description: "A variational upper bound on free energy: F(H) ≤ F(H0) + ⟨H−H0⟩_{H0}, equivalently a tangent-line bound for log Tr e^{A}."
---

## Definitions and notation

- {{< knowl id="gibbs-state-quantum" section="stat-mech-quantum" text="Quantum Gibbs state" >}} and {{< knowl id="quantum-partition-function" section="stat-mech-quantum" text="quantum partition function" >}}.
- {{< knowl id="free-energy-statistical" section="stat-mech" text="(Helmholtz) free energy in statistical mechanics" >}}.
- {{< knowl id="golden-thompson-lemma" text="Golden–Thompson lemma" >}} (often used to establish convexity properties).

## Statement

Let $A$ and $B$ be self-adjoint operators on a finite-dimensional Hilbert space (or more generally assume $e^{A}$ and $e^{A+B}$ are trace-class so the traces below are finite). Define
$$
Z(A) := \operatorname{Tr}(e^{A}),
\qquad
\langle B\rangle_{A} := \frac{\operatorname{Tr}(e^{A}B)}{\operatorname{Tr}(e^{A})}.
$$
Then the Peierls–Bogoliubov inequality states:
$$
\log Z(A+B) \;\ge\; \log Z(A) + \langle B\rangle_{A}.
$$

**Thermodynamic form.** Let $H$ and $H_0$ be (finite-volume) Hamiltonians and fix $\beta>0$. Set
$$
Z := \operatorname{Tr}(e^{-\beta H}), \qquad Z_0 := \operatorname{Tr}(e^{-\beta H_0}),
\qquad
F(H) := -\frac{1}{\beta}\log Z.
$$

Let $\langle\cdot\rangle_{0}$ denote expectation in the Gibbs state $\rho_0 = e^{-\beta H_0}/Z_0$. Then
$$
F(H) \le F(H_0) + \langle H - H_0\rangle_{0}.
$$

## Key hypotheses and conclusions

**Hypotheses**
- $A,B$ are self-adjoint and $Z(A),Z(A+B)$ are finite.
- In the Hamiltonian form: $Z$ and $Z_0$ are finite at the chosen inverse temperature $\beta$.

**Conclusions**
- $\log Z(\cdot)$ is bounded below by its tangent plane: $\log Z(A+B)\ge \log Z(A)+\langle B\rangle_A$.
- Free energy admits a variational upper bound in terms of any trial Hamiltonian $H_0$ and its Gibbs expectation.

