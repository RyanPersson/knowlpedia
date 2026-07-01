+++
id = "discrete-structures/finite-box-lattice"
title = "Finite box in the lattice"
kind = "knowl"
summary = "A finite cube-shaped subset of the integer lattice used as a finite region."
aliases = ["finite-box-lattice", "Finite box in the lattice"]
domains = ["discrete-structures"]
legacy_source_path = "discrete-structures/finite-box-lattice.md"
+++

A **finite box** (or **finite cube**) in the lattice [[discrete-structures/lattice-zd|lattice-zd]] is a finite region of the form
\[
\Lambda_L := \{x=(x_1,\dots,x_d)\in\mathbb{Z}^d : |x_i|\le L \text{ for all } i\},
\]
where \(L\) is a nonnegative [[shared-foundations/natural-numbers|natural-numbers]].

This is the cube centered at the origin with side length \(2L+1\) (in lattice units). Its cardinality is
\[
|\Lambda_L|=(2L+1)^d.
\]

**Translations and other conventions.**
- Any translate \(\Lambda_L+a:=\{x+a:x\in\Lambda_L\}\) is also a finite box.
- Some authors use \(\{0,1,\dots,L-1\}^d\) as the “box of side length \(L\)”; this differs from \(\Lambda_L\) by translation and a minor change of parameter.

Finite boxes are common choices of “finite volume” regions for lattice models; associated notions of [[discrete-structures/boundary-finite-region|boundary-finite-region]] describe sites or edges near the complement.
