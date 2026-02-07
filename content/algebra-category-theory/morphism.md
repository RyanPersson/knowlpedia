---
title: "Morphism"
description: "An arrow between objects in a category."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and \(X,Y \in \mathrm{Ob}(\mathcal C)\).
A **morphism** \(f : X \to Y\) is an element of \(\mathrm{Hom}_{\mathcal C}(X,Y)\).

- The **source/domain** of \(f\) is \(X\) (compare {{< knowl id="domain" section="shared-foundations" text="domain" >}}).
- The **target/codomain** of \(f\) is \(Y\) (compare {{< knowl id="codomain" section="shared-foundations" text="codomain" >}}).
- Morphisms can be {{< knowl id="composition-category" text="composed" >}} when targets and sources match, and each object has an {{< knowl id="identity-morphism" text="identity morphism" >}}.

Special cases:
- If \(X=Y\), then \(f\) is an {{< knowl id="endomorphism-category" text="endomorphism" >}}.
- If \(f\) is invertible (has a two-sided inverse), then \(f\) is an {{< knowl id="isomorphism-category" text="isomorphism" >}}.
- If \(f\) is left-cancellative under composition, then \(f\) is a {{< knowl id="monomorphism-category" text="monomorphism" >}} (a “mono”).
- Dually, one has {{< knowl id="epimorphism-category" text="epimorphisms" >}} (“epis”).

## Examples
1. In \(\mathbf{Set}\), morphisms are {{< knowl id="function" section="shared-foundations" text="functions" >}} between sets.
2. In \(\mathbf{Grp}\), morphisms are group homomorphisms.
3. In \(\mathbf{Top}\), morphisms are continuous maps.
