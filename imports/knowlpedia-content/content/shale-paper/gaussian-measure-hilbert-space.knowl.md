+++
id = "shale-paper/gaussian-measure-hilbert-space"
title = "Gaussian Measure on a Hilbert Space (Segal)"
kind = "knowl"
summary = "An infinite-dimensional normal distribution built from finite-dimensional projections"
aliases = ["gaussian-measure-hilbert-space", "Gaussian Measure on a Hilbert Space (Segal)"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/gaussian-measure-hilbert-space.md"
+++

Segal's **normal distribution over \(M\)** is a probability space \((N,\mathfrak R,n)\) such that
each [[shale-paper/tame-function|tame function]] \(f(x)=\bar f(Px)\) has expectation
given by the finite-dimensional Gaussian integral on \(\mathrm{ran}(P)\).

**Key properties (paper use):**
- Defines \(L_p(M,n)\) spaces used throughout §3.
- Quasi-invariance under $T$ holds exactly for $T\in \mathrm{rGL}(M)$ (see [[shale-paper/restricted-general-linear-group-rgl|restricted general linear group]]).

**Example:** In finite dimensions, this is the standard density \(\propto e^{-\|x\|^2/2c}\,dx\).
