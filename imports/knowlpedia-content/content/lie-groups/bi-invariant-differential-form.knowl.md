+++
id = "lie-groups/bi-invariant-differential-form"
title = "Bi-invariant differential form"
kind = "knowl"
summary = "A differential form on a Lie group invariant under both left and right translations."
aliases = ["bi-invariant-differential-form", "Bi-invariant differential form"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/bi-invariant-differential-form.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]]. For $g\in G$, write $L_g$ and $R_g$ for [[lie-groups/left-translation|left translation]] and [[lie-groups/right-translation|right translation]].

**Definition.** A differential $k$-form $\omega\in \Omega^k(G)$ is **bi-invariant** if
$$
L_g^*\omega=\omega \quad\text{and}\quad R_g^*\omega=\omega \qquad \text{for all } g\in G.
$$

Equivalently, $\omega$ is both [[lie-groups/left-invariant-differential-form|left-invariant]] and [[lie-groups/right-invariant-differential-form|right-invariant]].

**Characterization (connected case).** If $G$ is connected, a left-invariant form is determined by its value at the identity $e$, i.e. by an alternating multilinear map $\omega_e:\wedge^k\mathfrak{g}\to \Bbbk$. Such a form is bi-invariant if and only if $\omega_e$ is invariant under the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]]:
$$
\omega_e(\mathrm{Ad}_g X_1,\dots,\mathrm{Ad}_g X_k)=\omega_e(X_1,\dots,X_k)\quad\text{for all }g\in G.
$$

**Motivation.** Bi-invariant forms capture intrinsic geometry on $G$ compatible with both left and right symmetries. For example, a [[lie-groups/bi-invariant-metric|bi-invariant metric]] determines a bi-invariant volume form, and Ad-invariant forms on $\mathfrak{g}$ are the starting point for Chern–Weil constructions on homogeneous spaces.
