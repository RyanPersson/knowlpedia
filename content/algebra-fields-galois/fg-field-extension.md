---
title: "Finitely generated field extension"
description: "An extension L/K of the form L = K(S) for some finite set S ⊂ L."
---

**Definition.** A {{</* knowl id="field-extension" text="field extension" */>}} \(L/K\) is **finitely generated** if there exist elements \(\alpha_1,\dots,\alpha_r\in L\) such that
\[
L = K(\alpha_1,\dots,\alpha_r),
\]
the smallest subfield of \(L\) containing \(K\) and all \(\alpha_i\).  
Equivalently, \(L\) is obtained from \(K\) by adjoining finitely many elements, possibly algebraic and/or transcendental.

A {{</* knowl id="simple-extension" text="simple extension" */>}} is the special case \(r=1\).

**See also.** {{</* knowl id="algebraic-extension" text="algebraic extension" */>}}, {{</* knowl id="transcendental-extension" text="transcendental extension" */>}}.

**Examples.**
1. \(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q}\) is finitely generated (and finite).
2. \(\mathbb{Q}(t,\sqrt{t})/\mathbb{Q}\) is finitely generated: first adjoin transcendental \(t\), then adjoin \(\sqrt t\).
3. The rational function field \(K(x,y)=K(x,y)\) is finitely generated over \(K\) by \(\{x,y\}\) but has infinite degree.
