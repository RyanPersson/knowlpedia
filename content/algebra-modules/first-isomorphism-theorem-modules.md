---
title: "First isomorphism theorem for modules"
description: "A module homomorphism induces an isomorphism M/ker f ≅ im f."
---

**First isomorphism theorem (modules)**: Let \(f\colon M\to N\) be a {{< knowl id="module-homomorphism" text="module homomorphism" >}}. Then the induced map
\[
\overline f\colon M/\ker(f)\longrightarrow \mathrm{im}(f),\qquad \overline f(m+\ker(f))=f(m),
\]
is an isomorphism of \(R\)-modules. Here \(\ker(f)\) is the {{< knowl id="kernel-module" text="kernel" >}} and \(\mathrm{im}(f)\) is the {{< knowl id="image-module" text="image" >}}, and \(M/\ker(f)\) is a {{< knowl id="quotient-module" text="quotient module" >}}.

This theorem identifies the “effective domain” of a map with its image and is the basic mechanism behind many results in the theory of {{< knowl id="exact-sequence-modules" text="exact sequences" >}}; it is the module analogue of {{< knowl id="first-isomorphism-theorem-rings" section="algebra-rings" text="the first isomorphism theorem for rings" >}}

**Proof sketch**: Define \(\overline f\) as above; it is well-defined because elements differing by \(\ker(f)\) have the same image. Surjectivity is immediate from the definition of \(\mathrm{im}(f)\), and injectivity follows because \(\overline f(m+\ker(f))=0\) implies \(m\in\ker(f)\). Linearity is inherited from \(f\).
