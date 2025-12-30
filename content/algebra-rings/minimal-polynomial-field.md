---
title: "Minimal polynomial over a field"
description: "The unique monic irreducible polynomial over K annihilating a given algebraic element."
---

Let $K\subseteq L$ be fields and let $\alpha\in L$ be algebraic over $K$. The **minimal polynomial of $\alpha$ over $K$** is the unique monic {{< knowl id="irreducible-polynomial" text="irreducible polynomial" >}} $m_{\alpha,K}(x)\in K[x]$ such that $m_{\alpha,K}(\alpha)=0$.

The minimal polynomial packages the algebraic relations of $\alpha$ over the base {{< knowl id="field" text="field" >}} and determines the simple extension $K(\alpha)$ up to $K$-isomorphism. It is defined inside the {{< knowl id="polynomial-ring" text="polynomial ring" >}} $K[x]$ and generates the kernel of the evaluation map $K[x]\to L$, $f\mapsto f(\alpha)$.

**Examples:**
- Over $\mathbb{Q}$, the minimal polynomial of $\sqrt{2}$ is $x^2-2$.
- Over $\mathbb{R}$, the minimal polynomial of $i$ is $x^2+1$.
- If $\alpha\in K$, then the minimal polynomial is $x-\alpha$.