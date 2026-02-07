---
title: "Artinian ring"
description: "A ring in which descending chains of ideals stabilize."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}.

$R$ is **Artinian** if it satisfies the *descending chain condition* (DCC) on ideals: for every chain
\[
I_1 \supseteq I_2 \supseteq I_3 \supseteq \cdots
\]
there exists $N$ such that $I_n=I_N$ for all $n\ge N$.

Equivalently, every nonempty set of ideals of $R$ has a minimal element under inclusion.

## Key consequences in the commutative case
- Every commutative Artinian ring is {{< knowl id="noetherian-ring" text="Noetherian" >}}. In particular, many finiteness tools become available automatically.
- A commutative Artinian ring has {{< knowl id="krull-dimension" text="Krull dimension" >}} $0$: every prime ideal is maximal. In terms of spectra, $\operatorname{Spec}(R)$ is a finite discrete space and coincides with the {{< knowl id="maximal-spectrum" text="maximal spectrum" >}}.
- The Jacobson radical (the {{< knowl id="jacobson-radical-intersection-maximals" text="intersection of maximal ideals" >}}) is nilpotent, and $R$ decomposes as a finite product of Artinian local rings; this is closely related to the {{< knowl id="chinese-remainder-theorem" section="algebra-rings" text="Chinese remainder theorem" >}}.

## Examples
1. **Fields.**  
   Any {{< knowl id="field" section="algebra-rings" text="field" >}} is Artinian: its only ideals are $(0)$ and $(1)$.

2. **Finite quotients of $\mathbb{Z}$.**  
   $\mathbb{Z}/n\mathbb{Z}$ is Artinian (it is finite, so it has only finitely many ideals). For instance, $\mathbb{Z}/12\mathbb{Z}$ is Artinian.

3. **Truncated polynomial rings.**  
   If $k$ is a field, then $k[x]/(x^n)$ is Artinian: the ideals are $(0)\subset (x^{n-1})\subset \cdots \subset (x)\subset (1)$, so every descending chain stabilizes.

(As a contrast, $k[x]$ is Noetherian but not Artinian: the descending chain $(x)\supset (x^2)\supset (x^3)\supset \cdots$ never stabilizes.)
