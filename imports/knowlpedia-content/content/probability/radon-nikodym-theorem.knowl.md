+++
id = "probability/radon-nikodym-theorem"
title = "Radon–Nikodym theorem"
kind = "knowl"
summary = "Existence and uniqueness of a density for one measure that is absolutely continuous with respect to another."
aliases = ["radon-nikodym-theorem", "Radon–Nikodym theorem"]
domains = ["probability"]
legacy_source_path = "probability/radon-nikodym-theorem.md"
+++

**Radon–Nikodym theorem:** Let \((X,\mathcal{A},\mu)\) be a [[measure-theory/measure-space|measure space]] such that \(\mu\) is \(\sigma\)-finite, and let \(\nu\) be a \(\sigma\)-finite [[measure-theory/measure|measure]] on \((X,\mathcal{A})\) that is absolutely continuous with respect to \(\mu\) (written \(\nu \ll \mu\), meaning \(\mu(E)=0 \implies \nu(E)=0\) for all \(E\in\mathcal{A}\)). Then there exists a [[measure-theory/measurable-function|measurable function]] \(f:X\to[0,\infty]\) such that
\[
\nu(E)=\int_E f\,d\mu \qquad \text{for all } E\in\mathcal{A}.
\]
Moreover, \(f\) is unique up to \(\mu\)-almost everywhere equality, and it is denoted by \(\frac{d\nu}{d\mu}\) (the Radon–Nikodym derivative of \(\nu\) with respect to \(\mu\)).

In probability, applying this to [[probability/probability-measure|probability measure]]s yields the notion of a “density” or likelihood ratio: if \(Q \ll P\) on a [[probability/probability-space|probability space]], then \(L=\frac{dQ}{dP}\) satisfies \(Q(E)=\int_E L\,dP\), and for suitable \(g\) one has \(\mathbb{E}_Q[g]=\mathbb{E}_P[gL]\), linking the theorem to [[probability/expectation|expectation]]. A common structural use is that [[probability/conditional-expectation|conditional expectation]] can be characterized as a Radon–Nikodym derivative with respect to the restriction of a probability measure to a smaller [[measure-theory/sigma-algebra|sigma-algebra]].
