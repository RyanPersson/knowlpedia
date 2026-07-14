---
title: "Quotient topology"
description: "The finest topology making a given surjection continuous."
---

Let $X$ be a {{{< knowl id="topological-space" text="topological space" >}}} and let $q:X\to Y$ be a {{{< knowl id="surjective-function" section="shared-foundations" text="surjective function" >}}}. The **quotient topology** on $Y$ is defined by declaring a subset $U\subseteq Y$ to be {{{< knowl id="open-set" text="open" >}}} if and only if the {{{< knowl id="preimage" section="shared-foundations" text="preimage" >}}} $q^{-1}(U)$ is open in $X$.

With this topology, $q$ is automatically a {{{< knowl id="continuous-map" text="continuous map" >}}}; a surjection equipped with this property is often called a *quotient map*. A common source of quotient topologies is an {{{< knowl id="equivalence-relation" section="shared-foundations" text="equivalence relation" >}}} $\sim$ on $X$, where $Y$ is the {{{< knowl id="quotient-set" section="shared-foundations" text="quotient set" >}}} $X/{\sim}$ and $q$ is the canonical projection.
