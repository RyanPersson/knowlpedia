---
title: "Discrete subgroup"
description: "A subgroup that is discrete in the manifold topology; its Lie algebra is ."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}.

A subgroup $\Gamma\le G$ is **discrete** if it is a discrete subset in the subspace topology (equivalently, every $\gamma\in\Gamma$ is isolated in $G$).

## Basic Lie-theoretic consequences
- Any discrete subgroup is automatically closed; hence by the {{< knowl id="closed-subgroup-theorem" text="Closed Subgroup Theorem" >}} it is an embedded {{< knowl id="lie-subgroup" text="Lie subgroup" >}}.
- The Lie algebra of a discrete subgroup is trivial:
  \[
  \mathrm{Lie}(\Gamma)=0,
  \]
  because there are no nontrivial smooth curves in $\Gamma$ through the identity.

If $\Gamma$ is also a {{< knowl id="normal-lie-subgroup" text="normal" >}} subgroup, then the quotient $G/\Gamma$ is a Lie group (see {{< knowl id="quotient-lie-group" text="quotient Lie group" >}}), and the projection $G\to G/\Gamma$ is a {{< knowl id="covering-lie-group" text="covering Lie group" >}} map precisely when $\Gamma$ is discrete and acts freely by left translations.

## Examples
- $\mathbb Z^n$ is a discrete subgroup of $\mathbb R^n$ (additively).
- The subgroup $\{\pm I\}$ is discrete in {{< knowl id="example-su2" text="$SU(2)$" >}} and is the kernel of the standard covering $SU(2)\to SO(3)$ (compare {{< knowl id="example-so3" text="$SO(3)$" >}}).

**Context.** Discrete subgroups appear as “global” corrections to Lie-algebraic data: different discrete central quotients of a simply connected group yield different Lie groups with the same Lie algebra.
