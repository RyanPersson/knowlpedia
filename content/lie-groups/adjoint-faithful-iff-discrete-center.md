---
title: "Adjoint representation: discrete kernel iff discrete center"
description: "For connected Lie groups, ker(Ad)=Z(G), so Ad has discrete kernel exactly when the center is discrete."
---

Let $G$ be a {{< knowl id="connected-lie-group" text="connected Lie group" >}} with Lie algebra $\mathfrak{g}$, and let {{< knowl id="adjoint-action-of-a-lie-group" text="$\mathrm{Ad}$" >}} denote the adjoint representation $\mathrm{Ad}:G\to \mathrm{Aut}(\mathfrak{g})$.

**Theorem.** If $G$ is connected, then
$$
\ker(\mathrm{Ad}) = Z(G),
$$

where $Z(G)$ is the {{< knowl id="center-of-a-lie-group" text="center of $G$" >}}. In particular, $\mathrm{Ad}$ has **discrete kernel** if and only if $Z(G)$ is discrete.

This is often packaged as: the adjoint action is “almost effective” precisely when the center is discrete; compare {{< knowl id="effective-action" text="effective actions" >}} (which correspond to trivial kernel).

**Context.** The key input is that $\mathrm{Ad}(g)$ is the differential at the identity of the {{< knowl id="conjugation-action-of-a-lie-group" text="conjugation action" >}}; for connected groups, acting trivially on $\mathfrak{g}$ forces $g$ to commute with a neighborhood of the identity, hence with all of $G$. A standard formulation appears as {{< knowl id="kernel-of-ad-is-center-lemma" text="the kernel-of-Ad equals the center lemma" >}}.
