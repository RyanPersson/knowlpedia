---
title: "Inverse function theorem in R^k"
description: "A map with invertible derivative at a point has a differentiable local inverse."
---

**Inverse function theorem in $\mathbb R^k$:** Let $U\subseteq\mathbb R^k$ be an {{< knowl id="open-set" section="topology" text="open set" >}} and let $f:U\to\mathbb R^k$ be continuously differentiable. If the {{< knowl id="jacobian-determinant" text="Jacobian determinant" >}} $\det Df(a)$ is nonzero at some $a\in U$, then there exist neighborhoods $A$ of $a$ and $B$ of $f(a)$ such that $f$ restricts to a bijection $f:A\to B$ whose inverse $f^{-1}:B\to A$ is continuously differentiable. Moreover,
$$
D(f^{-1})(f(a))=(Df(a))^{-1}.
$$

Thus, near $a$, the map $f$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" section="fiber-bundles">}} onto its image; in particular it is a local {{< knowl id="homeomorphism" section="topology" text="homeomorphism" >}}.
