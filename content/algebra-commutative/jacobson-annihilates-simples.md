---
title: "Jacobson radical annihilates simple modules"
description: "Every element of the Jacobson radical acts as zero on any simple module."
---

The Jacobson radical can be defined and studied through its action on modules. One of its basic properties is that it kills every simple module, making it invisible in the semisimple world. In the commutative setting, this is closely tied to {{< knowl id="jacobson-radical-intersection-maximals" text="the description of the Jacobson radical as an intersection of maximal ideals" >}}.

## Theorem

Let $R$ be a ring (commutative or not), and let $J(R)$ denote its Jacobson radical. Then for every simple (right) $R$-module $S$,
\[
J(R)\cdot S = 0.
\]

Equivalently,
\[
J(R)\subseteq \operatorname{Ann}_R(S)
\]
for every simple module $S$, where {{< knowl id="annihilator-module" section="algebra-modules" text="the annihilator" >}} is the ideal of ring elements acting as $0$ on $S$.

In particular, if $R$ is commutative, every simple $R$-module is of the form $R/\mathfrak m$ for some maximal ideal $\mathfrak m$, and the theorem specializes to the inclusion
\[
J(R)\subseteq \mathfrak m
\quad\text{for all maximal ideals }\mathfrak m,
\]
which is exactly the statement that $J(R)$ equals the intersection of maximal ideals from {{< knowl id="jacobson-radical-intersection-maximals" text="the commutative characterization" >}}.

## Examples

1. **Local rings.**  
   If $(R,\mathfrak m)$ is a {{< knowl id="local-ring" text="local ring" >}}, then $J(R)=\mathfrak m$. The unique simple $R$-module is the {{< knowl id="residue-field" text="residue field $R/\mathfrak m$" >}}, and $\mathfrak m$ acts by $0$ on it by definition. Hence $J(R)$ annihilates the simple module.

2. **The integers.**  
   In $R=\mathbb Z$, $J(\mathbb Z)=0$ (see {{< knowl id="jacobson-radical-intersection-maximals" text="intersection of maximal ideals in $\mathbb Z$" >}}). The simple $\mathbb Z$-modules are $\mathbb Z/p\mathbb Z$, and indeed $0$ acts as $0$ on every module.

3. **Dual numbers.**  
   Let $R=k[\varepsilon]/(\varepsilon^2)$. Then $J(R)=(\bar\varepsilon)$, and the unique simple module is $R/(\bar\varepsilon)\cong k$. The element $\bar\varepsilon$ acts as $0$ on $k$, so $J(R)\cdot k=0$.

This principle is one of the standard bridges between ring structure and module structure; it is also a key input in the Artin–Wedderburn picture of semisimple rings, where the Jacobson radical vanishes.
