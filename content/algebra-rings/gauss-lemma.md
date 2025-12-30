---
title: "Gauss's lemma"
description: "Over a UFD, primitive polynomials factor over the fraction field exactly when they factor over the ring."
---

**Gauss's lemma**: Let \(R\) be a {{< knowl id="ufd" text="UFD" >}} with {{< knowl id="fraction-field" text="fraction field" >}} \(K\). If \(f\in R[x]\) is {{< knowl id="primitive-polynomial" text="primitive" >}}, then any factorization \(f=gh\) in the {{< knowl id="polynomial-ring" text="polynomial ring" >}} \(K[x]\) can be written (after multiplying \(g,h\) by nonzero scalars in \(K\)) as a factorization \(f=g'h'\) with \(g',h'\in R[x]\) primitive. In particular, a primitive \(f\in R[x]\) is {{< knowl id="irreducible-polynomial" text="irreducible" >}} in \(R[x]\) if and only if it is irreducible in \(K[x]\).

This rests on the {{< knowl id="gauss-content-lemma" text="content multiplicativity lemma" >}} and is the key bridge between factorization over \(R\) and over its field of fractions.

**Proof sketch**: Clear denominators to write \(f=c\cdot \tilde g\tilde h\) with \(\tilde g,\tilde h\in R[x]\) and \(c\in R\setminus\{0\}\). Taking contents and using multiplicativity forces \(c\) to be a unit when \(f\) is primitive, so \(f\) factors in \(R[x]\). Irreducibility equivalence follows by contrapositive.