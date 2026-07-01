+++
id = "shale-paper/restricted-general-linear-group-rgl"
title = "Restricted General Linear Group rGL(H)"
kind = "knowl"
summary = "Invertible operators whose positive part differs from I by a Hilbert–Schmidt operator"
aliases = ["restricted-general-linear-group-rgl", "Restricted General Linear Group rGL(H)"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/restricted-general-linear-group-rgl.md"
+++

Shale's **restricted general linear group** is
\[
rGL(H)=\{T\in GL(H): |T|=(T^*T)^{1/2}\in GL(H)_2\}.
\]

Equivalently, \(|T|-I\) is [[shale-paper/hilbert-schmidt-operator|Hilbert–Schmidt]].
This group is exactly where the Gaussian measure in §3 is quasi-invariant.

**Key properties:**
- Stable under [[shale-paper/polar-decomposition|polar decomposition]] \(T=u(T)|T|\).
- Carries the "change-of-variables" unitary rep [[shale-paper/segal-unitary-representation-Ufrak|𝔘(T)]] on \(L_2(M,n)\).

**Example:** In finite dimensions, \(rGL(H)=GL(H)\).
