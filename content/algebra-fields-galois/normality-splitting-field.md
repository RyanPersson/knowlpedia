---
title: "Normal extensions and splitting fields"
description: "An algebraic extension is normal iff it is a splitting field of polynomials over the base field."
---

Let \(K\subseteq L\) be an algebraic {{< knowl id="field-extension" text="field extension" >}}. The following are equivalent:

1. \(L/K\) is a {{< knowl id="normal-extension" text="normal extension" >}}.
2. For every irreducible \(f(x)\in K[x]\) having at least one root in \(L\), the polynomial \(f\) splits completely into linear factors over \(L\).
3. There exists a set \(S\subseteq K[x]\) such that \(L\) is the {{< knowl id="splitting-field" text="splitting field" >}} of \(S\) over \(K\). If \(L/K\) is finite, one may take \(S=\{f\}\) for a single polynomial \(f\in K[x]\).

In particular, finite normal extensions are exactly finite splitting fields (up to \(K\)-isomorphism, cf. {{< knowl id="splitting-field-uniqueness" text="uniqueness of splitting fields" >}}).

### Examples

1. **Quadratic extensions are normal.**  
   \(L=\mathbb{Q}(\sqrt2)\) is the splitting field of \(x^2-2\) over \(\mathbb{Q}\), hence \(L/\mathbb{Q}\) is normal.

2. **A non-normal cubic.**  
   \(L=\mathbb{Q}(\sqrt[3]{2})\) contains one root of \(x^3-2\) but not the complex roots \(\sqrt[3]{2}\zeta_3\), \(\sqrt[3]{2}\zeta_3^2\). Thus \(x^3-2\) does not split over \(L\), so \(L/\mathbb{Q}\) is not normal.

3. **Finite fields as splitting fields.**  
   For \(L=\mathbb{F}_{p^n}\) and \(K=\mathbb{F}_p\), the polynomial \(x^{p^n}-x\in K[x]\) splits over \(L\) with roots exactly the elements of \(L\). Hence \(L/K\) is normal (and in fact {{< knowl id="galois-extension" text="Galois" >}}).
