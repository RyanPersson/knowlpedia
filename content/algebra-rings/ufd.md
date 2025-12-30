---
title: "Unique factorization domain"
description: "An integral domain where every element factors uniquely into irreducibles up to associates and order."
---

A **unique factorization domain (UFD)** is an {{< knowl id="integral-domain" text="integral domain" >}} $R$ such that:
1. Every nonzero nonunit element can be written as a finite product of {{< knowl id="irreducible-element" text="irreducible elements" >}}, and
2. This factorization is unique up to reordering and replacing factors by {{< knowl id="associated-elements" text="associates" >}}.

In a UFD, irreducible and {{< knowl id="prime-element" text="prime" >}} elements coincide, which makes divisibility behave like the integers. Many polynomial rings over UFDs are again UFDs, enabling “induction on variables” arguments in commutative algebra.

**Examples:**
- $\mathbb{Z}$ is a UFD.
- If $k$ is a field, then $k[x,y]$ is a UFD.
- $\mathbb{Z}[\sqrt{-5}]$ is not a UFD (e.g. $6$ has essentially different factorizations).