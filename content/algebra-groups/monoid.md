---
title: "Monoid"
description: "A semigroup with an identity element"
---

A **monoid** is a {{< knowl id="semigroup" text="semigroup" >}} $(M,\cdot)$ together with an element $e\in M$ (called an identity element) such that for every $a\in M$,
$
e\cdot a = a \quad\text{and}\quad a\cdot e = a.
$

Monoids generalize {{< knowl id="group" text="groups" >}} by dropping the requirement that elements have inverses. Many monoids arise from {{< knowl id="composition" section="shared-foundations" text="composition" >}} of endomorphisms (self-maps).

**Examples:**
- $(\mathbb{N},+,0)$ is a monoid.
- $(\mathbb{N},\times,1)$ is a monoid.
- For any set $X$, the set of all {{< knowl id="function" section="shared-foundations" text="functions" >}} $X\to X$ is a monoid under composition, with identity $\mathrm{id}_X$.
- The set of all $n\times n$ real matrices is a monoid under multiplication, with identity matrix $I_n$; it is not a group because not every matrix is invertible.
