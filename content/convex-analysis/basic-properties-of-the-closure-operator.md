---
title: "Basic properties of closure"
description: "Monotonicity, idempotence, and compatibility with finite unions"
---

**Proposition.**
Let $(X,d)$ be a metric space and let $A,B\subset X$. Then:

1. If $A\subset B$, then $\overline{A}\subset \overline{B}$.
2. $\overline{A}=A$ if and only if $A$ is {{< knowl id="closed-subset" text="closed" >}}.
3. $\overline{\overline{A}}=\overline{A}$ (idempotence).
4. $\overline{A\cup B}=\overline{A}\cup \overline{B}$.

**Proof sketch.**
1. Any closed set containing $B$ also contains $A$, so the intersection defining $\overline{A}$ is contained in the intersection defining $\overline{B}$.
2. By definition $\overline{A}$ is closed and contains $A$; equality holds exactly when $A$ is closed.
3. $\overline{A}$ is closed, so closing it again does nothing.
4. The inclusion $\overline{A}\cup\overline{B}\subset \overline{A\cup B}$ follows from monotonicity. For the reverse inclusion, note $\overline{A}\cup\overline{B}$ is closed and contains $A\cup B$, hence contains $\overline{A\cup B}$ by minimality.
