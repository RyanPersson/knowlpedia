+++
id = "shale-paper/polar-decomposition"
title = "Polar Decomposition"
kind = "knowl"
summary = "Writing T as a unitary/orthogonal part times a positive part"
aliases = ["polar-decomposition", "Polar Decomposition"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/polar-decomposition.md"
+++

Any invertible bounded operator \(T\) on a Hilbert space has a **polar decomposition**
\[
T=u(T)\,|T|,\quad |T|=(T^*T)^{1/2}\ge 0,
\]
where \(u(T)\) is unitary (complex case) or orthogonal (real case).

**Key properties (paper use):**
- Used to define [[shale-paper/restricted-general-linear-group-rgl|rGL(H)]] via \(|T|\in GL(H)_2\).
- Lets one reduce many proofs to the positive cone (e.g. \(Sp(K)^+\)).

**Example:** If \(T\) is positive selfadjoint, then \(u(T)=I\) and \(|T|=T\).
