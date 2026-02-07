---
title: "Inner derivation"
description: "A derivation of the form ad_x(y) = [x,y]."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}. Recall that a {{< knowl id="derivation-lie-algebra" text="derivation" >}} is a linear map $D:\mathfrak g\to\mathfrak g$ satisfying the Leibniz rule
\[
D([x,y])=[D(x),y]+[x,D(y)].
\]

**Definition (Inner derivation).**  
For each $x\in\mathfrak g$, the map
\[
\mathrm{ad}_x:\mathfrak g\to\mathfrak g,\qquad \mathrm{ad}_x(y)=[x,y]
\]
is a derivation. A derivation is called **inner** if it equals $\mathrm{ad}_x$ for some $x\in\mathfrak g$.

The assignment $x\mapsto \mathrm{ad}_x$ is the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} $\mathrm{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g)$, and the space of inner derivations is $\mathrm{ad}(\mathfrak g)\subseteq \mathrm{Der}(\mathfrak g)$.

**Key relation to the center.**  
The kernel of $\mathrm{ad}$ is exactly the {{< knowl id="center-of-a-lie-algebra" text="center" >}} (see {{< knowl id="kernel-of-ad-small-is-center-lemma" text="the kernel-of-ad lemma" >}}), so inner derivations detect noncentral directions.

**Context.**  
Derivations modulo inner derivations measure “outer” symmetries of $\mathfrak g$ (compare {{< knowl id="outer-derivation" text="outer derivations" >}}), and exponentiating $\mathrm{ad}_x$ is the infinitesimal source of many {{< knowl id="lie-algebra-automorphism" text="automorphisms" >}}.
