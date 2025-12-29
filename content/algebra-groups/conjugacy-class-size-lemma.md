---
title: "Conjugacy Class Size Lemma"
description: "The size of a conjugacy class equals the index of the centralizer"
---

**Conjugacy Class Size Lemma**: Let $G$ be a finite {{< knowl id="group" text="group" >}} and let $g\in G$. Let $\mathrm{Cl}(g)$ denote the {{< knowl id="conjugacy-class" text="conjugacy class" >}} of $g$, and let $C_G(g)$ denote the {{< knowl id="centralizer" text="centralizer" >}} of $g$. Then
$
|\mathrm{Cl}(g)| = [G : C_G(g)],
$
where $[G:C_G(g)]$ is the {{< knowl id="index-of-subgroup" text="index" >}} of $C_G(g)$ in $G$.

This is an instance of the {{< knowl id="orbit-stabilizer-theorem" text="orbit–stabilizer theorem" >}} applied to the {{< knowl id="conjugation-action" text="conjugation action" >}} of $G$ on itself.

**Proof sketch**: Under conjugation, the orbit of $g$ is $\mathrm{Cl}(g)$. The stabilizer of $g$ is $\{x\in G : xgx^{-1}=g\}=C_G(g)$. Orbit–stabilizer gives $|\mathrm{Cl}(g)|=[G:C_G(g)]$.
