---
title: "Nielsen–Schreier Theorem"
description: "Every subgroup of a free group is free (with a rank formula in finite index)"
---

**Nielsen–Schreier Theorem.**
Let $F$ be a {{< knowl id="free-group" text="free group" >}} and let $H \le F$ be a {{< knowl id="subgroup" text="subgroup" >}}. Then $H$ is a free group.

If $F$ has finite rank $n$ and the {{< knowl id="index-of-subgroup" text="index" >}} $[F:H]$ is finite, then $H$ has finite rank and satisfies the Schreier index formula
$$
\operatorname{rank}(H) = 1 + [F:H]\,(n-1).
$$

This theorem is proved by constructing an explicit free generating set for $H$ from a transversal of cosets; {{< knowl id="schreiers-lemma" text="Schreier's lemma" >}} provides the standard generating set used in the proof. It is a foundational result in combinatorial group theory.

**Proof sketch.**
Choose a Schreier transversal $T$ for the cosets of $H$ in $F$. Schreier's method produces generators of $H$ of the form $t s (\overline{ts})^{-1}$ (with $t\in T$ and $s$ in a free generating set of $F$), and one shows these generators satisfy no relations, hence freely generate $H$.
