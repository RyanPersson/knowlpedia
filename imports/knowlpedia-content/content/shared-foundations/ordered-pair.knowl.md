+++
id = "shared-foundations/ordered-pair"
title = "Ordered pair"
kind = "knowl"
summary = "A two-component object where order matters."
aliases = ["ordered-pair", "Ordered pair"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/ordered-pair.md"
+++

An **ordered pair** is a two-component object $(a,b)$ whose equality is componentwise:
$$
(a,b)=(c,d)\iff a=c \text{ and } b=d.
$$
In set theory one standard implementation is the **Kuratowski ordered pair**:
$$
(a,b):=\bigl\{\{a\},\{a,b\}\bigr\}.
$$

Ordered pairs are used to form the [[shared-foundations/cartesian-product|Cartesian product]] and to encode [[shared-foundations/relation|relations]] as sets of pairs.

**Examples:**
- $(1,2)\neq(2,1)$ because the first coordinates differ.
- If $a=b$, then $(a,a)$ is still a well-defined ordered pair (with both coordinates equal).
