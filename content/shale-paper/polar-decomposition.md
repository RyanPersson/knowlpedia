---
title: "Polar Decomposition"
description: "Writing T as a unitary/orthogonal part times a positive part"
---

Any invertible bounded operator \(T\) on a Hilbert space has a **polar decomposition**
\[
T=u(T)\,|T|,\quad |T|=(T^*T)^{1/2}\ge 0,
\]
where \(u(T)\) is unitary (complex case) or orthogonal (real case).

**Key properties (paper use):**
- Used to define {{< knowl id="restricted-general-linear-group-rgl" text="rGL(H)" >}} via \(|T|\in GL(H)_2\).
- Lets one reduce many proofs to the positive cone (e.g. \(Sp(K)^+\)).

**Example:** If \(T\) is positive selfadjoint, then \(u(T)=I\) and \(|T|=T\).
