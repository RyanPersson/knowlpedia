---
title: "Radon–Nikodym theorem"
description: "Existence and uniqueness of a density for one measure that is absolutely continuous with respect to another."
---

**Radon–Nikodym theorem:** Let \((X,\mathcal{A},\mu)\) be a {{< knowl id="measure-space" section="measure-theory" text="measure space" >}} such that \(\mu\) is \(\sigma\)-finite, and let \(\nu\) be a \(\sigma\)-finite {{< knowl id="measure" section="measure-theory" text="measure" >}} on \((X,\mathcal{A})\) that is absolutely continuous with respect to \(\mu\) (written \(\nu \ll \mu\), meaning \(\mu(E)=0 \implies \nu(E)=0\) for all \(E\in\mathcal{A}\)). Then there exists a {{< knowl id="measurable-function" section="measure-theory" text="measurable function" >}} \(f:X\to[0,\infty]\) such that
\[
\nu(E)=\int_E f\,d\mu \qquad \text{for all } E\in\mathcal{A}.
\]
Moreover, \(f\) is unique up to \(\mu\)-almost everywhere equality, and it is denoted by \(\frac{d\nu}{d\mu}\) (the Radon–Nikodym derivative of \(\nu\) with respect to \(\mu\)).

In probability, applying this to {{< knowl id="probability-measure" text="probability measure" >}}s yields the notion of a “density” or likelihood ratio: if \(Q \ll P\) on a {{< knowl id="probability-space" text="probability space" >}}, then \(L=\frac{dQ}{dP}\) satisfies \(Q(E)=\int_E L\,dP\), and for suitable \(g\) one has \(\mathbb{E}_Q[g]=\mathbb{E}_P[gL]\), linking the theorem to {{< knowl id="expectation" text="expectation" >}}. A common structural use is that {{< knowl id="conditional-expectation" text="conditional expectation" >}} can be characterized as a Radon–Nikodym derivative with respect to the restriction of a probability measure to a smaller {{< knowl id="sigma-algebra" section="measure-theory" text="sigma-algebra" >}}.
