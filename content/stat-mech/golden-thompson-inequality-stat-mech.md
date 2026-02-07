---
title: "Golden–Thompson inequality in statistical mechanics"
description: "Trace bound Tr(e^{A+B}) ≤ Tr(e^A e^B) and its standard application to quantum partition functions and free-energy bounds."
---

## Statement
Let $A$ and $B$ be self-adjoint operators on a finite-dimensional Hilbert space (equivalently, Hermitian matrices). Then
$$
\operatorname{Tr}\!\left(e^{A+B}\right)\le \operatorname{Tr}\!\left(e^{A}e^{B}\right).
$$
This is the {{< knowl id="golden-thompson-inequality" section="quantum-foundations" text="Golden–Thompson inequality" >}}, emphasized here in the form most commonly used in quantum statistical mechanics.

### Partition-function form
If $H_1$ and $H_2$ are Hamiltonians and $H=H_1+H_2$, then for $\beta>0$,
$$
Z(\beta)=\operatorname{Tr}\!\left(e^{-\beta(H_1+H_2)}\right)
\le
\operatorname{Tr}\!\left(e^{-\beta H_1}e^{-\beta H_2}\right),
$$

where $Z(\beta)$ is the {{< knowl id="quantum-partition-function" section="stat-mech-quantum" text="quantum partition function" >}}.

## Key hypotheses
- $A=A^\ast$ and $B=B^\ast$ (Hermitian).
- Finite-dimensional setting (or more generally: $A,B$ bounded with trace-class exponentials; the finite-dimensional case is the cleanest for stat-mech applications).

## Key conclusions
- The trace of the exponential of a sum is bounded by the trace of the product of exponentials:
  $$
  \operatorname{Tr}(e^{A+B}) \le \operatorname{Tr}(e^A e^B).
  $$

- For decomposed Hamiltonians $H=H_1+H_2$, this yields an upper bound on $Z(\beta)$ and hence a lower bound on the corresponding free energy (via $F=-(1/\beta)\log Z$ as in {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}).
## significance
A standard proof uses the Lie–Trotter product formula
$$
e^{A+B}=\lim_{n\to\infty}\left(e^{A/n}e^{B/n}\right)^n
$$

together with trace Hölder inequalities to compare $\operatorname{Tr}(e^{A+B})$ to $\operatorname{Tr}(e^{A}e^{B})$.

In statistical mechanics, the inequality is a core tool for:
- bounding interacting partition functions by splitting a Hamiltonian into “solvable + perturbation” pieces (useful alongside {{< knowl id="peierls-bogoliubov-inequality" text="Peierls–Bogoliubov" >}} bounds);
- establishing convexity/monotonicity properties of $\log Z$ and related thermodynamic potentials;
- controlling approximations where noncommuting terms obstruct naive factorization.
