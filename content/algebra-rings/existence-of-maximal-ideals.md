---
title: "Existence of maximal ideals"
description: "Every nontrivial unital commutative ring has a maximal ideal (via Zorn's lemma)."
---

**Existence of maximal ideals (Zorn)**: Let \(R\) be a {{< knowl id="unital-ring" text="unital ring" >}} with \(1\neq 0\), assumed commutative. Then \(R\) has a {{< knowl id="maximal-ideal" text="maximal ideal" >}}.

This result is typically proved using {{< knowl id="zorns-lemma" section="shared-foundations" text="Zorn's lemma" >}} (and hence the {{< knowl id="axiom-of-choice" section="shared-foundations" text="axiom of choice" >}}) applied to the partially ordered set of proper {{< knowl id="ideal" text="ideals" >}} of \(R\) ordered by inclusion.

**Proof sketch**: Let \(\mathcal{P}\) be the set of proper ideals of \(R\), ordered by inclusion. Any chain \(\mathcal{C}\subseteq\mathcal{P}\) has an upper bound \(\bigcup_{J\in\mathcal{C}}J\), which is an ideal and remains proper because \(1\notin J\) for all \(J\in\mathcal{C}\). By Zorn, \(\mathcal{P}\) has a maximal element, which is a maximal ideal.