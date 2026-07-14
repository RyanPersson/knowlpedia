---
title: "Quotient topology"
description: "The finest topology on a target set that makes a given surjection continuous."
---

Let $q:X\to Y$ be a {{< knowl id="surjective-function" section="shared-foundations" text="surjection" >}} from a {{< knowl id="topological-space" text="topological space" >}} $X$ onto a set $Y$. The **quotient topology** on $Y$ is defined by declaring a subset $U\subseteq Y$ to be open if and only if the {{< knowl id="preimage" section="shared-foundations" text="preimage" >}} $q^{-1}(U)$ is open in $X$.

With this topology, $q$ is automatically {{< knowl id="continuous-map" text="continuous" >}}, and $Y$ is called a quotient space of $X$. A common special case is when $Y=X/{\sim}$ is a {{< knowl id="quotient-set" section="shared-foundations" text="quotient set" >}} for an {{< knowl id="equivalence-relation" section="shared-foundations" text="equivalence relation" >}} $\sim$ on $X$.

**Examples:**
- If $X=[0,1]$ and one identifies $0\sim 1$, the resulting quotient space is topologically a circle.
- Collapsing a subset $A\subseteq X$ to a single point produces a quotient space used in “gluing” constructions.
- If $q$ is a homeomorphism onto its image, the quotient topology agrees with the existing topology on $Y$.
