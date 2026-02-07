---
title: "Ring"
description: "A set with addition forming an abelian group and multiplication that is associative and distributive over addition."
---

A **ring** is a set $R$ equipped with two {{< knowl id="binary-operation" section="shared-foundations" text="binary operations" >}} $+$ and $\cdot$ such that:
1. $(R,+)$ is an {{< knowl id="abelian-group" section="algebra-groups" text="abelian group" >}} (in particular, there is an additive identity $0$ and every element has an additive inverse),
2. multiplication is associative: $(ab)c=a(bc)$ for all $a,b,c\in R$,
3. multiplication distributes over addition: $a(b+c)=ab+ac$ and $(a+b)c=ac+bc$ for all $a,b,c\in R$.

These conditions are often summarized as the {{< knowl id="ring-axioms" text="ring axioms" >}}. Many texts additionally impose a multiplicative identity, leading to a {{< knowl id="unital-ring" text="unital ring" >}}; commutativity of multiplication leads to a {{< knowl id="commutative-ring" text="commutative ring" >}}.

**Examples:**
- $\mathbb Z$ with usual $+$ and $\cdot$ is a (unital, commutative) ring.
- $M_n(\mathbb Z)$ is a ring under matrix addition and multiplication, typically noncommutative for $n\ge 2$.
- The even integers $2\mathbb Z$ form a ring (under inherited operations) but are not unital.