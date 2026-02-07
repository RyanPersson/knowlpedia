---
title: "Absolute value preserves integrability"
description: "If a function is Riemann integrable then so is its absolute value, with a triangle inequality."
---

**Absolute value preserves integrability:** Let $f:[a,b]\to\mathbb R$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} on the {{< knowl id="interval" text="interval" >}} $[a,b]$. Then the {{< knowl id="absolute-value" text="absolute value" >}} function $|f|$ is Riemann integrable on $[a,b]$, and the triangle inequality holds:
$$
\left|\int_a^b f\right|\le \int_a^b |f|.
$$

This is often used together with {{< knowl id="riemann-linearity" text="linearity" >}} to control integrals by comparing them to integrals of nonnegative functions.
