+++
id = "linear-algebra/trace"
title = "Trace"
kind = "knowl"
summary = "Sum of diagonal entries of a square matrix, invariant under change of basis."
aliases = ["trace"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/trace.md"
+++

A **trace** is the scalar associated to an $n\times n$ matrix $A=(a_{ij})$ over a field $\mathbb{F}$ defined by
\[
\operatorname{tr}(A)=\sum_{i=1}^n a_{ii}.
\]
For a [[linear-algebra/linear-operator|linear operator]] $T:V\to V$ on a finite-dimensional [[linear-algebra/vector-space|vector space]], the trace $\operatorname{tr}(T)$ is defined as $\operatorname{tr}(A)$ for any matrix $A$ representing $T$ in a basis; this is independent of the basis.

Trace is often paired with the [[linear-algebra/determinant|determinant]] in matrix identities and appears in coefficients of the [[linear-algebra/characteristic-polynomial|characteristic polynomial]]. When the characteristic polynomial splits, the trace equals the sum of the [[linear-algebra/eigenvalue|eigenvalues]] counted with algebraic multiplicity.

**Examples:**
- If $A$ is diagonal with diagonal entries $d_1,\dots,d_n$, then $\operatorname{tr}(A)=d_1+\cdots+d_n$.
- The identity matrix $I_n$ satisfies $\operatorname{tr}(I_n)=n$.
- Any nilpotent matrix (some power equals $0$) has trace $0$.
