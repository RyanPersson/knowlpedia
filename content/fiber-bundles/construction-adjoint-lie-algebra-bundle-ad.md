---
title: "Adjoint Lie algebra bundle ad(P)"
description: "The Lie algebra bundle associated to a principal G-bundle via the adjoint representation on the Lie algebra."
tags: ["needs-review"]
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} with Lie algebra {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak g$. Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. The adjoint representation $\mathrm{Ad}:G\to \mathrm{Aut}(\mathfrak g)$ gives a left action of $G$ on $\mathfrak g$ by $g\cdot X := \mathrm{Ad}(g)X$.

**Construction (adjoint Lie algebra bundle).** Define
\[
\mathrm{ad}(P) := P\times_G \mathfrak g.
\]
This is a smooth vector bundle over $M$. Moreover, each fiber $\mathrm{ad}(P)_x$ carries a Lie bracket induced from the {{< knowl id="lie-bracket" text="Lie bracket" >}} on $\mathfrak g$:
\[
[p,X]\ \text{ and }\ [p,Y] \ \mapsto\ [p,[X,Y]].
\]
This is well-defined because $\mathrm{Ad}(g)$ is a Lie algebra automorphism.

Local sections $s:U\to P$ identify $\mathrm{ad}(P)|_U$ with $U\times \mathfrak g$; changes of section act by $\mathrm{Ad}$.

## Examples
1. If $P$ is trivial, then $\mathrm{ad}(P)\cong M\times \mathfrak g$ as a Lie algebra bundle.
2. If $G$ is abelian, then $\mathrm{Ad}$ is trivial and $\mathrm{ad}(P)\cong M\times \mathfrak g$ for every principal $G$-bundle.
3. For a principal $\mathrm{SO}(n)$-bundle, $\mathrm{ad}(P)$ is the bundle of skew-symmetric endomorphisms (locally identified with $\mathfrak{so}(n)$) transforming by conjugation under change of orthonormal frame.
