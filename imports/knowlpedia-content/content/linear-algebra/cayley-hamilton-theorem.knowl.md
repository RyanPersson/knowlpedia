+++
id = "linear-algebra/cayley-hamilton-theorem"
title = "Cayley–Hamilton theorem"
kind = "knowl"
summary = "A square matrix satisfies its own characteristic polynomial."
aliases = ["cayley-hamilton-theorem", "Cayley–Hamilton theorem"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/cayley-hamilton-theorem.md"
+++

**Cayley–Hamilton theorem:** Let $T:V\to V$ be a [[linear-algebra/linear-operator|linear operator]] on a finite-dimensional vector space $V$. Let $p_T(t)$ be the [[linear-algebra/characteristic-polynomial|characteristic polynomial]] of $T$. Then
\[
p_T(T)=0,
\]
meaning that substituting $T$ into its own characteristic polynomial yields the zero operator on $V$.

Equivalently, if $A$ is an $n\times n$ matrix and $p_A(t)=\det(tI-A)$ (defined using the [[linear-algebra/determinant|determinant]]), then $p_A(A)=0$. One consequence is that the [[linear-algebra/minimal-polynomial|minimal polynomial]] divides the characteristic polynomial, linking algebraic identities of $T$ to its [[linear-algebra/eigenvalue|eigenvalues]].
