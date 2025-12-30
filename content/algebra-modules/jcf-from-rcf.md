---
title: "Jordan canonical form from rational canonical form"
description: "When the relevant polynomials split, rational canonical form refines to Jordan form."
---

**Jordan canonical form from rational canonical form**: Let $V$ be a finite-dimensional vector space over a field $F$, and let $T:V\to V$ be linear. Assume the characteristic polynomial of $T$ splits over $F$ (for example, $F$ is algebraically closed). Then there exists a basis of $V$ for which the matrix of $T$ is in Jordan canonical form.

This follows by refining the invariant-factor decomposition in {{< knowl id="rcf-from-structure-theorem" text="rational canonical form from the structure theorem" >}} into primary factors, yielding the {{< knowl id="jordan-canonical-form-theorem" text="Jordan canonical form theorem" >}}; the Jordan blocks are organized by the roots of the {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}}.
