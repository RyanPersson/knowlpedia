---
title: "Finite box in the lattice"
description: "A finite cube-shaped subset of the integer lattice used as a finite region."
---

A **finite box** (or **finite cube**) in the lattice {{< knowl id="lattice-zd" >}} is a finite region of the form
\[
\Lambda_L := \{x=(x_1,\dots,x_d)\in\mathbb{Z}^d : |x_i|\le L \text{ for all } i\},
\]
where \(L\) is a nonnegative {{< knowl id="natural-numbers" section="shared-foundations" >}}.

This is the cube centered at the origin with side length \(2L+1\) (in lattice units). Its cardinality is
\[
|\Lambda_L|=(2L+1)^d.
\]

**Translations and other conventions.**
- Any translate \(\Lambda_L+a:=\{x+a:x\in\Lambda_L\}\) is also a finite box.
- Some authors use \(\{0,1,\dots,L-1\}^d\) as the “box of side length \(L\)”; this differs from \(\Lambda_L\) by translation and a minor change of parameter.

Finite boxes are common choices of “finite volume” regions for lattice models; associated notions of {{< knowl id="boundary-finite-region" >}} describe sites or edges near the complement.
