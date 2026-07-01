+++
id = "real-analysis/riemann-integrable-function"
title = "Riemann integrable function"
kind = "knowl"
summary = "A bounded function whose upper and lower sums can be made arbitrarily close."
aliases = ["riemann-integrable-function", "Riemann integrable function"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/riemann-integrable-function.md"
+++

A **Riemann integrable function** on $[a,b]$ is a bounded function $f:[a,b]\to\mathbb R$ such that for every $\varepsilon>0$ there exists a [[real-analysis/partition-of-an-interval|partition]] $P$ with
\[
U(f,P)-L(f,P)<\varepsilon,
\]
where $U(f,P)$ is the [[real-analysis/upper-sum|upper sum]] and $L(f,P)$ is the [[real-analysis/lower-sum|lower sum]]. Equivalently,
\[
\sup_P L(f,P)=\inf_P U(f,P).
\]

When $f$ is Riemann integrable, the common value is the [[real-analysis/riemann-integral|Riemann integral]] of $f$. Integrability is closely tied to the [[real-analysis/set-of-discontinuities|set of discontinuities]] (see the [[measure-theory/lebesgue-criterion-for-riemann-integrability|Lebesgue criterion for Riemann integrability]]).

**Examples:**
- Any function that is continuous on $[a,b]$ is Riemann integrable.
- The indicator function of $\mathbb Q\cap[a,b]$ is not Riemann integrable on $[a,b]$.
