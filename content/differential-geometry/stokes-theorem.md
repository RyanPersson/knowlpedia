---
title: "Stokes' theorem"
description: "Generalization of the fundamental theorem of calculus to differential forms on oriented manifolds with boundary."
---

Let \(M\) be an oriented smooth \(n\)-manifold with (possibly empty) boundary \(\partial M\), and let \(\iota:\partial M \hookrightarrow M\) be the inclusion. If \(\alpha \in \Omega^{n-1}(M)\) is smooth and either compactly supported in the interior of \(M\) or \(M\) is compact with \(\alpha\) smooth up to the boundary, then **Stokes' theorem** states
$$
\int_M d\alpha \;=\; \int_{\partial M} \iota^*\alpha .
$$

### Orientation convention
The boundary \(\partial M\) is oriented by the **outward-normal-first** rule: a basis \((v_1,\dots,v_{n-1})\) of \(T_p(\partial M)\) is positively oriented if \((\nu, v_1,\dots,v_{n-1})\) is a positively oriented basis of \(T_p M\), where \(\nu\) points outward (or is a chosen outward-pointing normal vector field along \(\partial M\)).

### Key special cases
Stokes' theorem unifies several classical theorems:

- **Fundamental theorem of calculus** (\(n=1\)): for \(\alpha=f\) (a \(0\)-form) on \([a,b]\),
  $$
  \int_{[a,b]} df \;=\; \int_{\{b\}} f - \int_{\{a\}} f \;=\; f(b)-f(a).
  $$
- **Green's theorem** and the **divergence theorem** arise from choosing appropriate \((n-1)\)-forms corresponding to vector fields.
- The classical **Kelvin–Stokes theorem** in \(\mathbb{R}^3\) is the case \(n=2\) applied to a surface with boundary.

### Useful corollaries
- If \(\partial M=\varnothing\), then for any \(\alpha \in \Omega^{n-1}(M)\),
  $$
  \int_M d\alpha = 0.
  $$
- If \(\beta\) is a closed \(k\)-form (\(d\beta=0\)), then \(\int_{\partial C} \beta = 0\) for any \((k+1)\)-chain \(C\) for which the integrals make sense, since \(\int_{\partial C}\beta=\int_C d\beta\).

For an important class of closed \(2\)-forms, see {{< knowl id="symplectic-manifold" text="symplectic manifolds" >}}.
