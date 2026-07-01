+++
id = "algebra-groups/first-isomorphism-consequence-groups"
title = "First isomorphism consequence for groups"
kind = "knowl"
summary = "For a homomorphism f, the quotient G/ker(f) is isomorphic to im(f)"
aliases = ["first-isomorphism-consequence-groups", "First isomorphism consequence for groups"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/first-isomorphism-consequence-groups.md"
+++

**Proposition (Quotient by the kernel).**
Let $f:G\to H$ be a [[algebra-groups/group-homomorphism|group homomorphism]]. Then there exists a unique group isomorphism
$$
\overline f:\; G/\ker(f)\ \longrightarrow\ \mathrm{im}(f)
$$

such that $\overline f(g\,\ker(f))=f(g)$ for all $g\in G$. In particular,
$$
G/\ker(f)\ \cong\ \mathrm{im}(f)
$$

as groups, where $G/\ker(f)$ is the [[algebra-groups/quotient-group|quotient group]] and $\mathrm{im}(f)$ is a subgroup of $H$.

**Context.**
This is the standard "hands-on" form of the [[algebra-groups/first-isomorphism-theorem-groups|first isomorphism theorem]]. It identifies precisely what information about $G$ is "lost" under $f$: exactly the [[algebra-groups/kernel-group|kernel]].
