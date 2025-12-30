---
title: "Injective module"
description: "A module with the extension property against injective homomorphisms."
---

An **injective module** is a left {{< knowl id="module" text="module" >}} \(E\) over a {{< knowl id="ring" text="ring" >}} \(R\) such that for every injective {{< knowl id="module-homomorphism" text="module homomorphism" >}} \(i\colon A\hookrightarrow B\) and every homomorphism \(f\colon A\to E\), there exists a homomorphism \(g\colon B\to E\) with \(g\circ i=f\).

Equivalently, the contravariant functor \(\mathrm{Hom}_R(-,E)\) is exact on {{< knowl id="exact-sequence-modules" text="exact sequences" >}} (or, equivalently, \(\mathrm{Ext}^1_R(-,E)=0\)). Injective modules are the categorical dual of {{< knowl id="projective-module" text="projective modules" >}}, and they can be recognized by {{< knowl id="baers-criterion" text="Baer’s criterion" >}} in many settings.

**Examples:**
- Over a {{< knowl id="field" text="field" >}}, every {{< knowl id="vector-space" text="vector space" >}} is injective as a module.
- As a \(\mathbb Z\)-module, \(\mathbb Q/\mathbb Z\) is injective (more generally, divisible abelian groups are injective \(\mathbb Z\)-modules).
- If \(\{E_i\}_{i\in I}\) are injective \(R\)-modules, then \(\prod_{i\in I} E_i\) is injective.
