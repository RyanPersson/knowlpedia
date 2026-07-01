+++
id = "algebra-commutative/simple-artinian-matrix-ring"
title = "Simple Artinian rings are matrix rings over division rings"
kind = "knowl"
summary = "A simple Artinian ring is isomorphic to a full matrix ring over a division ring."
aliases = ["simple-artinian-matrix-ring", "Simple Artinian rings are matrix rings over division rings"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/simple-artinian-matrix-ring.md"
+++

A central structure theorem in ring theory is that “finite-length” (Artinian) simple rings are precisely matrix rings over division rings. This is the simplest nontrivial case of the [[algebra-rings/artin-wedderburn-theorem|Artin–Wedderburn theorem]].

## Theorem

Let $R$ be a ring (not necessarily commutative). Assume:
- $R$ is **simple** (it has no nonzero proper two-sided ideals), and
- $R$ is [[algebra-commutative/artinian-ring|Artinian]] (equivalently, it is Artinian as a left or right module over itself).

Then there exist an integer $n\ge 1$ and a [[algebra-rings/division-ring|division ring]] $D$ such that
\[
R \cong M_n(D)
\]
as rings, where $M_n(D)$ denotes the ring of $n\times n$ matrices over $D$.

A useful refinement is that $D$ may be taken to be the endomorphism ring of a simple right $R$-module (a division ring by Schur’s lemma), and $n$ corresponds to the multiplicity with which that simple module appears in a decomposition of $R$ as a module over itself. The general semisimple case (finite products of such matrix rings) is encoded in [[algebra-commutative/semisimple-artinian-product|the semisimple Artinian product decomposition]].

In the commutative setting, this theorem collapses strongly: if $R$ is commutative and simple Artinian, then necessarily $n=1$ and $D$ is commutative, so $R$ is a [[algebra-rings/field|field]].

## Examples

1. **Matrix rings over a field.**
   For any field $k$ and any $n\ge 1$, the ring $M_n(k)$ is simple Artinian. Here $D=k$.

2. **Division rings (the case $n=1$).**
   Any division ring $D$ is simple Artinian, and the theorem recovers it as $M_1(D)\cong D$. For instance, the real quaternions $\mathbb H$ form a (noncommutative) division ring, hence are simple Artinian.

3. **Why “simple” matters.**
   The ring $k\times k$ is Artinian and semisimple, but not simple: it has nontrivial two-sided ideals $k\times 0$ and $0\times k$. Accordingly, it is not a single matrix ring, but it fits the product form described by [[algebra-commutative/semisimple-artinian-product|semisimple Artinian product decomposition]].

This theorem is frequently used alongside Jacobson radical facts such as [[algebra-commutative/jacobson-annihilates-simples|the Jacobson radical annihilates simple modules]], since in the semisimple Artinian setting the Jacobson radical is zero.
