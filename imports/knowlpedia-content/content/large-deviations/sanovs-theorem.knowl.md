+++
id = "large-deviations/sanovs-theorem"
title = "Sanov's theorem"
kind = "knowl"
summary = "Large deviations for empirical measures of an independent identically distributed sample."
aliases = ["sanovs-theorem", "Sanov's theorem"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/sanovs-theorem.md"
+++

**Sanov's theorem:** Let $(X_i)_{i\ge 1}$ be an [[probability/iid-sequence|i.i.d. sequence]] taking values in a Polish space $E$, with common [[probability/distribution-law|law]] $\mu$. Define the empirical measure
\[
L_n=\frac{1}{n}\sum_{i=1}^n \delta_{X_i},
\]
viewed as a random element of $\mathcal{P}(E)$ (Borel probability measures on $E$) equipped with the topology of weak convergence. Then $(L_n)$ satisfies a [[large-deviations/large-deviation-principle|large deviation principle]] on $\mathcal{P}(E)$ with speed $n$ and [[large-deviations/good-rate-function|good rate function]]
\[
I(\nu)=H(\nu\|\mu)=
\begin{cases}
\displaystyle \int_E \log\!\left(\frac{d\nu}{d\mu}\right)\,d\nu, & \nu\ll \mu,\\[6pt]
+\infty, & \text{otherwise.}
\end{cases}
\]

Here $H(\nu\|\mu)$ is [[probability/relative-entropy-kl-divergence|relative entropy (Kullback–Leibler divergence)]]. Combined with the [[large-deviations/contraction-principle-ldp|contraction principle]], Sanov's theorem yields many LDPs for functionals of empirical measures.
