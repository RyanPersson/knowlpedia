+++
id = "algebra-rings/ring"
title = "Ring"
kind = "knowl"
summary = "A set with addition forming an abelian group and multiplication that is associative and distributive over addition."
aliases = ["ring"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ring.md"
+++

A **ring** is a set $R$ equipped with two [[shared-foundations/binary-operation|binary operations]] $+$ and $\cdot$ such that:
1. $(R,+)$ is an [[algebra-groups/abelian-group|abelian group]] (in particular, there is an additive identity $0$ and every element has an additive inverse),
2. multiplication is associative: $(ab)c=a(bc)$ for all $a,b,c\in R$,
3. multiplication distributes over addition: $a(b+c)=ab+ac$ and $(a+b)c=ac+bc$ for all $a,b,c\in R$.

These conditions are often summarized as the [[algebra-rings/ring-axioms|ring axioms]]. Many texts additionally impose a multiplicative identity, leading to a [[algebra-rings/unital-ring|unital ring]]; commutativity of multiplication leads to a [[algebra-rings/commutative-ring|commutative ring]].

**Examples:**
- $\mathbb Z$ with usual $+$ and $\cdot$ is a (unital, commutative) ring.
- $M_n(\mathbb Z)$ is a ring under matrix addition and multiplication, typically noncommutative for $n\ge 2$.
- The even integers $2\mathbb Z$ form a ring (under inherited operations) but are not unital.
