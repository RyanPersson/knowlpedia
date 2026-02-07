---
title: "Horizontal lift of a curve"
description: "A curve in the total space projecting to a base curve and whose velocity is everywhere horizontal."
---

Let $\pi:E\to M$ be a surjective submersion equipped with an {{< knowl id="ehresmann-connection" text="Ehresmann connection" >}} with horizontal subspaces $H_eE\subset T_eE$.

Let $\gamma:I\to M$ be a {{< knowl id="smooth-map" text="smooth map" >}} from an interval $I\subset\mathbb R$, and fix $t_0\in I$ and $e_0\in E$ with $\pi(e_0)=\gamma(t_0)$.

**Definition.** A horizontal lift of $\gamma$ through $e_0$ is a curve $\widetilde\gamma:J\to E$ defined on an interval $J\subset I$ containing $t_0$ such that:
1. $\pi\circ \widetilde\gamma=\gamma|_J$, and
2. $\dot{\widetilde\gamma}(t)\in H_{\widetilde\gamma(t)}E$ for all $t\in J$.

Standard existence/uniqueness results for ordinary differential equations imply: given an Ehresmann connection, such a lift exists and is unique on some (possibly smaller) interval around $t_0$, and extends uniquely to a maximal interval.

Horizontal lifts are the basic input for defining {{< knowl id="parallel-transport" text="parallel transport" >}}.

## Examples
1. **Product bundle.** In $E=M\times F$ with product horizontals, the horizontal lift through $(\gamma(t_0),f_0)$ is $\widetilde\gamma(t)=(\gamma(t),f_0)$: the fiber component stays constant.
2. **Principal bundle lift.** On a principal bundle with connection, the horizontal lift of $\gamma$ starting at $p_0\in P_{\gamma(t_0)}$ is the unique path in $P$ projecting to $\gamma$ whose tangent vectors lie in the connection’s horizontal spaces.
3. **Vector bundle interpretation.** For a vector bundle with linear connection, a horizontal lift of $\gamma$ in the total space corresponds to a vector-valued curve $v(t)\in E_{\gamma(t)}$ satisfying the parallel-transport ODE along $\gamma$ (so that $v(t)$ is a parallel section along the curve).
