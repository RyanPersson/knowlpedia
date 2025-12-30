---
title: "Composition series"
description: "A finite chain of submodules with simple successive quotients."
---

A **composition series** of an $R$-module $M$ is a finite chain of {{</* knowl id="submodule" text="submodules" */>}}
\[
0=M_0 \subset M_1 \subset \cdots \subset M_n = M
\]
such that each factor $M_i/M_{i-1}$ is a {{</* knowl id="simple-module" text="simple module" */>}} (a simple quotient in the sense of {{</* knowl id="quotient-module" text="quotient modules" */>}}). The integer $n$ is the length of the series and, when a composition series exists, is an invariant of $M$ (Jordan–Hölder), recorded as the module {{</* knowl id="length-module" text="length" */>}}.

Composition series exist exactly for modules of finite length and provide a canonical way to “factor” modules into simple pieces.

**Examples:**
- For the $\mathbb Z$-module $\mathbb Z/p^k\mathbb Z$, the chain
  $0\subset p^{k-1}\mathbb Z/p^k\mathbb Z \subset \cdots \subset p\mathbb Z/p^k\mathbb Z \subset \mathbb Z/p^k\mathbb Z$
  is a composition series.
- For an $n$-dimensional vector space $V$ over a field, any flag $0\subset V_1\subset\cdots\subset V_n=V$ with $\dim(V_i)=i$ is a composition series.
- (Nonexample) The $\mathbb Z$-module $\mathbb Z$ has no composition series.
