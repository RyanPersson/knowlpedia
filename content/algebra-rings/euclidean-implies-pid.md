---
title: "Euclidean domain ⇒ PID"
description: "Every Euclidean domain has all ideals principal."
---

**Euclidean domain ⇒ PID**: If \(R\) is a {{< knowl id="euclidean-domain" text="Euclidean domain" >}}, then \(R\) is a {{< knowl id="pid" text="principal ideal domain" >}}: every {{< knowl id="ideal" text="ideal" >}} of \(R\) is a {{< knowl id="principal-ideal" text="principal ideal" >}}.

**Proof sketch**: Let \(I\neq (0)\) be an ideal and choose \(a\in I\) of minimal Euclidean norm. For any \(b\in I\), divide \(b=qa+r\) with either \(r=0\) or \(\delta(r)<\delta(a)\). Since \(r=b-qa\in I\), minimality forces \(r=0\), hence \(b\in (a)\). Therefore \(I=(a)\). The argument uses the division property encoded by the {{< knowl id="euclidean-algorithm" text="Euclidean algorithm" >}}.