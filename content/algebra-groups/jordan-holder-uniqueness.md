---
title: "Jordan-Hölder Uniqueness"
description: "Any two composition series of a group have the same simple composition factors up to order."
---

**Jordan-Hölder Uniqueness**: Let $G$ be a group that admits a {{< knowl id="composition-series-group" text="composition series" >}}. Suppose
$$(1)=G_0 \triangleleft G_1 \triangleleft \cdots \triangleleft G_n = G$$
and
$$(1)=H_0 \triangleleft H_1 \triangleleft \cdots \triangleleft H_m = G$$

are composition series (so each successive {{< knowl id="quotient-group" text="quotient group" >}} $G_i/G_{i-1}$ and $H_j/H_{j-1}$ is a {{< knowl id="simple-group" text="simple group" >}}). Then:
- $n=m$ (the lengths coincide), and
- there exists a permutation $\sigma$ of $\{1,\dots,n\}$ such that
  $$G_i/G_{i-1} \cong H_{\sigma(i)}/H_{\sigma(i)-1}\quad\text{for all }i.$$

This is precisely the "uniqueness" conclusion extracted from the {{< knowl id="jordan-holder-theorem-groups" text="Jordan-Hölder theorem" >}}; a standard proof proceeds via {{< knowl id="schreier-refinement-theorem" text="Schreier refinement" >}}, showing that any two subnormal series have equivalent refinements.

**Examples:**
- In $S_3$, the chain $(1)\triangleleft A_3 \triangleleft S_3$ is a composition series; the factors are $A_3/(1)\cong C_3$ and $S_3/A_3\cong C_2$. Any other composition series of $S_3$ yields the same multiset $\{C_2,C_3\}$.
- In the cyclic group $C_{12}$, one composition series is $(1)\triangleleft C_2 \triangleleft C_4 \triangleleft C_{12}$ with factors $C_2, C_2, C_3$. Another is $(1)\triangleleft C_3 \triangleleft C_6 \triangleleft C_{12}$ with factors $C_3, C_2, C_2$. The factors match up to reordering, as the theorem predicts.
