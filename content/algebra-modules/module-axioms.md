---
title: "Module axioms"
description: "The axioms defining a (left) module over a unital ring."
---

The **module axioms** define a (left) {{< knowl id="module" text="module" >}} \(M\) over a {{< knowl id="unital-ring" text="unital ring" >}} \(R\) as follows. One requires:
1. \((M,+)\) is an abelian group (so \(+\) is a {{< knowl id="binary-operation" text="binary operation" >}} with associativity, commutativity, identity \(0\), and inverses).
2. A scalar multiplication map \(R\times M\to M\), \((r,m)\mapsto rm\), satisfying for all \(r,s\in R\) and \(m,n\in M\):
   - \((r+s)m = rm + sm\),
   - \(r(m+n) = rm + rn\),
   - \((rs)m = r(sm)\),
   - \(1_R m = m\).

These axioms encode “linearity” over a {{< knowl id="ring" text="ring" >}}; replacing \(R\) by a field yields the {{< knowl id="vector-space-axioms" text="vector space axioms" >}}.
