---
title: "Sanov's theorem"
description: "Large deviations for empirical measures of an independent identically distributed sample."
---

**Sanov's theorem:** Let $(X_i)_{i\ge 1}$ be an {{< knowl id="iid-sequence" section="probability" text="i.i.d. sequence" >}} taking values in a Polish space $E$, with common {{< knowl id="distribution-law" section="probability" text="law" >}} $\mu$. Define the empirical measure
\[
L_n=\frac{1}{n}\sum_{i=1}^n \delta_{X_i},
\]
viewed as a random element of $\mathcal{P}(E)$ (Borel probability measures on $E$) equipped with the topology of weak convergence. Then $(L_n)$ satisfies a {{< knowl id="large-deviation-principle" text="large deviation principle" >}} on $\mathcal{P}(E)$ with speed $n$ and {{< knowl id="good-rate-function" text="good rate function" >}}
\[
I(\nu)=H(\nu\|\mu)=
\begin{cases}
\displaystyle \int_E \log\!\left(\frac{d\nu}{d\mu}\right)\,d\nu, & \nu\ll \mu,\\[6pt]
+\infty, & \text{otherwise.}
\end{cases}
\]

Here $H(\nu\|\mu)$ is {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (Kullback–Leibler divergence)" >}}. Combined with the {{< knowl id="contraction-principle-ldp" text="contraction principle" >}}, Sanov's theorem yields many LDPs for functionals of empirical measures.
