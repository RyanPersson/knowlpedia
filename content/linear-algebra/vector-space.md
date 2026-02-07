---
title: "Vector space"
description: "A set with addition and scalar multiplication satisfying the vector space axioms."
---

A **vector space** over a {{< knowl id="field-axioms" section="real-analysis" text="field" >}} $\mathbb{F}$ is a {{< knowl id="set" section="shared-foundations" text="set" >}} $V$ equipped with two operations ({{< knowl id="function" section="shared-foundations" text="functions" >}}) $+:V\times V\to V$ and $\cdot:\mathbb{F}\times V\to V$ such that for all $u,v,w\in V$ and $a,b\in\mathbb{F}$:
\[
\begin{aligned}
&u+v=v+u,\qquad (u+v)+w=u+(v+w),\\
&\exists\,0\in V:\ v+0=v,\qquad \forall v\in V\ \exists\,(-v)\in V:\ v+(-v)=0,\\
&a\cdot(u+v)=a\cdot u+a\cdot v,\qquad (a+b)\cdot v=a\cdot v+b\cdot v,\\
&(ab)\cdot v=a\cdot(b\cdot v),\qquad 1\cdot v=v.
\end{aligned}
\]

Vector spaces are the basic objects studied via {{< knowl id="linear-map" text="linear maps" >}} and invariants such as the {{< knowl id="determinant" text="determinant" >}} and {{< knowl id="eigenvalue" text="eigenvalues" >}} of operators.

**Examples:**
- $\mathbb{R}^n$ with componentwise addition and scalar multiplication is a vector space over $\mathbb{R}$.
- The set of polynomials $\mathbb{F}[x]$ with the usual addition and scalar multiplication is a vector space over $\mathbb{F}$.
- The set of $m\times n$ matrices over $\mathbb{F}$ is a vector space over $\mathbb{F}$.
