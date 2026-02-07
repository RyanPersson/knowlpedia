---
title: "Kernel of ad and the center"
description: "The kernel of the adjoint representation ad is the center of the Lie algebra."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}. The {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} is the linear map
\[
\mathrm{ad}:\mathfrak g\to \mathfrak{gl}(\mathfrak g),\qquad \mathrm{ad}_x(y)=[x,y].
\]

**Lemma.**  
\[
\ker(\mathrm{ad}) \;=\; Z(\mathfrak g),
\]
where $Z(\mathfrak g)$ is the {{< knowl id="center-of-a-lie-algebra" text="center of the Lie algebra" >}}.

**Proof.**  
By definition, $x\in\ker(\mathrm{ad})$ iff $\mathrm{ad}_x(y)=0$ for all $y\in\mathfrak g$, i.e. $[x,y]=0$ for all $y$. This is exactly the defining condition for $x\in Z(\mathfrak g)$.

**Context.**  
This identifies the failure of $\mathrm{ad}$ to be injective with central directions and clarifies the meaning of {{< knowl id="inner-derivation" text="inner derivations" >}}: $\mathrm{ad}_x$ depends only on the class of $x$ modulo the center. At the group level, a related statement is {{< knowl id="kernel-of-ad-is-center-lemma" text="ker(Ad) equals the group center (connected case)" >}}.
