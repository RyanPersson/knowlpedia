---
title: "Category Argument Template"
description: "A standard Baire category method for producing a dense or residual set by intersecting dense open sets."
---

**Category argument template:** Let $X$ be a {{< knowl id="baire-space" text="Baire space" >}} and let $U_1,U_2,\dots \subseteq X$ be sets that are each {{< knowl id="open-set" text="open" >}} and {{< knowl id="dense-set" text="dense" >}} in $X$. Then the intersection $\bigcap_{n=1}^\infty U_n$ is dense (in particular, nonempty) in $X$, and it is a {{< knowl id="residual-set" text="residual set" >}} since its complement is a countable union of {{< knowl id="nowhere-dense-set" text="nowhere dense sets" >}}.

Conceptually, this packages the {{< knowl id="baire-category-theorem" text="Baire category theorem" >}} into a reusable method: encode the $n$th requirement of a property as membership in a dense open set $U_n$, and then conclude that there are points satisfying all requirements at once (finite versions rely only on {{< knowl id="intersection-of-dense-open-is-dense" text="intersection of dense open sets being dense" >}}).
