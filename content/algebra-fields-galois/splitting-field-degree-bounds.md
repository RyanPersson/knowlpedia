---
title: "Degree Bounds for Splitting Fields (Separable Case)"
description: "For a separable degree-n polynomial, the splitting field has degree at most n!."
---

**Theorem (Separable bound).**  
Let \(K\) be a field and let \(f\in K[x]\) be a separable polynomial of degree \(n\). If \(L\) is the {{</* knowl id="splitting-field" text="splitting field" */>}} of \(f\) over \(K\), then \(L/K\) is finite and
\[
[L:K] = |\mathrm{Gal}(L/K)| \le n!.
\]
Equivalently, the {{</* knowl id="galois-group" text="Galois group" */>}} injects into the permutation group on the \(n\) roots, so its order is at most \(n!\).

**Examples.**
1. Over \(\mathbb{Q}\), \(f=x^3-2\) is separable of degree \(3\). Its splitting field has degree \(6\), and indeed \(6\le 3!=6\).
2. Over \(\mathbb{Q}\), \(f=x^4-2\) has a splitting field of degree \(8\), and \(8\le 4!=24\).
3. If \(f\) already splits over \(K\), then \(L=K\) and \([L:K]=1\le n!\).

**Related.** {{</* knowl id="splitting-field-existence-uniqueness" text="splitting fields" */>}}, {{</* knowl id="separable-distinct-roots" text="separable ⇔ distinct roots" */>}}.
