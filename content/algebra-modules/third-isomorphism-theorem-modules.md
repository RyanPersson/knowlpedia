---
title: "Third isomorphism theorem for modules"
description: "If A ⊆ B ⊆ M then (M/A)/(B/A) ≅ M/B."
---

**Third isomorphism theorem (modules)**: Let \(M\) be an \(R\)-module and let \(A\subseteq B\subseteq M\) be {{< knowl id="submodule" text="submodules" >}}. Then there is a natural isomorphism
\[
(M/A)/(B/A) \;\cong\; M/B
\]
of \(R\)-modules, where each quotient is a {{< knowl id="quotient-module" text="quotient module" >}}.

This theorem expresses the compatibility of iterated quotients and is fundamental in organizing “modding out step by step” in module theory.

**Proof sketch** *(optional)*: Use the natural surjection \(M/A\to M/B\) induced from \(M\to M/B\); its kernel is \(B/A\). Apply the first isomorphism theorem to that map.
