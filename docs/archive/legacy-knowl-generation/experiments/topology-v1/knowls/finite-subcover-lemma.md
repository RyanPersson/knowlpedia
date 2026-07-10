---
title: "Finite subcover lemma"
description: "A compact set admits a finite subcollection from any open cover"
---

**Finite subcover lemma**: Let $K$ be a {{< knowl id="compact-set" text="compact set" >}} in a topological space, and let $\mathcal{U}$ be an {{< knowl id="open-cover" text="open cover" >}} of $K$. Then there exist $U_1,\dots,U_n \in \mathcal{U}$ such that
$$
K \subseteq U_1 \cup \cdots \cup U_n.
$$

This is the “usable form” of compactness: most arguments with compact sets proceed by writing down an open cover and extracting a finite subcover.

**Examples:**
- The family $\{(-1/n,\,1+1/n)\}_{n\in\mathbb{N}}$ is an open cover of $[0,1]\subset\mathbb{R}$, and the single set $(-1,2)$ already covers $[0,1]$.
- In contrast, the open cover $\{(n-1,\,n+1)\}_{n\in\mathbb{Z}}$ of $\mathbb{R}$ has no finite subcover.
