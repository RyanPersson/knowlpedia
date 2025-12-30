---
title: "Hom module"
description: "The module (or abelian group) of module homomorphisms between two modules."
---

A **Hom module** \(\mathrm{Hom}_R(M,N)\) is the set of all {{< knowl id="module-homomorphism" text="module homomorphisms" >}} \(f\colon M\to N\) between \(R\)-{{< knowl id="module" text="modules" >}}, equipped with pointwise addition \((f+g)(m)=f(m)+g(m)\). This makes \(\mathrm{Hom}_R(M,N)\) an abelian group. If \(R\) is a {{< knowl id="commutative-ring" text="commutative ring" >}}, then \(\mathrm{Hom}_R(M,N)\) is naturally an \(R\)-module via \((r\cdot f)(m)=r\,f(m)\).

In the noncommutative setting, additional module structures arise from bimodules: if \(M\) is an \((R,S)\)-{{< knowl id="bimodule" text="bimodule" >}} and \(N\) is a left \(R\)-module, then \(\mathrm{Hom}_R(M,N)\) carries a natural left \(S\)-module structure by \((s\cdot f)(m)=f(ms)\).

**Examples:**
- For any left \(R\)-module \(M\), evaluation at \(1\) gives \(\mathrm{Hom}_R(R,M)\cong M\).
- If \(V,W\) are {{< knowl id="vector-space" text="vector spaces" >}} over a field \(k\), then \(\mathrm{Hom}_k(V,W)\) is a vector space, naturally isomorphic to the space of \(k\)-linear maps \(V\to W\).
