---
title: "Nullstellensatz corollary: maximal ideals are points"
description: "Over an algebraically closed field, maximal ideals of a polynomial ring are exactly the ideals of points."
---

A key consequence of the {{< knowl id="nullstellensatz-variety-correspondence" text="Nullstellensatz variety correspondence" >}} is that maximal ideals in a polynomial ring over an algebraically closed field have an explicit and geometric form.

## Corollary (Weak Nullstellensatz / maximal ideals of \(k[x_1,\dots,x_n]\))
Let \(k\) be an algebraically closed {{< knowl id="field" section="algebra-rings" text="field" >}}. If \(\mathfrak m \subset k[x_1,\dots,x_n]\) is a maximal ideal, then there exists a point
\(a=(a_1,\dots,a_n) \in k^n\) such that
\[
\mathfrak m = (x_1-a_1,\dots,x_n-a_n).
\]
Equivalently, the {{< knowl id="maximal-spectrum" text="maximal spectrum" >}} of \(k[x_1,\dots,x_n]\) is naturally identified with the set of \(k\)-rational points \(k^n\), and the {{< knowl id="residue-field" text="residue field" >}} at \(\mathfrak m\) is canonically \(k\).

Under this identification, the subspace topology induced from the {{< knowl id="zariski-topology" text="Zariski topology" >}} on {{< knowl id="prime-spectrum" text="Spec" >}} agrees with the usual “vanishing set” Zariski topology on \(k^n\).

## Examples
1. **One variable.**  
   In \(\mathbb C[x]\), every maximal ideal is of the form \((x-a)\) for a unique \(a \in \mathbb C\).

2. **Two variables.**  
   In \(\mathbb C[x,y]\), the ideal \((x-1,\; y+2)\) is maximal and corresponds to the point \((1,-2) \in \mathbb C^2\).

3. **A non-maximal ideal and the points above it.**  
   In \(\mathbb C[x]\), the ideal \((x^2+1)\) is not maximal because \(x^2+1=(x-i)(x+i)\). The maximal ideals containing \((x^2+1)\) are \((x-i)\) and \((x+i)\), corresponding to the two points \(i\) and \(-i\).
