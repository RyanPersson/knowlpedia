---
title: "Bi-invariant differential form"
description: "A differential form on a Lie group invariant under both left and right translations."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. For $g\in G$, write $L_g$ and $R_g$ for {{< knowl id="left-translation" text="left translation" >}} and {{< knowl id="right-translation" text="right translation" >}}.

**Definition.** A differential $k$-form $\omega\in \Omega^k(G)$ is **bi-invariant** if
$$
L_g^*\omega=\omega \quad\text{and}\quad R_g^*\omega=\omega \qquad \text{for all } g\in G.
$$

Equivalently, $\omega$ is both {{< knowl id="left-invariant-differential-form" text="left-invariant" >}} and {{< knowl id="right-invariant-differential-form" text="right-invariant" >}}.

**Characterization (connected case).** If $G$ is connected, a left-invariant form is determined by its value at the identity $e$, i.e. by an alternating multilinear map $\omega_e:\wedge^k\mathfrak{g}\to \Bbbk$. Such a form is bi-invariant if and only if $\omega_e$ is invariant under the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" >}}:
$$
\omega_e(\mathrm{Ad}_g X_1,\dots,\mathrm{Ad}_g X_k)=\omega_e(X_1,\dots,X_k)\quad\text{for all }g\in G.
$$

**Motivation.** Bi-invariant forms capture intrinsic geometry on $G$ compatible with both left and right symmetries. For example, a {{< knowl id="bi-invariant-metric" text="bi-invariant metric" >}} determines a bi-invariant volume form, and Ad-invariant forms on $\mathfrak{g}$ are the starting point for Chern–Weil constructions on homogeneous spaces.
