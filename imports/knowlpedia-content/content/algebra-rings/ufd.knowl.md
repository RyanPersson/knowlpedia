+++
id = "algebra-rings/ufd"
title = "Unique factorization domain"
kind = "knowl"
summary = "An integral domain where every element factors uniquely into irreducibles up to associates and order."
aliases = ["ufd", "Unique factorization domain"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ufd.md"
+++

A **unique factorization domain (UFD)** is an [[algebra-rings/integral-domain|integral domain]] $R$ such that:
1. Every nonzero nonunit element can be written as a finite product of [[algebra-rings/irreducible-element|irreducible elements]], and
2. This factorization is unique up to reordering and replacing factors by [[algebra-rings/associated-elements|associates]].

In a UFD, irreducible and [[algebra-rings/prime-element|prime]] elements coincide, which makes divisibility behave like the integers. Many polynomial rings over UFDs are again UFDs, enabling “induction on variables” arguments in commutative algebra.

**Examples:**
- $\mathbb{Z}$ is a UFD.
- If $k$ is a field, then $k[x,y]$ is a UFD.
- $\mathbb{Z}[\sqrt{-5}]$ is not a UFD (e.g. $6$ has essentially different factorizations).
