---
title: "Convex hull is the smallest convex set containing Ω"
description: "co(Ω) is convex, contains Ω, and lies in every convex superset of Ω"
---

**Proposition.**
For any set $\Omega\subset X$ in a real vector space, the {{< knowl id="convex-hull" text="convex hull" >}} $\mathrm{co}(\Omega)$ satisfies:

1. $\mathrm{co}(\Omega)$ is {{< knowl id="convex-set" text="convex" >}}.
2. $\Omega\subset \mathrm{co}(\Omega)$.
3. If $C$ is convex and $\Omega\subset C$, then $\mathrm{co}(\Omega)\subset C$.

**Context.** This states precisely that $\mathrm{co}(\Omega)$ is the minimal convex superset of $\Omega$.

**Proof sketch.** By construction, $\mathrm{co}(\Omega)$ is an intersection of convex sets containing $\Omega$, so it contains $\Omega$ and is contained in each such set. Convexity follows from closure of convexity under intersections.
