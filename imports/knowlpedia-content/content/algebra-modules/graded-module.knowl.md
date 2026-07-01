+++
id = "algebra-modules/graded-module"
title = "Graded module"
kind = "knowl"
summary = "A module decomposed into degrees compatible with a graded ring action."
aliases = ["graded-module", "Graded module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/graded-module.md"
+++

A **graded module** over a graded ring \(R=\bigoplus_{n}R_n\) is an \(R\)-[[algebra-modules/module|module]] \(M\) together with a direct-sum decomposition
\[
M=\bigoplus_{n\in\mathbb Z} M_n
\]
(as an internal [[algebra-modules/direct-sum-modules|direct sum]] of abelian groups) such that \(R_i\cdot M_j\subseteq M_{i+j}\) for all \(i,j\). A homomorphism of graded modules is typically required to preserve degree (or have specified degree shift).

Graded modules are the natural linear objects over a [[algebra-modules/graded-ring|graded ring]] and encode “homogeneous” algebra in commutative algebra and algebraic geometry.

**Examples:**
- Any graded ring \(R\) is a graded \(R\)-module over itself, with the same decomposition \(R=\bigoplus R_n\).
- If \(R\) is graded and \(I\subseteq R\) is a homogeneous [[algebra-rings/ideal|ideal]], then \(R/I\) is a graded module (and graded ring) with \((R/I)_n = R_n/(I\cap R_n)\).
