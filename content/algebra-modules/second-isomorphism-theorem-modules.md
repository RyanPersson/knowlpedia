---
title: "Second isomorphism theorem for modules"
description: "For submodules A,B ≤ M, one has (A+B)/B ≅ A/(A∩B)."
---

**Second isomorphism theorem (modules)**: Let \(M\) be an \(R\)-module and let \(A,B\) be {{</* knowl id="submodule" text="submodules" */>}} of \(M\). Then there is a natural isomorphism of \(R\)-modules
\[
(A+B)/B \;\cong\; A/(A\cap B),
\]
where \(A\cap B\) is the {{</* knowl id="intersection" text="intersection" */>}} and each quotient is a {{</* knowl id="quotient-module" text="quotient module" */>}}.

This isomorphism is obtained by restricting the quotient map \(M\to M/B\) to \(A\), and it is a standard application of the {{</* knowl id="first-isomorphism-theorem-modules" text="first isomorphism theorem" */>}}.

**Proof sketch**: Consider the homomorphism \(A\to (A+B)/B\) induced by inclusion \(A\hookrightarrow A+B\) followed by the quotient map. Its kernel is exactly \(A\cap B\), and its image is all of \((A+B)/B\). Apply the first isomorphism theorem.
