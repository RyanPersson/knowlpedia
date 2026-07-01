+++
id = "large-deviations/exponential-tightness"
title = "Exponential tightness"
kind = "knowl"
summary = "A compact-containment condition ensuring probabilities outside compacts decay exponentially fast."
aliases = ["exponential-tightness", "Exponential tightness"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/exponential-tightness.md"
+++

A sequence of probability measures $(\mu_n)_{n\ge1}$ on a topological space $E$ is **exponentially tight at speed** $(a_n)_{n\ge1}$ with $a_n\to\infty$ if for every $M>0$ there exists a compact set $K_M\subseteq E$ such that
$$
\limsup_{n\to\infty}\frac{1}{a_n}\log \mu_n(K_M^{\,c}) \le -M.
$$

Exponential tightness is a strengthened form of ordinary tightness for [[probability/probability-measure|probability measures]]: it not only forces most mass into compacts, but does so with exponentially small tails at the LDP speed. It is frequently paired with a [[large-deviations/rate-function|rate function]] to obtain or upgrade a [[large-deviations/large-deviation-principle|large deviation principle]], and it is a standard hypothesis in results like the [[large-deviations/gartner-ellis-theorem|Gärtner–Ellis theorem]].

**Examples:**
- If $X$ has a finite [[probability/moment-generating-function|moment generating function]] in a neighborhood of $0$, then the laws of $\bar X_n=\frac1n\sum_{i=1}^n X_i$ are typically exponentially tight at speed $n$ on $\mathbb R$ (exponential moment bounds imply exponentially small tails).
- If $E$ itself is compact, then any sequence $(\mu_n)$ is exponentially tight at any speed, since one can take $K_M=E$ for all $M$.
