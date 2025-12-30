---
title: "Existence of Algebraic Closures"
description: "Every field has an algebraic closure."
---

**Theorem (Existence).**  
For every field \(K\), there exists an extension field \(\overline{K}\) such that:

1. \(\overline{K}/K\) is an {{< knowl id="algebraic-extension" text="algebraic extension" >}}, and  
2. \(\overline{K}\) is {{< knowl id="algebraic-closure" text="algebraically closed" >}}.

Such a field \(\overline{K}\) is called an **algebraic closure** of \(K\). Standard proofs use {{< knowl id="zorns-lemma" text="Zorn's lemma" >}} (hence {{< knowl id="axiom-of-choice" text="choice" >}}).

**Examples.**
1. An algebraic closure of \(\mathbb{R}\) is \(\mathbb{C}\) (every complex number satisfies a quadratic over \(\mathbb{R}\)).
2. An algebraic closure of \(\mathbb{F}_p\) is the union \(\bigcup_{n\ge1}\mathbb{F}_{p^n}\) inside a fixed ambient algebraic closure.
3. \(\overline{\mathbb{Q}}\) denotes an algebraic closure of \(\mathbb{Q}\) (often viewed inside \(\mathbb{C}\)).

**Related.** {{< knowl id="algebraic-closure-uniqueness" text="uniqueness of algebraic closures" >}}.
