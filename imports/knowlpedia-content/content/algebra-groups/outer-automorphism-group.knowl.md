+++
id = "algebra-groups/outer-automorphism-group"
title = "Outer Automorphism Group"
kind = "knowl"
summary = "Automorphisms modulo inner automorphisms"
aliases = ["outer-automorphism-group", "Outer Automorphism Group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/outer-automorphism-group.md"
+++

For a group $G$, the **outer automorphism group** is the quotient
$$
\operatorname{Out}(G) := \operatorname{Aut}(G)\big/\operatorname{Inn}(G),
$$

where $\operatorname{Aut}(G)$ is the [[algebra-groups/automorphism-group|automorphism group]] and $\operatorname{Inn}(G)$ is the subgroup of [[algebra-groups/inner-automorphism|inner automorphisms]]. This is a [[algebra-groups/quotient-group|quotient group]], and it measures the "new" automorphisms not coming from conjugation.

Saying $\operatorname{Out}(G)$ is trivial means every automorphism of $G$ is inner.

**Examples:**
- If $G$ is abelian, then $\operatorname{Inn}(G)$ is trivial, so $\operatorname{Out}(G)=\operatorname{Aut}(G)$.
- If $\operatorname{Aut}(G)=\operatorname{Inn}(G)$, then $\operatorname{Out}(G)$ is the trivial group.
- For many groups, $\operatorname{Out}(G)$ is small even when $\operatorname{Aut}(G)$ is large, reflecting that "most" automorphisms are induced by conjugation.
