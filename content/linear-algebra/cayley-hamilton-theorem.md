---
title: "Cayley–Hamilton theorem"
description: "A square matrix satisfies its own characteristic polynomial."
---

**Cayley–Hamilton theorem:** Let $T:V\to V$ be a {{< knowl id="linear-operator" text="linear operator" >}} on a finite-dimensional vector space $V$. Let $p_T(t)$ be the {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}} of $T$. Then
\[
p_T(T)=0,
\]
meaning that substituting $T$ into its own characteristic polynomial yields the zero operator on $V$.

Equivalently, if $A$ is an $n\times n$ matrix and $p_A(t)=\det(tI-A)$ (defined using the {{< knowl id="determinant" text="determinant" >}}), then $p_A(A)=0$. One consequence is that the {{< knowl id="minimal-polynomial" text="minimal polynomial" >}} divides the characteristic polynomial, linking algebraic identities of $T$ to its {{< knowl id="eigenvalue" text="eigenvalues" >}}.
