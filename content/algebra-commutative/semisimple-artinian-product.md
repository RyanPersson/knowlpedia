---
title: "Semisimple Artinian rings decompose as finite products"
description: "A semisimple Artinian ring is a finite product of simple Artinian rings; if commutative, it is a finite product of fields."
---

A *semisimple Artinian ring* (see {{< knowl id="artinian-semisimple-ring" section="algebra-rings" text="semisimple Artinian ring" >}}) is, in particular, an {{< knowl id="artinian-ring" text="Artinian ring" >}} whose module theory has no nontrivial extensions. The structure theorem is a product decomposition into simple pieces.

## Theorem (product decomposition)
Let \(R\) be a semisimple Artinian ring (not assumed commutative). Then there exist simple Artinian rings \(R_1,\dots,R_t\) such that
\[
R \cong R_1 \times \cdots \times R_t .
\]
Moreover, each \(R_i\) is a matrix ring over a division ring: \(R_i \cong M_{n_i}(D_i)\). This refinement is exactly the content of the {{< knowl id="artin-wedderburn-theorem" section="algebra-rings" text="Artin–Wedderburn theorem" >}}, and the simple-factor description is packaged in {{< knowl id="simple-artinian-matrix-ring" text="simple Artinian matrix rings" >}}.

If \(R\) is also {{< knowl id="commutative-ring" section="algebra-rings" text="commutative" >}}, then every simple Artinian factor must be a {{< knowl id="field" section="algebra-rings" text="field" >}} (since a commutative division ring is a field, and commutativity forces \(n_i=1\)). Hence in the commutative case,
\[
R \cong K_1 \times \cdots \times K_t
\]
for fields \(K_i\).

## Examples
1. **Squarefree integers (commutative case).**  
   By the {{< knowl id="chinese-remainder-theorem" section="algebra-rings" text="Chinese remainder theorem" >}},
   \(\mathbb Z/6\mathbb Z \cong \mathbb Z/2\mathbb Z \times \mathbb Z/3\mathbb Z\).  
   Both factors are fields, so \(\mathbb Z/6\mathbb Z\) is a commutative semisimple Artinian ring.

2. **Finite products of fields.**  
   For any field \(k\), the ring \(k \times k \times k\) is semisimple Artinian (each factor is simple Artinian), and it is already presented in the product form of the theorem.

3. **An Artinian ring that is not semisimple.**  
   The ring \(\mathbb Z/4\mathbb Z\) is Artinian, but it is not semisimple: the class of \(2\) is nonzero and nilpotent since \(2^2=0\) mod \(4\). Equivalently, its {{< knowl id="jacobson-radical-intersection-maximals" text="Jacobson radical" >}} is nonzero, so it cannot be semisimple.
