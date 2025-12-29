---
title: "A p-group has nontrivial center"
description: "A finite group of order p^n always has a center of size divisible by p"
---

**A p-group has nontrivial center**: Let $G$ be a finite {{</* knowl id="p-group" text="p-group" */>}}, i.e. $|G|=p^n$ for some prime $p$ and integer $n\ge 1$. Then the {{</* knowl id="center-of-group" text="center" */>}} $Z(G)$ is nontrivial; in fact, $|Z(G)|$ is divisible by $p$, so $|Z(G)|\ge p$.

This is a standard application of the {{</* knowl id="class-equation" text="class equation" */>}}, which decomposes $|G|$ into the size of the center plus sizes of non-central conjugacy classes.

**Proof sketch**: By the class equation,
$
|G| = |Z(G)| + \sum_i [G:C_G(x_i)],
$
where each $x_i$ represents a non-central {{</* knowl id="conjugacy-class" text="conjugacy class" */>}}, and $C_G(x_i)$ is the {{</* knowl id="centralizer" text="centralizer" */>}} of $x_i$. For $x_i\notin Z(G)$, the index $[G:C_G(x_i)]$ is a power of $p$ strictly larger than $1$, hence divisible by $p$. Since $|G|$ is divisible by $p$, it follows that $|Z(G)|$ is divisible by $p$, so $Z(G)\neq\{e\}$.
