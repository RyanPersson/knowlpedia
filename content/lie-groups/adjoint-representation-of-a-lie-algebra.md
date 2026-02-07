---
title: "Adjoint Representation of a Lie Algebra"
description: "The representation sending an element to the linear map given by bracketing with it."
---

Let \(\mathfrak{g}\) be a {{< knowl id="lie-algebra" text="Lie algebra" >}} with {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}} \([\ ,\ ]\).
For \(X\in\mathfrak{g}\), define a linear map
$$
\operatorname{ad}_X:\mathfrak{g}\to \mathfrak{g},\qquad \operatorname{ad}_X(Y)=[X,Y].
$$
This gives a map
$$
\operatorname{ad}:\mathfrak{g}\to \mathfrak{gl}(\mathfrak{g}),\qquad X\mapsto \operatorname{ad}_X,
$$
called the **adjoint representation** of \(\mathfrak{g}\).

## Key property
The map \(\operatorname{ad}\) is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}:
$$
[\operatorname{ad}_X,\operatorname{ad}_Y]=\operatorname{ad}_{[X,Y]}
\quad\text{in}\quad \mathfrak{gl}(\mathfrak{g}).
$$
Thus \(\operatorname{ad}\) is a {{< knowl id="representation-of-a-lie-algebra" text="representation of a Lie algebra" >}} on the vector space \(\mathfrak{g}\).

## Kernel and center
\(\ker(\operatorname{ad})\) consists of elements commuting with everything, i.e. the {{< knowl id="center-of-a-lie-algebra" text="center" >}} \(Z(\mathfrak{g})\).

## Killing form
The {{< knowl id="killing-form" text="Killing form" >}} is defined by
$$
B(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y),
$$
using the {{< knowl id="trace" section="linear-algebra" text="trace" >}}. It is fundamental for {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebras" >}}.

For a Lie group version, see {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action of a Lie group" >}}.
