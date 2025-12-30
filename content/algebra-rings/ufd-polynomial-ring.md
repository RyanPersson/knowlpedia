---
title: "Gauss's theorem (UFD ⇒ polynomial ring is UFD)"
description: "If R is a UFD, then the polynomial ring R[x] is again a UFD (and likewise in finitely many variables)."
---

**Gauss's theorem**: If \(R\) is a {{< knowl id="ufd" text="UFD" >}}, then the {{< knowl id="polynomial-ring" text="polynomial ring" >}} \(R[x]\) is a UFD. More generally, \(R[x_1,\dots,x_n]\) is a UFD for all \(n\ge 1\).

**Proof sketch**: Let \(K\) be the {{< knowl id="fraction-field" text="fraction field" >}} of \(R\). Since \(K\) is a field, \(K[x]\) is a PID (hence a UFD). Using {{< knowl id="gauss-lemma" text="Gauss's lemma" >}}, factorizations and irreducibility questions for primitive polynomials lift between \(R[x]\) and \(K[x]\), yielding unique factorization in \(R[x]\).