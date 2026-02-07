---
title: "Symplectic manifold"
description: "A smooth manifold equipped with a closed, nondegenerate 2-form."
---

A **symplectic manifold** is a pair \((M,\omega)\) where \(M\) is a smooth manifold and \(\omega \in \Omega^2(M)\) is a differential \(2\)-form such that:

1. **Nondegeneracy:** for every \(p\in M\), the bilinear form \(\omega_p:T_pM\times T_pM\to \mathbb{R}\) is nondegenerate. Equivalently,
   $$
   \iota_v \omega_p = 0 \quad\Longrightarrow\quad v=0 \quad (v\in T_pM),
   $$
   or equivalently the map \(T_pM \to T_p^*M\), \(v\mapsto \iota_v\omega_p\), is an isomorphism.

2. **Closedness:**
   $$
   d\omega = 0.
   $$

These conditions force \(\dim M\) to be even, say \(\dim M = 2n\), and \(\omega^n\) is nowhere vanishing. In particular, \(\omega^n/n!\) is a canonical volume form and orients \(M\):
$$
\frac{1}{n!}\,\omega^{\wedge n} \neq 0 \quad \text{everywhere on } M.
$$

### Darboux theorem (local normal form)
A fundamental feature of symplectic geometry is that symplectic forms have **no local invariants**: for each \(p\in M\) there exist local coordinates \((q_1,\dots,q_n,p_1,\dots,p_n)\) near \(p\) such that
$$
\omega = \sum_{i=1}^n dq_i \wedge dp_i .
$$

### Hamiltonian vector fields
Given a smooth function \(H\in C^\infty(M)\) (a Hamiltonian), the **Hamiltonian vector field** \(X_H\) is defined by
$$
\iota_{X_H}\omega = dH.
$$
Nondegeneracy guarantees \(X_H\) exists and is unique. The flow of \(X_H\) preserves \(\omega\) (it is a symplectomorphism flow).

### Closedness and Stokes
Because \(d\omega=0\), Stokes' theorem implies that \(\omega\) integrates to zero over boundaries: for any suitable \(3\)-chain \(C\),
$$
\int_{\partial C}\omega = \int_C d\omega = 0.
$$
See {{< knowl id="stokes-theorem" text="Stokes' theorem" >}}.
