---
title: "Perfect fields and separability of finite extensions"
description: "Over a perfect field, every algebraic (hence every finite) extension is separable."
---

A {{< knowl id="perfect-field" text="perfect field" >}} is a field \(K\) such that every algebraic extension of \(K\) is {{< knowl id="separable-extension" text="separable" >}}. The key consequence for field extensions is:

**Theorem.** If \(K\) is perfect and \(L/K\) is algebraic (in particular, if \(L/K\) is finite), then \(L/K\) is separable. Moreover, any algebraic extension \(L\) of a perfect field \(K\) is itself perfect.

This is especially useful combined with the {{< knowl id="separable-normal-galois" text="separable + normal = Galois" >}} criterion: over a perfect base field, to check that a finite extension is {{< knowl id="galois-extension" text="Galois" >}}, it suffices to check {{< knowl id="normal-extension" text="normality" >}}.

### Examples

1. **Characteristic \(0\).**  
   Every field of characteristic \(0\) is perfect, so any finite extension of \(\mathbb{Q}\) (e.g. \(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q}\)) is automatically separable.

2. **Finite fields.**  
   Any finite field \(\mathbb{F}_{p^n}\) is perfect (see {{< knowl id="finite-fields-perfect" text="finite fields are perfect" >}}), hence any finite extension \(\mathbb{F}_{p^m}/\mathbb{F}_{p^n}\) is separable.

3. **A non-perfect base gives inseparability.**  
   Let \(K=\mathbb{F}_p(t)\). Then \(K\) is not perfect, and \(L=K(t^{1/p})\) is a finite (degree \(p\)) {{< knowl id="field-extension" text="extension" >}} that is {{< knowl id="inseparable-extension" text="inseparable" >}} (its defining polynomial \(x^p-t\) has zero derivative; see {{< knowl id="separable-distinct-roots" text="separable iff distinct roots" >}}).
