---
title: "Structure theorem for finitely generated modules over a PID"
description: "A finitely generated module over a PID splits as a free part plus cyclic torsion factors."
---

**Structure theorem (f.g. modules over a PID)**: Let \(R\) be a {{< knowl id="pid" section="algebra-rings" text="principal ideal domain" >}} and let \(M\) be a {{< knowl id="finitely-generated-module" text="finitely generated module" >}} over \(R\). Then there exist an integer \(r\ge 0\) and nonzero elements \(d_1,\dots,d_t\in R\) with \(d_1\mid d_2\mid \cdots \mid d_t\) such that
\[
M \;\cong\; R^{\,r}\;\oplus\;\bigoplus_{i=1}^t R/(d_i),
\]
a decomposition as a {{< knowl id="direct-sum-modules" text="direct sum" >}} of a free part and cyclic torsion factors. The integer \(r\) and the invariant factors \(d_i\) are unique up to multiplication by units in \(R\). In particular, the torsion submodule of \(M\) is a {{< knowl id="torsion-module" text="torsion module" >}} and the free summand is a {{< knowl id="free-module" text="free module" >}} of rank \(r\).

This theorem is the module-theoretic engine behind the classification of finitely generated abelian groups (the case \(R=\mathbb Z\)); see {{< knowl id="classification-fg-abelian-groups" text="classification of finitely generated abelian groups" >}}. It is closely tied to {{< knowl id="smith-normal-form-theorem" text="Smith normal form" >}}, and it admits an equivalent primary decomposition form (see the {{< knowl id="elementary-divisor-theorem" text="elementary divisor theorem" >}}).
