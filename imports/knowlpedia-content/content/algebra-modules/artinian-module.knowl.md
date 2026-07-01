+++
id = "algebra-modules/artinian-module"
title = "Artinian module"
kind = "knowl"
summary = "A module satisfying the descending chain condition on submodules."
aliases = ["artinian-module", "Artinian module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/artinian-module.md"
+++

An $R$-[[algebra-modules/module|module]] $M$ is **Artinian** if it satisfies the descending chain condition (DCC) on [[algebra-modules/submodule|submodules]]: for every chain
\[
N_1 \supseteq N_2 \supseteq N_3 \supseteq \cdots
\]
there exists $k$ such that $N_k=N_{k+1}=\cdots$. For many classes of modules, Artinianity is equivalent to having finite length; compare [[algebra-modules/length-module|length]].

Artinian modules are “finite from below” in their submodule lattice and are the setting for induction on minimal submodules.

**Examples:**
- Any finite abelian group is Artinian as a $\mathbb Z$-module.
- Any finite-dimensional vector space over a field is Artinian (every descending chain of subspaces stabilizes).
- (Nonexample) $\mathbb Z$ is not Artinian: the chain $\mathbb Z \supset 2\mathbb Z \supset 4\mathbb Z \supset \cdots$ never stabilizes.
