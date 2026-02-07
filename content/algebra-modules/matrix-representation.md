---
title: "Matrix representation"
description: "A matrix encoding a linear map relative to chosen bases."
---

The **matrix representation** of a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}} \(T: V \to W\) with respect to bases \(\mathcal{B} = \{v_1, \ldots, v_n\}\) of \(V\) and \(\mathcal{C} = \{w_1, \ldots, w_m\}\) of \(W\) is the \(m \times n\) {{< knowl id="matrix" section="linear-algebra" text="matrix" >}} \([T]_{\mathcal{B}}^{\mathcal{C}}\) whose columns are the coordinate vectors of \(T(v_j)\) in the basis \(\mathcal{C}\).

That is, if \(T(v_j) = \sum_{i=1}^m a_{ij} w_i\), then the \((i,j)\) entry of the matrix is \(a_{ij}\).

## Properties
- **Composition**: \([ST]_{\mathcal{B}}^{\mathcal{D}} = [S]_{\mathcal{C}}^{\mathcal{D}} [T]_{\mathcal{B}}^{\mathcal{C}}\).
- **Change of basis**: If \(P\) is the change-of-basis matrix from \(\mathcal{B}\) to \(\mathcal{B}'\), then \([T]_{\mathcal{B}'}^{\mathcal{C}'} = Q^{-1} [T]_{\mathcal{B}}^{\mathcal{C}} P\).
- **Similarity**: Two matrices represent the same operator (different bases) iff they are similar.

## Standard representation
For \(T: \mathbb{R}^n \to \mathbb{R}^m\), the standard matrix is \([T(e_1) \mid \cdots \mid T(e_n)]\).

## Invariants
The {{< knowl id="rank" section="linear-algebra" text="rank" >}}, {{< knowl id="determinant" section="linear-algebra" text="determinant" >}} (for square matrices), and {{< knowl id="eigenvalue" section="linear-algebra" text="eigenvalues" >}} are independent of the basis choice.
