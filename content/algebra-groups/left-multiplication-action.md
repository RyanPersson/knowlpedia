---
title: "Left multiplication action"
description: "A group acts on itself by left translation"
---

**Proposition (Left multiplication action).**
Let $G$ be a {{< knowl id="group" text="group" >}}. Define a map $G\times G\to G$ by
$$
g\cdot x := gx.
$$

Then this defines a {{< knowl id="group-action" text="group action" >}} of $G$ on the underlying set of $G$.

Moreover, this action is:
- **transitive** (there is one orbit), and
- **free** (only the identity fixes any element),

hence it is a {{< knowl id="regular-action" text="regular action" >}}, often called the **left regular action**.

**Context.**
This action is the input for {{< knowl id="cayleys-theorem" text="Cayley's theorem" >}}: it produces an injective homomorphism from $G$ into a symmetric group by viewing elements as permutations of $G$.
