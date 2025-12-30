---
title: "Hilbert's Nullstellensatz (weak)"
description: "Over an algebraically closed field, every proper ideal in a polynomial ring has a common zero."
---

**Hilbert's Nullstellensatz (weak)**: Let \(k\) be an algebraically closed {{< knowl id="field" text="field" >}}, and let \(I\) be a proper {{< knowl id="ideal" text="ideal" >}} of the {{< knowl id="polynomial-ring" text="polynomial ring" >}} \(k[x_1,\dots,x_n]\). Then the affine variety
\[
V(I)=\{a\in k^n : f(a)=0\text{ for all }f\in I\}
\]
is nonempty.

Equivalently, every {{< knowl id="maximal-ideal" text="maximal ideal" >}} of \(k[x_1,\dots,x_n]\) has the form \((x_1-a_1,\dots,x_n-a_n)\) for some \(a=(a_1,\dots,a_n)\in k^n\).

**Proof sketch**: If \(\mathfrak m\) is maximal, then \(A:=k[x_1,\dots,x_n]/\mathfrak m\) is a finitely generated \(k\)-algebra that is a field. The images of the \(x_i\) are algebraic over \(k\); algebraic closedness forces \(A\cong k\), giving \(\mathfrak m=(x_1-a_1,\dots,x_n-a_n)\) and hence a common zero.