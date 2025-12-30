---
title: "Universal property of quotient rings"
description: "A homomorphism that kills an ideal factors uniquely through the quotient."
---

**Universal property of quotient rings**: Let \(R\) be a ring, let \(I\triangleleft R\) be an {{< knowl id="ideal" text="ideal" >}}, and let \(\pi:R\to R/I\) be the canonical projection onto the {{< knowl id="quotient-ring" text="quotient ring" >}}. For any {{< knowl id="ring-homomorphism" text="ring homomorphism" >}} \(f:R\to S\) such that \(I\subseteq \ker(f)\) (where \(\ker(f)\) is the {{< knowl id="kernel-ring" text="kernel" >}}), there exists a unique ring homomorphism \(\bar f:R/I\to S\) with
\[
f=\bar f\circ \pi.
\]

This property characterizes \(R/I\) up to unique isomorphism and is the categorical mechanism behind “imposing relations” by quotienting.