+++
id = "thermodynamics/maxwell-relations-theorem"
title = "Maxwell relations theorem"
kind = "knowl"
summary = "Because thermodynamic potentials are state functions (exact differentials), their mixed second derivatives agree, yielding Maxwell relations among response functions."
aliases = ["maxwell-relations-theorem", "Maxwell relations theorem"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/maxwell-relations-theorem.md"
+++

## Statement

Let $\Phi=\Phi(x_1,\dots,x_n)$ be a thermodynamic potential expressed in its natural variables, and assume $\Phi$ is twice continuously differentiable. If its differential has the form
$$
d\Phi = \sum_{i=1}^n A_i\,dx_i,
$$

then exactness of $d\Phi$ implies symmetry of mixed partial derivatives:
$$
\frac{\partial A_i}{\partial x_j} = \frac{\partial A_j}{\partial x_i}
\qquad (i\neq j).
$$
These identities are called **Maxwell relations**.

For a simple one-component system (fixed particle number $N$) the standard thermodynamic potentials yield the familiar relations:

- From internal energy $U(S,V)$:
  $$
  dU = T\,dS - P\,dV,
  \qquad\Rightarrow\qquad
  \left(\frac{\partial T}{\partial V}\right)_{S} = -\left(\frac{\partial P}{\partial S}\right)_{V}.
  $$

- From Helmholtz free energy $F(T,V)$:
  $$
  dF = -S\,dT - P\,dV,
  \qquad\Rightarrow\qquad
  \left(\frac{\partial S}{\partial V}\right)_{T} = \left(\frac{\partial P}{\partial T}\right)_{V}.
  $$

- From Gibbs free energy $G(T,P)$:
  $$
  dG = -S\,dT + V\,dP,
  \qquad\Rightarrow\qquad
  \left(\frac{\partial S}{\partial P}\right)_{T} = -\left(\frac{\partial V}{\partial T}\right)_{P}.
  $$

(Analogous relations hold when including particle number and chemical potential among the variables.)

## Key hypotheses and conclusions

**Hypotheses**
- The system admits an equilibrium thermodynamic description (states in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]]).
- Thermodynamic potentials are well-defined [[thermodynamics/thermodynamic-state|state functions]] and are $C^2$ in their natural variables.
- The differential forms written for $dU,dF,dG,\ldots$ hold (typically derived from the first and second laws plus Legendre transforms).

**Conclusions**
- Mixed partial derivatives of potentials coincide, producing Maxwell relations.
- Maxwell relations provide experimentally useful identities that connect hard-to-measure derivatives (often involving entropy) to easier ones (often involving pressure/volume/temperature).

## Cross-links to definitions

Thermodynamic objects:
- [[thermodynamics/internal-energy-thermo|internal energy]], [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]], [[thermodynamics/gibbs-free-energy|Gibbs free energy]], [[thermodynamics/grand-potential|grand potential]].
- [[thermodynamics/thermodynamic-entropy|entropy]], [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/chemical-potential-thermo|chemical potential]].

Structural/mathematical links:
- [[thermodynamics/maxwell-relation|Maxwell relation (definition)]].
- [[convex-analysis/legendre-transform|Legendre transform]] (thermodynamic potentials as Legendre transforms of $U$).
- [[stat-mech/prop-maxwell-from-mixed-partials|Maxwell-from-mixed-partials proposition]] and [[stat-mech/corollary-maxwell-standard-identities|standard Maxwell identities corollary]].
**Idea.** A thermodynamic potential is a state function, so its differential is exact (see [[stat-mech/exact-differential-criterion|exact differential criterion]]). Exactness implies equality of mixed second derivatives (Clairaut/Schwarz theorem), which directly produces the Maxwell relations once the coefficients in $dU,dF,dG,\ldots$ are identified with $T,S,P,V,\mu,N$.

**Significance.** Maxwell relations are consistency conditions for equilibrium thermodynamics and a practical computational tool: they turn “entropy derivatives” into measurable response derivatives and are central in deriving identities for heat capacities, compressibilities, and susceptibilities.
