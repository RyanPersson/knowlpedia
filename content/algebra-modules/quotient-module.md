---
title: "Quotient module"
description: "The module obtained by collapsing a submodule to zero."
---

Let $M$ be a left $R$-module and let $N\le M$ be a {{< knowl id="submodule" text="submodule" >}}. Define an {{< knowl id="equivalence-relation" text="equivalence relation" >}} on $M$ by $m\sim m'$ iff $m-m'\in N$. The **quotient module** $M/N$ is the {{< knowl id="quotient-set" text="quotient set" >}} of equivalence classes, written $m+N$, with operations
\[
(m+N)+(m'+N)=(m+m')+N,\qquad r(m+N)=(rm)+N.
\]
These operations are well-defined precisely because $N$ is closed under subtraction and scalar multiplication.

The construction is characterized by the {{< knowl id="quotient-module-universal-property" text="universal property of the quotient module" >}}: maps out of $M$ that kill $N$ factor uniquely through $M/N$.

**Examples:**
- For $M=\mathbb Z^2$ and $N=2\mathbb Z^2$, the quotient $M/N$ has four elements and is isomorphic (as a $\mathbb Z$-module) to $(\mathbb Z/2\mathbb Z)^2$.
- For a ring $R$ and ideal $I\lhd R$, the quotient $R/I$ is a quotient module of the left $R$-module $R$.
- (Edge case) If $N=M$, then $M/N$ is the zero module; if $N=0$, then $M/N\cong M$.
