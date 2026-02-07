---
title: "Central Extension"
description: "An extension whose kernel lies in the center of the total group"
---

An extension
$$
1 \to A \xrightarrow{\iota} E \xrightarrow{\pi} Q \to 1
$$

is a **central extension** if $\iota(A)$ is contained in the {{< knowl id="center-of-group" text="center" >}} $Z(E)$. Equivalently, the kernel $A$ commutes with every element of $E$.

Central extensions are a special case of {{< knowl id="group-extension" text="group extensions" >}} in which the "added part" sits centrally. In particular, $A$ is necessarily {{< knowl id="abelian-group" text="abelian" >}}, since every subgroup of the center is abelian.

**Examples:**
- The quaternion group fits into a central extension $1\to \{\pm 1\}\to Q_8\to Q_8/\{\pm1\}\to 1$.
- If $E$ is abelian, then every extension $1\to A\to E\to Q\to 1$ is central.
- For any group $G$, the quotient map $G\to G/Z(G)$ exhibits $G$ as a central extension of $G/Z(G)$ by $Z(G)$.
