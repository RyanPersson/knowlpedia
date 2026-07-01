+++
id = "stat-mech/ldp-rate-function-magnetization"
title = "Rate function for magnetization"
kind = "knowl"
summary = "The large-deviation rate function governing probabilities of atypical magnetization values under a Gibbs measure; its minimizers describe typical phases and its shape encodes coexistence and metastability."
aliases = ["ldp-rate-function-magnetization", "Rate function for magnetization"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/ldp-rate-function-magnetization.md"
+++

Let $\sigma_i \in \{-1,+1\}$ be spins in a volume $\Lambda$ with $|\Lambda|=N$. The (intensive) magnetization is
$$
m_N \;=\; \frac{1}{N}\sum_{i\in\Lambda}\sigma_i.
$$

Under an equilibrium Gibbs measure (see [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]]), $m_N$ often satisfies a **large deviation principle** (LDP) at speed $N$:
$$
\mathbb{P}(m_N \approx m)\;\asymp\;\exp\big(-N\, I(m)\big),
$$

where $I$ is the **rate function**. See [[large-deviations/large-deviation-principle|large deviation principle]] and [[large-deviations/rate-function|rate function]].

## Connection to the pressure (log-partition density)

In the canonical ensemble with external field $h$ (see [[stat-mech/canonical-ensemble|canonical ensemble]] and [[stat-mech/partition-function-canonical|canonical partition function]]), exponential tilting of magnetization corresponds to shifting the field.

Indeed,
$$
\mathbb{E}_{\beta,h}\!\left[e^{t\,N m_N}\right]
={}
\frac{Z_N(\beta,\,h+t/\beta)}{Z_N(\beta,\,h)}.
$$
If the pressure
$$
p(\beta,h) \;=\; \lim_{N\to\infty}\frac{1}{N}\log Z_N(\beta,h)
$$
exists (see [[stat-mech/pressure-log-partition-density|pressure (log-partition density)]]), then the scaled cumulant generating function is
$$
\Lambda_{\beta,h}(t)=p(\beta,h+t/\beta)-p(\beta,h).
$$

When $\Lambda_{\beta,h}$ is differentiable, the Gartner–Ellis mechanism yields a convex rate function given by the Legendre–Fenchel transform
$$
I_{\beta,h}(m)=\sup_{t\in\mathbb{R}}\Big\{t m-\Lambda_{\beta,h}(t)\Big\}.
$$

Non-differentiability of $p(\beta,h)$ in $h$ is a signature of phase coexistence and can produce flat pieces in $I_{\beta,h}$.

## Interpreting the shape of $I(m)$

- **Single phase (no coexistence):** $I(m)$ has a unique minimizer at the typical magnetization.
- **Symmetry breaking / coexistence:** at $h=0$ below critical temperature in Ising-type systems, $I(m)$ may have multiple minimizers (or a flat interval of minimizers at speed $N$), reflecting competing phases; see [[stat-mech-lattice/phase-transition-gibbs|phase transitions]] and [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]].
- **Metastability:** local (non-global) minima of $I(m)$ correspond to metastable magnetizations in a static large-deviation sense; see [[stat-mech/metastable-state|metastable states]].

A key caution at coexistence: intermediate magnetizations may be realized by phase separation with probability costs scaling like surface area (not volume). In that case, the speed-$N$ rate function can develop a **plateau** (zero cost on an interval), while the sharper cost is governed by interfaces and surface tension; see [[stat-mech/surface-tension-interface|surface tension and interfaces]].

## Explicit example: Curie–Weiss (mean-field) magnetization rate function

For the Curie–Weiss model (see [[stat-mech/curie-weiss-model|Curie–Weiss model]]), the magnetization obeys an LDP with an explicit rate function.

Let
$$
I_0(m)=\frac{1+m}{2}\log\frac{1+m}{2}+\frac{1-m}{2}\log\frac{1-m}{2}+\log 2
\quad\text{for } m\in[-1,1],
$$

the Cramér rate function of i.i.d. $\pm1$ spins (see [[large-deviations/cramers-theorem|Cramér's theorem]]).
Then for coupling $J$ and field $h$, define the mean-field “free-energy-like” function
$$
\phi_{\beta,h}(m)= I_0(m) - \frac{\beta J}{2}m^2 - \beta h\, m.
$$
The magnetization rate function can be written as
$$
I_{\beta,h}(m)=\phi_{\beta,h}(m)-\inf_{m'\in[-1,1]}\phi_{\beta,h}(m').
$$
Its minimizers are exactly the stable equilibrium magnetizations, and its local minima encode mean-field metastability (compare [[stat-mech/mean-field-approximation|mean-field approximation]] and [[stat-mech/landau-free-energy-functional|Landau theory]]).
