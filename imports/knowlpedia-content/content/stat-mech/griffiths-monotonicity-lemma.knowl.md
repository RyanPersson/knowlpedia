+++
id = "stat-mech/griffiths-monotonicity-lemma"
title = "Griffiths monotonicity lemma"
kind = "knowl"
summary = "For ferromagnetic Ising-type models, spin correlations are monotone nondecreasing in the couplings and external fields; used to construct infinite-volume limits and compare boundary conditions."
aliases = ["griffiths-monotonicity-lemma", "Griffiths monotonicity lemma"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/griffiths-monotonicity-lemma.md"
+++

## Statement (monotonicity in parameters)

Consider the ferromagnetic Ising model on a finite graph/finite region $\Lambda$ with spins $\sigma_x\in\{-1,+1\}$ and Hamiltonian
$$
H(\sigma)= -\sum_{\{x,y\}} J_{xy}\,\sigma_x\sigma_y \;-\; \sum_x h_x\,\sigma_x,
$$

with **ferromagnetic couplings** $J_{xy}\ge 0$ and **nonnegative external field** $h_x\ge 0$ (and any fixed boundary condition, typically plus).

Let $\langle \cdot \rangle_{J,h}$ denote expectation with respect to the associated [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]].

For any finite set $A\subset \Lambda$, define the spin product $\sigma_A := \prod_{x\in A}\sigma_x$. Then:

- For every edge $\{x,y\}$,
  $$
  \frac{\partial}{\partial J_{xy}} \langle \sigma_A \rangle_{J,h} \ge 0.
  $$

- For every site $x$,
  $$
  \frac{\partial}{\partial h_x} \langle \sigma_A \rangle_{J,h} \ge 0.
  $$

Equivalently, all correlation functions $\langle \sigma_A\rangle_{J,h}$ are **nondecreasing** functions of each coupling $J_{xy}$ and each field $h_x$ in the ferromagnetic, $h\ge 0$ regime.

## Key hypotheses

- The model is ferromagnetic: $J_{xy}\ge 0$ for all interacting pairs.
- External field is nonnegative: $h_x\ge 0$ (a common hypothesis ensuring the relevant correlation inequalities hold in the strongest form).
- Differentiability of finite-volume expectations in the parameters (automatic for finite systems).

## Key conclusions

- Monotonicity of magnetization $m_x=\langle \sigma_x\rangle$ and higher correlations with respect to strengthening couplings/fields.
- Useful monotone limits as volume grows (e.g., with plus boundary conditions), supporting construction of [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] by monotone convergence.
- Parameter comparison and bounds for observables such as [[stat-mech/correlation-function-two-point|two-point correlations]].

## Cross-links to relevant definitions and tools

- The model: [[stat-mech-lattice/ising-model|Ising model]].
- Expectation as an integral w.r.t. a probability measure: [[probability/expectation|expectation]].
- Positivity inequalities typically used in the proof:
  - [[stat-mech/griffiths-inequalities|Griffiths inequalities]]
  - [[stat-mech/gks-inequalities|GKS inequalities]]
  - [[stat-mech/fkg-inequality|FKG inequality]]
