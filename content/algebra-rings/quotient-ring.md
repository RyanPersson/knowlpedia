---
title: "Quotient ring"
description: "A ring formed from a ring by identifying elements that differ by a two-sided ideal."
---

Let $R$ be a ring and let $I$ be a {{< knowl id="two-sided-ideal" text="two-sided ideal" >}} of $R$. The **quotient ring** $R/I$ is the {{< knowl id="quotient-set" text="quotient set" >}} of $R$ by the {{< knowl id="equivalence-relation" text="equivalence relation" >}} $r\sim s$ iff $r-s\in I$, with addition and multiplication on {{< knowl id="coset" text="cosets" >}} defined by
\[
(r+I)+(s+I)=(r+s)+I,\qquad (r+I)(s+I)=(rs)+I.
\]
The two-sided condition ensures multiplication is well-defined.

The canonical projection $\pi:R\to R/I$ is a surjective ring homomorphism with kernel $I, and $R/I$ satisfies the {{< knowl id="quotient-ring-universal-property" text="universal property of quotients" >}}.

**Examples:**
- $\mathbb Z/(n)$ is the familiar ring $\mathbb Z/n\mathbb Z$.
- For a field $k$, the quotient $k[x]/(x^2)$ is a ring in which the class of $x$ is nilpotent.
- If $I=R$, then $R/I$ is the zero ring; if $I=\{0\}$, then $R/I\cong R$.