+++
id = "convex-analysis/convex-hull-is-the-smallest-convex-set-containing"
title = "Convex hull is the smallest convex set containing Ω"
kind = "knowl"
summary = "co(Ω) is convex, contains Ω, and lies in every convex superset of Ω"
aliases = ["convex-hull-is-the-smallest-convex-set-containing", "Convex hull is the smallest convex set containing Ω"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convex-hull-is-the-smallest-convex-set-containing.md"
+++

**Proposition.**
For any set $\Omega\subset X$ in a real vector space, the [[convex-analysis/convex-hull|convex hull]] $\mathrm{co}(\Omega)$ satisfies:

1. $\mathrm{co}(\Omega)$ is [[convex-analysis/convex-set|convex]].
2. $\Omega\subset \mathrm{co}(\Omega)$.
3. If $C$ is convex and $\Omega\subset C$, then $\mathrm{co}(\Omega)\subset C$.

**Context.** This states precisely that $\mathrm{co}(\Omega)$ is the minimal convex superset of $\Omega$.

**Proof sketch.** By construction, $\mathrm{co}(\Omega)$ is an intersection of convex sets containing $\Omega$, so it contains $\Omega$ and is contained in each such set. Convexity follows from closure of convexity under intersections.
