+++
id = "algebra-modules/submodule"
title = "Submodule"
kind = "knowl"
summary = "An additive subgroup closed under the scalar action of a module."
aliases = ["submodule"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/submodule.md"
+++

Let $M$ be a left $R$-[[algebra-modules/module|module]]. A **submodule** of $M$ is a [[shared-foundations/subset|subset]] $N\subseteq M$ such that:
1. $0\in N$,
2. $n_1,n_2\in N \Rightarrow n_1-n_2\in N$,
3. $r\in R$ and $n\in N \Rightarrow rn\in N$.

Equivalently, $N$ is an additive subgroup of $(M,+)$ that is stable under scalar multiplication. Practical closure tests are summarized in the [[algebra-modules/submodule-criterion|submodule criterion]].

**Examples:**
- In the $\mathbb Z$-module $M=\mathbb Z^2$, the set $N=\{(2a,2b):a,b\in\mathbb Z\}$ is a submodule.
- If $R$ is a ring, any [[algebra-rings/ideal|ideal]] $I\lhd R$ is a submodule of the left $R$-module $R$.
- (Edge case) The sets $\{0\}$ and $M$ are always submodules; a module is [[algebra-modules/simple-module|simple]] exactly when these are the only submodules.
