+++
id = "algebra-rings/regular-element"
title = "Regular element"
kind = "knowl"
summary = "An element that is not a zero divisor (equivalently, multiplication by it is injective)."
aliases = ["regular-element", "Regular element"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/regular-element.md"
+++

Let $R$ be a ring. An element $a\in R$ is **left regular** if $ax=ay$ implies $x=y$ for all $x,y\in R$, and **right regular** if $xa=ya$ implies $x=y$ for all $x,y\in R$. It is **regular** if it is both left and right regular. In a commutative ring, this is equivalent to saying $a$ is not a [[algebra-rings/zero-divisor|zero divisor]], i.e. $ax=0$ implies $x=0$.

Regular elements are precisely those with trivial [[algebra-rings/annihilator-ideal|annihilator]] (in the commutative case), and they are the multiplicative set used to form total rings of fractions and localizations.

**Examples:**
- In $\mathbb Z$, every nonzero integer is regular.
- In $\mathbb Z/6\mathbb Z$, the class of $5$ is regular, while the class of $2$ is not.
- In $k[x,y]/(xy)$, the class of $x$ is not regular.
