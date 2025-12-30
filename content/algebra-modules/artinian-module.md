---
title: "Artinian module"
description: "A module satisfying the descending chain condition on submodules."
---

An $R$-module $M$ is **Artinian** if it satisfies the descending chain condition (DCC) on {{</* knowl id="submodule" text="submodules" */>}}: for every chain
\[
N_1 \supseteq N_2 \supseteq N_3 \supseteq \cdots
\]
there exists $k$ such that $N_k=N_{k+1}=\cdots$. For many classes of modules, Artinianity is equivalent to having finite length; compare {{</* knowl id="length-module" text="length" */>}}.

Artinian modules are “finite from below” in their submodule lattice and are the setting for induction on minimal submodules.

**Examples:**
- Any finite abelian group is Artinian as a $\mathbb Z$-module.
- Any finite-dimensional vector space over a field is Artinian (every descending chain of subspaces stabilizes).
- (Nonexample) $\mathbb Z$ is not Artinian: the chain $\mathbb Z \supset 2\mathbb Z \supset 4\mathbb Z \supset \cdots$ never stabilizes.
