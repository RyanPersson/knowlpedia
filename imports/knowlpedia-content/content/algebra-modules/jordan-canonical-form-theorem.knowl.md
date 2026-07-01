+++
id = "algebra-modules/jordan-canonical-form-theorem"
title = "Jordan canonical form theorem"
kind = "knowl"
summary = "Over a splitting field, every linear operator is similar to a direct sum of Jordan blocks."
aliases = ["jordan-canonical-form-theorem", "Jordan canonical form theorem"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/jordan-canonical-form-theorem.md"
+++

**Jordan canonical form theorem**: Let \(T\) be a linear operator on a finite-dimensional vector space \(V\) over an algebraically closed field \(k\) (more generally, assume the characteristic polynomial splits over \(k\)). Then there exists a basis of \(V\) in which the matrix of \(T\) is block diagonal with blocks of the form \(J_{m}(\lambda)\), where \(\lambda\) ranges over the [[linear-algebra/eigenvalue|eigenvalues]] of \(T\). Each Jordan block corresponds to a chain of generalized [[linear-algebra/eigenvector|eigenvectors]], and the multiset of block sizes for each \(\lambda\) is uniquely determined by \(T\) up to permutation.

In this form, \(T\) is [[algebra-modules/diagonalizable|diagonalizable]] exactly when all Jordan blocks have size \(1\). The sizes of Jordan blocks are governed by the primary decomposition of the \(k[x]\)-module associated to \(T\), and can be derived from the [[linear-algebra/minimal-polynomial|minimal polynomial]]; one route is through the [[algebra-modules/rational-canonical-form-theorem|rational canonical form theorem]]
