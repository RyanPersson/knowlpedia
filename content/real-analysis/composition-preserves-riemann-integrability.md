---
title: "Composition preserves Riemann integrability"
description: "Composing a Riemann integrable function with a continuous function preserves integrability."
---

**Composition preserves Riemann integrability:** Let $f:[a,b]\to\mathbb R$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} on $[a,b]$, and let $\varphi:J\to\mathbb R$ be {{< knowl id="continuous-map" section="topology" text="continuous" >}} on an {{< knowl id="interval" text="interval" >}} $J$ that contains the range $f([a,b])$. Then $\varphi\circ f$ is Riemann integrable on $[a,b]$.

In particular, taking $\varphi(t)=t^2$ shows that $f^2$ is integrable whenever $f$ is integrable, and taking $\varphi(t)=|t|$ connects directly to {{< knowl id="absolute-value-preserves-integrability" text="absolute value preserving integrability" >}}.
