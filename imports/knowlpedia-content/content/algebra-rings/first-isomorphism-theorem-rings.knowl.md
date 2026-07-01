+++
id = "algebra-rings/first-isomorphism-theorem-rings"
title = "First isomorphism theorem for rings"
kind = "knowl"
summary = "A ring homomorphism induces an isomorphism from the quotient by its kernel onto its image."
aliases = ["first-isomorphism-theorem-rings", "First isomorphism theorem for rings"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/first-isomorphism-theorem-rings.md"
+++

**First isomorphism theorem (rings)**: Let \(\varphi:R\to S\) be a [[algebra-rings/ring-homomorphism|ring homomorphism]]. Then the induced map
\[
\bar\varphi: R/\ker(\varphi)\longrightarrow \operatorname{im}(\varphi),\qquad r+\ker(\varphi)\longmapsto \varphi(r),
\]
is a [[algebra-rings/ring-isomorphism|ring isomorphism]], where \(\ker(\varphi)\) is the [[algebra-rings/kernel-ring|kernel]] and \(\operatorname{im}(\varphi)\) is the [[algebra-rings/image-ring|image]].

This identifies the universal quotient [[algebra-rings/quotient-ring|quotient ring]] determined by \(\varphi\) with the concrete subring realized as its image, and is the basic tool behind “modding out by relations” in ring constructions.
