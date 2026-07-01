+++
id = "measure-theory/caratheodory-construction"
title = "Carathéodory construction"
kind = "knowl"
summary = "A method that turns an outer measure into a measure by selecting Carathéodory measurable sets."
aliases = ["caratheodory-construction", "Carathéodory construction"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/caratheodory-construction.md"
+++

**Carathéodory construction:** Let $\mu^*$ be an [[measure-theory/outer-measure|outer measure]] on a set $X$. Define
$$
\mathcal{M}
=\Bigl\{E\subseteq X : \mu^*(A)=\mu^*(A\cap E)+\mu^*(A\setminus E)\ \text{for every } A\subseteq X\Bigr\}.
$$

Then $\mathcal{M}$ is a [[measure-theory/sigma-algebra|sigma-algebra]] on $X$, and the restriction $\mu:=\mu^*|_{\mathcal{M}}$ is a [[measure-theory/measure|measure]] on $\mathcal{M}$. The sets in $\mathcal{M}$ are exactly the [[measure-theory/caratheodory-measurable-set|Carathéodory measurable sets]] associated to $\mu^*$.

This construction is a standard way to build a [[measure-theory/measurable-space|measurable space]] and a measure from an outer measure; in particular it underlies the definition of [[measure-theory/lebesgue-measure|Lebesgue measure]] on $\mathbb{R}^n$.
