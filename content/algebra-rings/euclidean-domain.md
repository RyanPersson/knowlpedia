---
title: "Euclidean domain"
description: "An integral domain admitting division with remainder controlled by a Euclidean function."
---

A **Euclidean domain** is an {{< knowl id="integral-domain" text="integral domain" >}} $R$ equipped with a function $\delta:R\setminus\{0\}\to \mathbb{N}$ such that for all $a\in R$ and $b\in R\setminus\{0\}$, there exist $q,r\in R$ with $a=bq+r$ and either $r=0$ or $\delta(r)<\delta(b)$.

This “division algorithm” implies the {{< knowl id="euclidean-algorithm" text="Euclidean algorithm" >}} and ensures existence of {{< knowl id="gcd" text="gcds" >}}. In particular, every Euclidean domain is a {{< knowl id="pid" text="PID" >}} (see {{< knowl id="euclidean-implies-pid" text="Euclidean implies PID" >}}).

**Examples:**
- $\mathbb{Z}$ with $\delta(n)=|n|$ is Euclidean.
- If $k$ is a field, then $k[x]$ is Euclidean with $\delta(f)=\deg(f)$ for $f\neq 0$.
- $k[x,y]$ is not Euclidean (it is not even a PID).