+++
id = "lie-groups/kernel-of-ad-small-is-center-lemma"
title = "Kernel of ad and the center"
kind = "knowl"
summary = "The kernel of the adjoint representation ad is the center of the Lie algebra."
aliases = ["kernel-of-ad-small-is-center-lemma", "Kernel of ad and the center"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/kernel-of-ad-small-is-center-lemma.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]]. The [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] is the linear map
\[
\mathrm{ad}:\mathfrak g\to \mathfrak{gl}(\mathfrak g),\qquad \mathrm{ad}_x(y)=[x,y].
\]

**Lemma.**
\[
\ker(\mathrm{ad}) \;=\; Z(\mathfrak g),
\]
where $Z(\mathfrak g)$ is the [[lie-groups/center-of-a-lie-algebra|center of the Lie algebra]].

**Proof.**
By definition, $x\in\ker(\mathrm{ad})$ iff $\mathrm{ad}_x(y)=0$ for all $y\in\mathfrak g$, i.e. $[x,y]=0$ for all $y$. This is exactly the defining condition for $x\in Z(\mathfrak g)$.

**Context.**
This identifies the failure of $\mathrm{ad}$ to be injective with central directions and clarifies the meaning of [[lie-groups/inner-derivation|inner derivations]]: $\mathrm{ad}_x$ depends only on the class of $x$ modulo the center. At the group level, a related statement is [[lie-groups/kernel-of-ad-is-center-lemma|ker(Ad) equals the group center (connected case)]].
