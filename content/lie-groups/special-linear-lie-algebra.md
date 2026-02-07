---
title: "Special linear Lie algebra"
description: "The Lie algebra sl(n,F) of trace-zero matrices with bracket [X,Y]=XY−YX."
---

For $\mathbb F\in\{\mathbb R,\mathbb C\}$, the **special linear Lie algebra** is
\[
\mathfrak{sl}_n(\mathbb F)=\{X\in M_n(\mathbb F): \mathrm{tr}(X)=0\},
\]
equipped with the commutator bracket
\[
[X,Y]=XY-YX
\]
(see {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}} and compare {{< knowl id="general-linear-lie-algebra" text="general linear Lie algebra" >}}).

This Lie algebra is the Lie algebra of the {{< knowl id="special-linear-group" text="special linear group" >}} $SL(n,\mathbb F)$: under the identification $T_I SL(n,\mathbb F)\cong \mathfrak{sl}_n(\mathbb F)$, tangent vectors at the identity are exactly the trace-zero directions. Equivalently, $\mathfrak{sl}_n(\mathbb F)$ is the kernel of the differential of $\det:GL(n,\mathbb F)\to\mathbb F^\times$ at the identity.

Over $\mathbb C$, $\mathfrak{sl}_n(\mathbb C)$ is a fundamental example of a complex simple Lie algebra for $n\ge 2$ (see {{< knowl id="simple-lie-algebra" text="simple Lie algebra" >}} and {{< knowl id="classification-simple-lie-algebras" text="classification of simple Lie algebras" >}}). The case $n=2$ is the standard testbed for root computations (see {{< knowl id="example-sl2c" text="standard sl2 example" >}}).
