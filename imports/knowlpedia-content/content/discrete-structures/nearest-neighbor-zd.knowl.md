+++
id = "discrete-structures/nearest-neighbor-zd"
title = "Nearest-neighbor adjacency on Z^d"
kind = "knowl"
summary = "The standard notion of adjacency on the integer lattice where points differ by 1 in one coordinate."
aliases = ["nearest-neighbor-zd", "Nearest-neighbor adjacency on Z^d"]
domains = ["discrete-structures"]
legacy_source_path = "discrete-structures/nearest-neighbor-zd.md"
+++

On the lattice [[discrete-structures/lattice-zd|lattice-zd]], two sites \(x,y\in\mathbb{Z}^d\) are **nearest neighbors** (written \(x\sim y\)) if they differ by \(1\) in exactly one coordinate and agree in all others.

Equivalently, using the \(\ell^1\) norm,
\[
x\sim y \quad\Longleftrightarrow\quad \|x-y\|_1 = 1,
\]
where \(\|z\|_1 := \sum_{i=1}^d |z_i|\).

A convenient characterization is:
\[
y = x \pm e_i \text{ for some } i\in\{1,\dots,d\},
\]
where \(e_i\) is the \(i\)-th standard basis vector.

**Degree.** Each site in \(\mathbb{Z}^d\) has exactly \(2d\) nearest neighbors.

This adjacency relation turns \(\mathbb{Z}^d\) into an infinite graph, sometimes called the **nearest-neighbor lattice graph**.
