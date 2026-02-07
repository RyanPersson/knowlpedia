---
title: "Smith normal form invariants"
description: "The Smith normal form diagonal entries are canonical invariants and control the cokernel module."
---

**Smith normal form invariants**: Let $R$ be a PID and let $A\in M_{m\times n}(R)$. Suppose $A$ has Smith normal form $\operatorname{diag}(d_1,\dots,d_r,0,\dots,0)$ with $d_1\mid d_2\mid\cdots\mid d_r$. Then the elements $d_i$ are uniquely determined by $A$ up to multiplication by a unit of $R$, and they determine the isomorphism class of the cokernel module
\[
\operatorname{coker}(A)\cong R^m/\operatorname{im}(A)\cong \bigoplus_{i=1}^r R/(d_i)\;\oplus\;R^{\,m-r}.
\]

The uniqueness part comes from the {{< knowl id="smith-normal-form-theorem" text="Smith normal form theorem" >}}, and the decomposition agrees with the invariant factors in the {{< knowl id="structure-theorem-pid" text="structure theorem over a PID" >}}, computing {{< knowl id="cokernel-module" text="cokernels" >}} over a {{< knowl id="pid" section="algebra-rings" text="PID" >}}.
