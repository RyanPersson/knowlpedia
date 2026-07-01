+++
id = "algebra-rings/minimal-polynomial-field"
title = "Minimal polynomial over a field"
kind = "knowl"
summary = "The unique monic irreducible polynomial over K annihilating a given algebraic element."
aliases = ["minimal-polynomial-field", "Minimal polynomial over a field"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/minimal-polynomial-field.md"
+++

Let $K\subseteq L$ be fields and let $\alpha\in L$ be algebraic over $K$. The **minimal polynomial of $\alpha$ over $K$** is the unique monic [[algebra-rings/irreducible-polynomial|irreducible polynomial]] $m_{\alpha,K}(x)\in K[x]$ such that $m_{\alpha,K}(\alpha)=0$.

The minimal polynomial packages the algebraic relations of $\alpha$ over the base [[algebra-rings/field|field]] and determines the simple extension $K(\alpha)$ up to $K$-isomorphism. It is defined inside the [[algebra-rings/polynomial-ring|polynomial ring]] $K[x]$ and generates the kernel of the evaluation map $K[x]\to L$, $f\mapsto f(\alpha)$.

**Examples:**
- Over $\mathbb{Q}$, the minimal polynomial of $\sqrt{2}$ is $x^2-2$.
- Over $\mathbb{R}$, the minimal polynomial of $i$ is $x^2+1$.
- If $\alpha\in K$, then the minimal polynomial is $x-\alpha$.
