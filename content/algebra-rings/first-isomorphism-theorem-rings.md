---
title: "First isomorphism theorem for rings"
description: "A ring homomorphism induces an isomorphism from the quotient by its kernel onto its image."
---

**First isomorphism theorem (rings)**: Let \(\varphi:R\to S\) be a {{< knowl id="ring-homomorphism" text="ring homomorphism" >}}. Then the induced map
\[
\bar\varphi: R/\ker(\varphi)\longrightarrow \operatorname{im}(\varphi),\qquad r+\ker(\varphi)\longmapsto \varphi(r),
\]
is a {{< knowl id="ring-isomorphism" text="ring isomorphism" >}}, where \(\ker(\varphi)\) is the {{< knowl id="kernel-ring" text="kernel" >}} and \(\operatorname{im}(\varphi)\) is the {{< knowl id="image-ring" text="image" >}}.

This identifies the universal quotient {{< knowl id="quotient-ring" text="quotient ring" >}} determined by \(\varphi\) with the concrete subring realized as its image, and is the basic tool behind “modding out by relations” in ring constructions.

**Proof sketch**: Define \(\bar\varphi(r+\ker\varphi)=\varphi(r)\). If \(r-r'\in\ker\varphi\), then \(\varphi(r)=\varphi(r')\), so the map is well-defined. It is clearly a ring homomorphism, surjective by definition of the image, and injective because \(\bar\varphi(r+\ker\varphi)=0\) implies \(r\in\ker\varphi\).