---
title: "Completeness Equivalences"
description: "Several standard statements that are equivalent forms of completeness of the real numbers."
---

**Completeness equivalences:** For an ordered field satisfying the {{< knowl id="field-axioms" text="field axioms" >}} and {{< knowl id="order-axioms" text="order axioms" >}}, the following statements are equivalent (each implies the others):

1. (Least upper bound property) Every nonempty {{< knowl id="bounded-above" text="bounded above" >}} subset of $\mathbb{R}$ has a {{< knowl id="supremum" text="supremum" >}} (the {{< knowl id="completeness-axiom" text="completeness axiom" >}}).
2. (Cauchy completeness) Every {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}} in $\mathbb{R}$ is a {{< knowl id="convergent-sequence" section="topology" text="convergent sequence" >}}.
3. (Monotone convergence) Every {{< knowl id="monotone-sequence" text="monotone sequence" >}} in $\mathbb{R}$ that is bounded converges (see {{< knowl id="monotone-sequence-convergence-theorem" text="monotone sequence convergence theorem" >}}).
4. (Nested intervals) If $(I_n)$ is a nested sequence of nonempty closed {{< knowl id="interval" text="intervals" >}} with lengths tending to $0$, then $\bigcap_{n=1}^\infty I_n$ consists of exactly one point.

These equivalent formulations let one choose the most convenient “completeness principle” for a given argument, depending on whether the problem is stated in terms of {{< knowl id="supremum" text="suprema" >}}, sequences, or intervals.
