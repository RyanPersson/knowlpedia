---
title: "Primary decomposition in Noetherian rings"
description: "In a Noetherian ring, every ideal is a finite intersection of primary ideals."
---

Primary decomposition is a way to express an ideal as an intersection of “power-of-a-prime” pieces. The phenomenon is special to {{< knowl id="noetherian-ring" text="Noetherian rings" >}} and is formalized by the {{< knowl id="lasker-noether-theorem" text="Lasker–Noether theorem" >}}. See also {{< knowl id="primary-decomposition" text="primary decomposition" >}} for the general language.

## Definition (primary ideal)
Let \(R\) be a commutative ring and let \(Q \subsetneq R\) be an ideal.  
\(Q\) is **primary** if whenever \(ab \in Q\) and \(a \notin Q\), there exists \(n \ge 1\) such that \(b^n \in Q\).

Equivalently, in \(R/Q\) every zero-divisor is nilpotent.

## Theorem (Noetherian primary decomposition)
Let \(R\) be a commutative {{< knowl id="noetherian-ring" text="Noetherian ring" >}} and let \(I \subseteq R\) be an ideal. Then there exist primary ideals \(Q_1,\dots,Q_r\) such that
\[
I = Q_1 \cap \cdots \cap Q_r .
\]
One can choose the decomposition so that the radicals \(\sqrt{Q_i}\) are distinct {{< knowl id="prime-spectrum" text="prime ideals" >}}. In any *minimal* primary decomposition (no redundant components and with distinct radicals), the set of prime ideals \(\{\sqrt{Q_1},\dots,\sqrt{Q_r}\}\) depends only on \(I\), not on the choice of decomposition.

## Examples
1. **A reduced principal ideal in a polynomial ring.**  
   In \(k[x,y]\), the ideal \((xy)\) decomposes as
   \[
   (xy) = (x) \cap (y).
   \]
   Here \((x)\) and \((y)\) are prime ideals (hence primary).

2. **A decomposition with an embedded component.**  
   In \(k[x,y]\),
   \[
   (x^2,xy) = (x) \cap (x^2,y).
   \]
   Indeed, if \(f \in (x) \cap (x^2,y)\), then \(f=xg\) and \(xg \in (x^2,y)\) forces \(g \in (x,y)\), so \(f \in (x^2,xy)\).  
   The ideal \((x)\) is prime, and \((x^2,y)\) is \((x,y)\)-primary since its radical is \((x,y)\).

3. **In the integers.**  
   In \(\mathbb Z\),
   \[
   (12) = (4) \cap (3).
   \]
   The ideal \((4)\) is \((2)\)-primary and \((3)\) is prime (hence primary).
