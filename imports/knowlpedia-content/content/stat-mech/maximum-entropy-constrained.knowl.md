+++
id = "stat-mech/maximum-entropy-constrained"
title = "Maximum entropy with constraints (Gibbs/exponential family)"
kind = "knowl"
summary = "Maximizing Shannon entropy under expectation constraints yields a Gibbs (exponential-family) distribution, with Lagrange multipliers fixed by the constraints."
aliases = ["maximum-entropy-constrained", "Maximum entropy with constraints (Gibbs/exponential family)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/maximum-entropy-constrained.md"
+++

## Statement (maximum entropy principle)
Let $(X,\mathcal F,\mu)$ be a measurable space with a reference measure $\mu$, and let $f_1,\dots,f_k:X\to\mathbb R$ be measurable “constraint functions.” Fix target values $c_1,\dots,c_k\in\mathbb R$ and consider probability measures $P$ that are absolutely continuous w.r.t. $\mu$, with density $p=\frac{dP}{d\mu}$ satisfying
- normalization: $\int p\,d\mu = 1$,
- moment constraints: $\int f_i\,p\,d\mu = c_i$ for $i=1,\dots,k$.

Assume there exists at least one feasible $p$ with finite Shannon entropy
$S(p)=-\int p\log p\,d\mu$ (see [[probability/shannon-entropy|Shannon entropy]]).

If the entropy maximization problem has an interior maximizer (e.g. under standard regularity/feasibility conditions), then any maximizer has the Gibbs/exponential-family form
\[
p^*(x)=\exp\!\Big(-\alpha-\sum_{i=1}^k \lambda_i f_i(x)\Big),
\]
where $\alpha\in\mathbb R$ and multipliers $\lambda_1,\dots,\lambda_k\in\mathbb R$ are chosen so that the constraints hold. Equivalently,
\[
p^*(x)=\frac{\exp\!\big(-\sum_{i=1}^k \lambda_i f_i(x)\big)}{Z(\lambda)},\qquad
Z(\lambda)=\int \exp\!\Big(-\sum_{i=1}^k \lambda_i f_i(x)\Big)\,d\mu.
\]

## Key hypotheses
- A feasible set exists: there is at least one density $p\ge 0$ with $\int p\,d\mu=1$ and $\int f_i p\,d\mu=c_i$.
- Finite entropy is attainable: $S(p)>-\infty$ for some feasible $p$.
- Regularity ensuring the optimizer is not on the boundary (so Lagrange multiplier calculus applies) and that $Z(\lambda)$ is finite at the solution.

## Conclusions
- **Form of the maximizer:** the maximum-entropy density is an exponential tilt of the reference $\mu$.
- **Uniqueness (typical):** since $S(p)$ is strictly concave on densities, the maximizer is unique when the feasible set is convex and contains an interior point.
- **Thermodynamic interpretation:** with a single constraint $f_1=H$ (energy), the maximizer is the [[stat-mech/canonical-ensemble|canonical ensemble]] with partition function [[stat-mech/partition-function-canonical|canonical partition function]]; the multiplier is the inverse temperature (see [[thermodynamics/temperature-thermo|temperature]]).

## Cross-links to definitions
- Probability framework: [[probability/probability-measure|probability measure]], [[probability/expectation|expectation]].
- Entropy/divergence: [[probability/shannon-entropy|Shannon entropy]], [[probability/relative-entropy-kl-divergence|relative entropy (KL divergence)]].
- Statistical mechanics: [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/partition-function-canonical|partition function]].
Use Lagrange multipliers for the constrained optimization of the strictly concave functional $S(p)$ over an affine slice of densities. Stationarity of
\[
S(p) - \alpha\Big(\int p\,d\mu-1\Big)-\sum_i \lambda_i\Big(\int f_i p\,d\mu-c_i\Big)
\]
forces $\log p(x)$ to be an affine function of the constraints, giving the exponential form.

Equivalently, maximizing $S(p)$ subject to constraints is the same as minimizing KL divergence to the reference measure $\mu$ subject to the same constraints (a projection principle), linking equilibrium ensembles to variational principles.
