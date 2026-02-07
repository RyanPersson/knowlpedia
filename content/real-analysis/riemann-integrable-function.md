---
title: "Riemann integrable function"
description: "A bounded function whose upper and lower sums can be made arbitrarily close."
---

A **Riemann integrable function** on $[a,b]$ is a bounded function $f:[a,b]\to\mathbb R$ such that for every $\varepsilon>0$ there exists a {{< knowl id="partition-of-an-interval" text="partition" >}} $P$ with
\[
U(f,P)-L(f,P)<\varepsilon,
\]
where $U(f,P)$ is the {{< knowl id="upper-sum" text="upper sum" >}} and $L(f,P)$ is the {{< knowl id="lower-sum" text="lower sum" >}}. Equivalently,
\[
\sup_P L(f,P)=\inf_P U(f,P).
\]

When $f$ is Riemann integrable, the common value is the {{< knowl id="riemann-integral" text="Riemann integral" >}} of $f$. Integrability is closely tied to the {{< knowl id="set-of-discontinuities" text="set of discontinuities" >}} (see the {{< knowl id="lebesgue-criterion-for-riemann-integrability" section="measure-theory" text="Lebesgue criterion for Riemann integrability" >}}).

**Examples:**
- Any function that is continuous on $[a,b]$ is Riemann integrable.
- The indicator function of $\mathbb Q\cap[a,b]$ is not Riemann integrable on $[a,b]$.
