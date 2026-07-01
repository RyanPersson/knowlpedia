+++
id = "fiber-bundles/proper-action"
title = "Proper action"
kind = "knowl"
summary = "A Lie group action for which the action graph map is a proper map."
aliases = ["proper-action", "Proper action"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/proper-action.md"
+++

Let [[fiber-bundles/lie-group|Lie group]] $G$ act on a [[fiber-bundles/smooth-manifold|smooth manifold]] $M$ via a smooth action.

The action is **proper** if the map
\[
\Theta: G\times M \longrightarrow M\times M,\qquad \Theta(g,x)=(g\cdot x,\ x)
\]
is a proper map (that is, the preimage of every compact subset of $M\times M$ is compact in $G\times M$).

Properness is a topological finiteness condition on how group elements can move points around. In particular, for a proper action the orbit space [[fiber-bundles/quotient-space-of-an-action|quotient space]] $M/G$ is Hausdorff, and all stabilizers are compact.

## Examples
1. **Compact groups act properly.** If $G$ is compact, then any continuous (hence any smooth) action of $G$ on a Hausdorff space is proper.
2. **Translations are proper.** The translation action of $\mathbb{R}^n$ on $\mathbb{R}^n$, $a\cdot x=x+a$, is proper.
3. **Non-example (periodic stabilizer).** The action of $\mathbb{R}$ on $S^1$ by rotations $t\cdot e^{i\theta}=e^{i(\theta+t)}$ is not proper: the preimage of the diagonal $\{(x,x)\}$ contains $(2\pi\mathbb{Z})\times S^1$, which is not compact.
