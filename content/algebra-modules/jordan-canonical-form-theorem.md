---
title: "Jordan canonical form theorem"
description: "Over a splitting field, every linear operator is similar to a direct sum of Jordan blocks."
---

**Jordan canonical form theorem**: Let \(T\) be a linear operator on a finite-dimensional vector space \(V\) over an algebraically closed field \(k\) (more generally, assume the characteristic polynomial splits over \(k\)). Then there exists a basis of \(V\) in which the matrix of \(T\) is block diagonal with blocks of the form \(J_{m}(\lambda)\), where \(\lambda\) ranges over the {{</* knowl id="eigenvalue" text="eigenvalues" */>}} of \(T\). Each Jordan block corresponds to a chain of generalized {{</* knowl id="eigenvector" text="eigenvectors" */>}}, and the multiset of block sizes for each \(\lambda\) is uniquely determined by \(T\) up to permutation.

In this form, \(T\) is {{</* knowl id="diagonalizable" text="diagonalizable" */>}} exactly when all Jordan blocks have size \(1\). The sizes of Jordan blocks are governed by the primary decomposition of the \(k[x]\)-module associated to \(T\), and can be derived from the {{</* knowl id="minimal-polynomial" text="minimal polynomial" */>}}; one route is through the {{</* knowl id="rational-canonical-form-theorem" text="rational canonical form theorem" */>}}

**Proof sketch**: Decompose \(V\) into generalized eigenspaces for each eigenvalue \(\lambda\), reducing to the case where \(T-\lambda I\) is nilpotent. For a nilpotent operator, build a basis from Jordan chains corresponding to a filtration by kernels of powers; these chains yield Jordan blocks. Combine the decompositions across eigenvalues to obtain the full Jordan form.
