---
title: "Frattini Argument"
description: "If N is normal and P is a Sylow p-subgroup of N, then G = N N_G(P)"
---

**Frattini Argument**: Let $G$ be a finite {{</* knowl id="group" text="group" */>}}, let $N\trianglelefteq G$ be a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}}, and let $P$ be a {{</* knowl id="sylow-subgroup" text="Sylow p-subgroup" */>}} of $N$ (so $p$ divides $|N|$). Let $N_G(P)$ denote the {{</* knowl id="normalizer" text="normalizer" */>}} of $P$ in $G$. Then
$
G = N\,N_G(P).
$

Equivalently, every $g\in G$ can be written as $g=nn'$ with $n\in N$ and $n'\in N_G(P)$.

**Proof sketch**: For $g\in G$, the conjugate $gPg^{-1}$ is a Sylow $p$-subgroup of $gNg^{-1}=N$ (normality is used here). By the Sylow conjugacy phenomenon inside $N$, there exists $n\in N$ with $n(gPg^{-1})n^{-1}=P$. Then $ng\in N_G(P)$, so $g=n^{-1}(ng)\in N\,N_G(P)$.
