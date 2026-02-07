---
title: "Outer derivation"
description: "A derivation not arising as an inner derivation; measured by Der(g)/ad(g)."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

## Definitions
A **derivation** of $\mathfrak g$ is a linear map $D:\mathfrak g\to\mathfrak g$ satisfying the Leibniz rule
$$
D([X,Y])=[D(X),Y]+[X,D(Y)] \quad \text{for all }X,Y\in\mathfrak g,
$$

as in {{< knowl id="derivation-lie-algebra" text="derivations of a Lie algebra" >}}. The space of all derivations is a Lie algebra $\mathrm{Der}(\mathfrak g)$ under the commutator bracket.

An **inner derivation** is one of the form $\mathrm{ad}_X$ for some $X\in\mathfrak g$, where $\mathrm{ad}_X(Y)=[X,Y]$ (see {{< knowl id="inner-derivation" text="inner derivations" >}} and the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}}). The set of inner derivations is an ideal $\mathrm{Inn}(\mathfrak g)=\mathrm{ad}(\mathfrak g)\subseteq \mathrm{Der}(\mathfrak g)$.

A derivation is called an **outer derivation** if it is not inner. The quotient Lie algebra
$$
\mathrm{Der}(\mathfrak g)/\mathrm{Inn}(\mathfrak g)
$$
measures outer derivations “modulo inner ones.”

## Basic remarks
- If $X$ lies in the {{< knowl id="center-of-a-lie-algebra" text="center" >}} of $\mathfrak g$, then $\mathrm{ad}_X=0$, so the map $\mathrm{ad}:\mathfrak g\to \mathrm{Der}(\mathfrak g)$ factors through $\mathfrak g/Z(\mathfrak g)$.
- For many rigid Lie algebras (notably {{< knowl id="semisimple-lie-algebra" text="semisimple" >}} ones), every derivation is inner, so the outer derivation quotient vanishes. This is one conceptual reason semisimple Lie algebras have very small deformation theory.

## Context
Outer derivations appear naturally when studying extensions and deformations of Lie algebras; inner derivations encode changes coming from conjugation, while outer derivations capture genuinely new infinitesimal symmetries.
