---
title: "Existence of algebraic closures"
description: "Every field admits an algebraic closure."
---

Let \(K\) be a {{< knowl id="field" section="algebra-rings" text="field" >}}.

**Theorem (Existence of algebraic closure).** There exists a {{< knowl id="field-extension" text="field extension" >}} \(\overline{K}/K\) such that:
1. \(\overline{K}\) is algebraically closed (every nonconstant polynomial in \(\overline{K}[x]\) splits into linear factors), and
2. \(\overline{K}/K\) is an {{< knowl id="algebraic-extension" text="algebraic extension" >}} (equivalently, every element of \(\overline{K}\) is an {{< knowl id="algebraic-element" text="algebraic element" >}} over \(K\)).

Such an extension \(\overline{K}\) is called an {{< knowl id="algebraic-closure" text="algebraic closure" >}} of \(K\). A standard proof uses Zorn’s lemma (hence the {{< knowl id="axiom-of-choice" section="shared-foundations" text="axiom of choice" >}}) to build a maximal algebraic extension and then shows it must be algebraically closed.

Moreover, any two algebraic closures of \(K\) are \(K\)-isomorphic; see {{< knowl id="algebraic-closure-uniqueness" text="uniqueness of algebraic closures" >}}.

### Examples
1. \(\mathbb{C}\) is an algebraic closure of \(\mathbb{R}\): it is algebraically closed, and \([\mathbb{C}:\mathbb{R}]=2\), so every complex number is algebraic over \(\mathbb{R}\).

2. The field \(\overline{\mathbb{Q}}\) of algebraic numbers (elements algebraic over \(\mathbb{Q}\)) is an algebraic closure of \(\mathbb{Q}\).

3. An algebraic closure of \(\mathbb{F}_p\) can be realized as the union
   \[
   \overline{\mathbb{F}_p}=\bigcup_{n\ge1}\mathbb{F}_{p^n}
   \]
   inside a fixed ambient algebraic closure. This viewpoint is compatible with the {{< knowl id="finite-field-existence-uniqueness" text="existence and uniqueness of finite fields" >}}.
