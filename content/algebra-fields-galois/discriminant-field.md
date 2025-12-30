---
title: "Discriminant of a field basis"
description: "For a finite extension L/K, the discriminant det(Tr(α_i α_j)) of a K-basis (α_i)."
---

**Definition.** Let \(L/K\) be a finite {{< knowl id="separable-extension" text="separable" >}} extension of degree \(n\), and let \(\alpha_1,\dots,\alpha_n\) be a \(K\)-basis of \(L\). The **discriminant** of this basis is
\[
\mathrm{disc}(\alpha_1,\dots,\alpha_n)
\;=\;
\det\!\big(\mathrm{Tr}_{L/K}(\alpha_i\alpha_j)\big)_{1\le i,j\le n}
\;\in\; K,
\]
where \(\mathrm{Tr}_{L/K}\) is the {{< knowl id="trace-field" text="field trace" >}} and \(\det\) is the {{< knowl id="determinant" text="determinant" >}}.

Under a change of basis by a matrix \(M\in \mathrm{GL}_n(K)\), the discriminant scales by \((\det M)^2\). In particular, whether the discriminant is zero or nonzero does not depend on the chosen basis (for separable extensions it is nonzero).

**See also.** {{< knowl id="norm-field" text="field norm" >}}, {{< knowl id="degree-of-extension" text="degree" >}}.

**Examples.**
1. For \(L=\mathbb{Q}(\sqrt2)\) with basis \((1,\sqrt2)\):
   \[
   \big(\mathrm{Tr}(\alpha_i\alpha_j)\big)=
   \begin{pmatrix}
   2 & 0\\
   0 & 4
   \end{pmatrix}
   \quad\Rightarrow\quad
   \mathrm{disc}(1,\sqrt2)=8.
   \]
2. For \(L=\mathbb{Q}(i)\) with basis \((1,i)\), one gets \(\mathrm{disc}(1,i)=-4\).
3. For \(L=\mathbb{F}_{q^2}\) over \(\mathbb{F}_q\), any \(\mathbb{F}_q\)-basis has nonzero discriminant because the trace pairing \((x,y)\mapsto \mathrm{Tr}(xy)\) is nondegenerate.
