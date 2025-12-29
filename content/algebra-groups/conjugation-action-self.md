---
title: "Conjugation action on itself"
description: "A group acts on itself by conjugation g·x = gxg^{-1}"
---

**Proposition (Conjugation action).**
Let $G$ be a {{< knowl id="group" text="group" >}}. Define a map $G\times G\to G$ by
$$
g\cdot x := gxg^{-1}.
$$
Then this defines a {{< knowl id="group-action" text="group action" >}} of $G$ on itself, called the {{< knowl id="conjugation-action" text="conjugation action" >}}.

**Context.**
The orbits of this action are the {{< knowl id="conjugacy-class" text="conjugacy classes" >}} in $G$, and stabilizers are centralizers. This action is the mechanism behind the class equation and many counting arguments.

**Proof sketch.**
Identity: $e\cdot x=exe^{-1}=x$. Compatibility:
$$
(g_1g_2)\cdot x = g_1(g_2xg_2^{-1})g_1^{-1} = g_1\cdot(g_2\cdot x).
$$
