---
title: "First isomorphism consequence for groups"
description: "For a homomorphism f, the quotient G/ker(f) is isomorphic to im(f)"
---

**Proposition (Quotient by the kernel).**
Let $f:G\to H$ be a {{< knowl id="group-homomorphism" text="group homomorphism" >}}. Then there exists a unique group isomorphism
$$
\overline f:\; G/\ker(f)\ \longrightarrow\ \mathrm{im}(f)
$$
such that $\overline f(g\,\ker(f))=f(g)$ for all $g\in G$. In particular,
$$
G/\ker(f)\ \cong\ \mathrm{im}(f)
$$
as groups, where $G/\ker(f)$ is the {{< knowl id="quotient-group" text="quotient group" >}} and $\mathrm{im}(f)$ is a subgroup of $H$.

**Context.**
This is the standard "hands-on" form of the {{< knowl id="first-isomorphism-theorem-groups" text="first isomorphism theorem" >}}. It identifies precisely what information about $G$ is "lost" under $f$: exactly the {{< knowl id="kernel-group" text="kernel" >}}.

**Proof sketch.**
Define $\overline f(g\ker(f)):=f(g)$.
- **Well-defined:** if $g\ker(f)=g'\ker(f)$ then $g^{-1}g'\in\ker(f)$ so $f(g)=f(g')$.
- **Homomorphism:** follows from $f(gg')=f(g)f(g')$.
- **Bijective onto $\mathrm{im}(f)$:** surjectivity is by definition of image; injectivity is $\ker(\overline f)=\{\,\ker(f)\,\}$.
Thus $\overline f$ is an isomorphism.
