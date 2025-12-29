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

**Proof sketch.**
Check the two action axioms: $e\cdot x=ex=x$ and $(g_1g_2)\cdot x=g_1\cdot(g_2\cdot x)$ by associativity.
Transitivity: given $x,y\in G$, take $g=yx^{-1}$ so that $g\cdot x=y$.
Freeness: if $g\cdot x=x$ then $gx=x$, so multiplying by $x^{-1}$ gives $g=e$.
