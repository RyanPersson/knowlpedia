---
title: "Algebraic element"
description: "An element α is algebraic over K if it satisfies a nonzero polynomial with coefficients in K."
---

**Definition.** Let \(L/K\) be a {{< knowl id="field-extension" text="field extension" >}} and let \(\alpha\in L\). The element \(\alpha\) is **algebraic over \(K\)** if there exists a nonzero polynomial \(f(x)\in K[x]\) such that \(f(\alpha)=0\).  
If no such nonzero polynomial exists, \(\alpha\) is {{< knowl id="transcendental-element" text="transcendental over K" >}}.

Among all polynomials in \(K[x]\) vanishing at \(\alpha\), there is a unique monic one of minimal degree: the {{< knowl id="minimal-polynomial-field" text="minimal polynomial" >}} \(m_\alpha(x)\), which is {{< knowl id="irreducible-polynomial" text="irreducible" >}} in \(K[x]\).

**See also.** {{< knowl id="simple-extension" text="simple extension" >}}, {{< knowl id="algebraic-extension" text="algebraic extension" >}}.

**Examples.**
1. \(\sqrt2\) is algebraic over \(\mathbb{Q}\) since it satisfies \(x^2-2=0\); its minimal polynomial is \(x^2-2\).
2. \(i\) is algebraic over \(\mathbb{R}\) since \(i^2+1=0\); \(\mathbb{C}=\mathbb{R}(i)\).
3. A {{< knowl id="primitive-root-of-unity" text="primitive n-th root of unity" >}} \(\zeta_n\) is algebraic over \(\mathbb{Q}\) since \(\zeta_n^n-1=0\) (more precisely it satisfies the {{< knowl id="cyclotomic-polynomial" text="cyclotomic polynomial" >}} \(\Phi_n(x)\)).
