---
title: "Nine lemma (3×3 lemma)"
description: "In a commutative 3×3 diagram in an abelian category with exact rows/columns, exactness of one row (or column) follows from the other eight exact sequences."
---

Let \(\mathcal A\) be an {{< knowl id="abelian-category" section="algebra-category-theory" text="abelian category" >}}. Consider a commutative \(3\times 3\) diagram
\[
\begin{array}{ccccccccc}
0 &\to& A' &\xrightarrow{}& A &\xrightarrow{}& A'' &\to& 0\\
&& \downarrow && \downarrow && \downarrow && \\
0 &\to& B' &\xrightarrow{}& B &\xrightarrow{}& B'' &\to& 0\\
&& \downarrow && \downarrow && \downarrow && \\
0 &\to& C' &\xrightarrow{}& C &\xrightarrow{}& C'' &\to& 0
\end{array}
\]
whose columns and first two rows are {{< knowl id="exact-sequence-categorical" section="algebra-category-theory" text="exact" >}} (equivalently, short exact in each line).

**Nine lemma (one common form).** If the three columns and the first two rows are exact, then the third row
\[
0\to C' \to C \to C'' \to 0
\]
is exact as well. Dually, if the three rows and the first two columns are exact, then the third column is exact.

This lemma is often proved by diagram chase using the {{< knowl id="snake-lemma" text="snake lemma" >}} (or via a systematic kernel/cokernel argument in an abelian category). It is a basic tool for proving exactness statements about constructions built from short exact sequences.

## Examples

### Example 1 (modules: quotienting a short exact sequence)
Let \(R\) be a ring and \(M\) an \(R\)-module. Fix submodules \(N_1\subseteq N_2\subseteq M\) and a further submodule \(K\subseteq M\). Consider the diagram with rows/columns induced by inclusions and quotient maps:
\[
\begin{array}{ccccccccc}
0 &\to& N_1\cap K &\to& N_1 &\to& N_1/(N_1\cap K) &\to& 0\\
&& \downarrow && \downarrow && \downarrow && \\
0 &\to& N_2\cap K &\to& N_2 &\to& N_2/(N_2\cap K) &\to& 0\\
&& \downarrow && \downarrow && \downarrow && \\
0 &\to& (N_2\cap K)/(N_1\cap K) &\to& N_2/N_1 &\to& \frac{N_2/(N_2\cap K)}{N_1/(N_1\cap K)} &\to& 0
\end{array}
\]
The first two rows and all columns are exact by standard submodule/quotient arguments (see {{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequences of modules" >}}). The nine lemma then gives exactness of the third row, i.e. a canonical short exact sequence describing the quotient \(N_2/N_1\) in terms of intersections with \(K\).

### Example 2 (abelian groups: a concrete 3×3 diagram)
Take \(\mathcal A = \mathbf{Ab}\). Consider
\[
0\to \mathbb Z \xrightarrow{\cdot 2} \mathbb Z \to \mathbb Z/2\to 0
\qquad
0\to \mathbb Z \xrightarrow{\cdot 3} \mathbb Z \to \mathbb Z/3\to 0
\]
and build the middle row as \(\mathbb Z \xrightarrow{\cdot 6} \mathbb Z \to \mathbb Z/6\to 0\), with vertical maps the evident multiplications making the squares commute. With the columns chosen as the evident short exact sequences, the nine lemma forces exactness of the bottom row once the other eight sequences are checked.

### Example 3 (recognizing exactness via kernels/cokernels)
In any abelian category, if you know eight out of the nine sequences are exact, the ninth often follows immediately. For instance, if you have computed kernels and cokernels in the first two rows/columns and verified the commutativity, nine lemma saves a separate check that \(\operatorname{im}(C'\to C)=\ker(C\to C'')\) and that \(C\to C''\) is an epimorphism.
