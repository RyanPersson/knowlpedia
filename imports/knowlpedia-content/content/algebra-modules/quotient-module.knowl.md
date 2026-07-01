+++
id = "algebra-modules/quotient-module"
title = "Quotient module"
kind = "knowl"
summary = "The module obtained by collapsing a submodule to zero."
aliases = ["quotient-module", "Quotient module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/quotient-module.md"
+++

Let $M$ be a left $R$-module and let $N\le M$ be a [[algebra-modules/submodule|submodule]]. Define an [[shared-foundations/equivalence-relation|equivalence relation]] on $M$ by $m\sim m'$ iff $m-m'\in N$. The **quotient module** $M/N$ is the [[shared-foundations/quotient-set|quotient set]] of equivalence classes, written $m+N$, with operations
\[
(m+N)+(m'+N)=(m+m')+N,\qquad r(m+N)=(rm)+N.
\]
These operations are well-defined precisely because $N$ is closed under subtraction and scalar multiplication.

The construction is characterized by the [[algebra-modules/quotient-module-universal-property|universal property of the quotient module]]: maps out of $M$ that kill $N$ factor uniquely through $M/N$.

**Examples:**
- For $M=\mathbb Z^2$ and $N=2\mathbb Z^2$, the quotient $M/N$ has four elements and is isomorphic (as a $\mathbb Z$-module) to $(\mathbb Z/2\mathbb Z)^2$.
- For a ring $R$ and ideal $I\lhd R$, the quotient $R/I$ is a quotient module of the left $R$-module $R$.
- (Edge case) If $N=M$, then $M/N$ is the zero module; if $N=0$, then $M/N\cong M$.
