---
title: "Lie Algebra"
description: "A vector space with a bilinear bracket operation that is antisymmetric and satisfies the Jacobi identity."
---

A **Lie algebra** is a {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} \(\mathfrak{g}\) (typically over \(\mathbb{R}\) or \(\mathbb{C}\)) equipped with a bilinear map
$$
[\ ,\ ]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g},
$$
called the {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}}, such that for all \(X,Y,Z\in\mathfrak{g}\):
1. **Alternating / antisymmetry:** \([X,X]=0\) (equivalently \([X,Y]=-[Y,X]\)).
2. **Jacobi identity:**
$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
$$

## Examples
- Any associative algebra becomes a Lie algebra with commutator \([A,B]=AB-BA\), e.g. matrix Lie algebras \(\mathfrak{gl}(n,\mathbb{R})\).
- The space of {{< knowl id="vector-field" section="fiber-bundles" text="vector fields" >}} on a manifold with the commutator bracket.
- An {{< knowl id="abelian-lie-algebra" text="abelian Lie algebra" >}} is one with \([X,Y]=0\) for all \(X,Y\).

## Maps and structure
A structure-preserving map is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}; bijective ones are {{< knowl id="lie-algebra-isomorphism" text="isomorphisms" >}}.

Important substructures include {{< knowl id="lie-subalgebra" text="Lie subalgebras" >}}, {{< knowl id="ideal-of-lie-algebra" text="ideals" >}}, and the {{< knowl id="center-of-a-lie-algebra" text="center" >}}.

Many classification notions are defined in terms of the bracket, such as
{{< knowl id="solvable-lie-algebra" text="solvable" >}},
{{< knowl id="nilpotent-lie-algebra" text="nilpotent" >}},
{{< knowl id="semisimple-lie-algebra" text="semisimple" >}},
{{< knowl id="simple-lie-algebra" text="simple" >}}, and
{{< knowl id="reductive-lie-algebra" text="reductive" >}} Lie algebras.
