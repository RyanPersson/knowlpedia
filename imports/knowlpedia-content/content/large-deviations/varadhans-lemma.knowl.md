+++
id = "large-deviations/varadhans-lemma"
title = "Varadhan's lemma"
kind = "knowl"
summary = "Asymptotic evaluation of exponential integrals under a large deviation principle."
aliases = ["varadhans-lemma", "Varadhan's lemma"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/varadhans-lemma.md"
+++

**Varadhan's lemma:** Let $X$ be a Polish space and let $(\mu_n)$ be [[probability/probability-measure|probability measures]] on $X$ that satisfy a [[large-deviations/large-deviation-principle|large deviation principle]] with speed $a_n\to\infty$ and [[large-deviations/good-rate-function|good rate function]] $I\colon X\to[0,\infty]$. If $f\colon X\to\mathbb{R}$ is continuous and bounded above, then
\[
\lim_{n\to\infty}\frac{1}{a_n}\log \int_X \exp\bigl(a_n f(x)\bigr)\,\mu_n(dx)
= \sup_{x\in X}\bigl\{f(x)-I(x)\bigr\}.
\]

Taking $f=-\varphi$ yields the [[large-deviations/laplace-principle|Laplace principle]]. In many applications, the “goodness” of $I$ is obtained by combining an LDP with [[large-deviations/exponential-tightness|exponential tightness]].
