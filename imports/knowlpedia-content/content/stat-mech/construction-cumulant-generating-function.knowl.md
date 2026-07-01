+++
id = "stat-mech/construction-cumulant-generating-function"
title = "Cumulant generating function"
kind = "knowl"
summary = "The log moment-generating function; its derivatives at zero produce cumulants, and in statistical mechanics it is realized by log Z with sources."
aliases = ["construction-cumulant-generating-function", "Cumulant generating function"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-cumulant-generating-function.md"
+++

The cumulant generating function (CGF) is the standard tool for organizing fluctuations beyond the mean and variance. In statistical mechanics, the role of the CGF is played by the logarithm of a suitably “sourced” partition function, making cumulants accessible via derivatives of $\log Z$.

## Definition in probability

Let $X$ be a real-valued [[probability/random-variable|random variable]] on a [[probability/probability-space|probability space]]. Its [[probability/moment-generating-function|moment generating function]] (MGF), when finite near $t=0$, is
$$
M_X(t) \;=\; \mathbb{E}\!\left[e^{tX}\right].
$$
The cumulant generating function is
$$
K_X(t) \;=\; \log M_X(t) \;=\; \log \mathbb{E}\!\left[e^{tX}\right].
$$

The $n$th cumulant of $X$ is obtained by differentiating at the origin:
$$
\kappa_n(X) \;=\; \left.\frac{\mathrm{d}^n}{\mathrm{d}t^n}K_X(t)\right|_{t=0}.
$$
In particular,
$$
\kappa_1(X)=\mathbb{E}[X],\qquad
\kappa_2(X)=\mathrm{Var}(X),
$$

linking cumulants to [[probability/expectation|expectation]] and [[probability/variance|variance]]. For two random variables $X,Y$, mixed derivatives of $K_{(X,Y)}$ yield covariances (see [[probability/covariance|covariance]]).

## Multi-variable CGF and mixed cumulants

For a vector $X=(X_1,\dots,X_m)$, define
$$
K_X(t) \;=\; \log \mathbb{E}\!\left[\exp\!\left(\sum_{i=1}^m t_i X_i\right)\right],
$$

with $t=(t_1,\dots,t_m)$. Then mixed partial derivatives at $t=0$ give joint cumulants:
$$
\kappa(X_{i_1},\dots,X_{i_n})
\;=\;
\left.\frac{\partial^n K_X(t)}{\partial t_{i_1}\cdots \partial t_{i_n}}\right|_{t=0}.
$$
These cumulants vanish when the variables split into independent groups, capturing “genuine” correlation structure.

## Statistical mechanics realization: log Z as a CGF

In the [[stat-mech/canonical-ensemble|canonical ensemble]], introduce “sources” (fields) $\lambda_i$ conjugate to observables $A_i$ by considering
$$
Z(\beta,\lambda)
\;=\;
\int_{\Gamma}\exp\!\left(-\beta H_0(x) + \sum_{i=1}^m \lambda_i A_i(x)\right)\,\mathrm{d}\mu(x).
$$

Then $\log Z(\beta,\lambda)$ is exactly a CGF for the observables $(A_1,\dots,A_m)$ with respect to the canonical weight. Concretely, derivatives of $\log Z$ produce cumulants of the $A_i$ (up to powers of $\beta$ depending on conventions), which is the basis of
[[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from log Z]].

For example, in the common convention where the coupling is $-\beta(H_0-\sum_i h_i A_i)$, one finds
- $\partial_{h_i}\log Z = \beta\,\langle A_i\rangle$,
- $\partial_{h_i}\partial_{h_j}\log Z = \beta^2\,\mathrm{Cov}(A_i,A_j)$,
and higher derivatives give higher cumulants.

## Physical interpretation

- $\log Z$ packages equilibrium statistics: means, variances, and all higher connected moments are encoded in its derivatives.
- The convexity of $\log Z$ in the sources (when it exists) implies nonnegativity of variances and a hierarchy of stability inequalities.
- Connected correlation functions in many-body systems are precisely these cumulants in space-dependent sources; see
[[stat-mech/construction-connected-correlations-cumulants|connected correlations as cumulants]]
for the field-theoretic/many-body formulation.

This “CGF viewpoint” also interfaces naturally with large-deviation asymptotics through exponential tilting and Laplace-type limits (compare [[large-deviations/laplace-principle|the Laplace principle]]).
