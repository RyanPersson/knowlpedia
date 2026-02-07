---
title: "Ordered pair"
description: "A two-component object where order matters."
---

An **ordered pair** is a two-component object $(a,b)$ whose equality is componentwise:
$$
(a,b)=(c,d)\iff a=c \text{ and } b=d.
$$
In set theory one standard implementation is the **Kuratowski ordered pair**:
$$
(a,b):=\bigl\{\{a\},\{a,b\}\bigr\}.
$$

Ordered pairs are used to form the {{< knowl id="cartesian-product" text="Cartesian product" >}} and to encode {{< knowl id="relation" text="relations" >}} as sets of pairs.

**Examples:**
- $(1,2)\neq(2,1)$ because the first coordinates differ.
- If $a=b$, then $(a,a)$ is still a well-defined ordered pair (with both coordinates equal).
