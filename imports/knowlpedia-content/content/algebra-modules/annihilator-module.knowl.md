+++
id = "algebra-modules/annihilator-module"
title = "Annihilator of a module"
kind = "knowl"
summary = "The ideal of scalars that kill the entire module."
aliases = ["annihilator-module", "Annihilator of a module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/annihilator-module.md"
+++

Let $M$ be a left $R$-[[algebra-modules/module|module]]. The **annihilator** of $M$ is
\[
\operatorname{ann}_R(M)=\{r\in R: rM=0\}.
\]
It equals the [[shared-foundations/intersection|intersection]] of the elementwise annihilators:
\[
\operatorname{ann}_R(M)=\bigcap_{m\in M}\operatorname{ann}_R(m),
\]
where $\operatorname{ann}_R(m)$ is the [[algebra-modules/annihilator-element|annihilator of an element]]. For a left module, $\operatorname{ann}_R(M)$ is a [[algebra-rings/two-sided-ideal|two-sided ideal]], since it is stable under multiplication on both sides by arbitrary ring elements.

The annihilator measures faithfulness: $M$ is faithful iff $\operatorname{ann}_R(M)=0$.

**Examples:**
- For a commutative ring $R$ and ideal $I$, the module $R/I$ satisfies $\operatorname{ann}_R(R/I)=I$.
- If $M=0$, then $\operatorname{ann}_R(M)=R$.
- If $M=R$ as a left module over itself, then $\operatorname{ann}_R(M)=0$.
