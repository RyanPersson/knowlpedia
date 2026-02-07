---
title: "Connection on a vector bundle"
description: "A rule for differentiating sections along vector fields, linear over constants and satisfying a Leibniz rule."
---

Let $E\to M$ be a smooth vector bundle over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$. Write $\Gamma(E)$ for the space of smooth sections of $E$, and $\mathfrak X(M)$ for the space of smooth {{< knowl id="vector-field" text="vector fields" >}} on $M$.

**Definition.** A (Koszul) connection on $E$ is a map
\[
\nabla:\mathfrak X(M)\times \Gamma(E)\to \Gamma(E),\quad (X,s)\mapsto \nabla_X s,
\]
such that for all $X,Y\in\mathfrak X(M)$, $s\in\Gamma(E)$, and $f\in C^\infty(M)$:
1. $\nabla_{X+Y}s=\nabla_X s+\nabla_Y s$ and $\nabla_{fX}s=f\,\nabla_X s$ (so it is $C^\infty(M)$-linear in the vector field), and
2. $\nabla_X(fs)=X(f)\,s+f\,\nabla_X s$ (the {{< knowl id="leibniz-rule-for-a-connection" text="Leibniz rule" >}} in the section slot).

The expression $\nabla_X s$ is called the {{< knowl id="covariant-derivative-of-a-section" text="covariant derivative of the section" >}} $s$ along $X$. Equivalently, a connection is an $\mathbb R$-linear operator $\nabla:\Gamma(E)\to\Gamma(T^*M\otimes E)$ such that $\nabla(fs)=df\otimes s+f\,\nabla s$, where $df$ is the 1-form obtained by differentiating $f$.

Connections on associated vector bundles are often constructed from a {{< knowl id="principal-connection" text="principal connection" >}} on a principal bundle.

## Examples
1. **Trivial connection on a product bundle.** For $E=M\times\mathbb R^r$, writing a section as a vector-valued function $s:M\to\mathbb R^r$, define $\nabla_X s:=X(s)$ (apply $X$ componentwise). This is a connection.
2. **Levi-Civita connection.** A Riemannian metric on $M$ determines a unique torsion-free metric connection on the {{< knowl id="tangent-bundle" text="tangent bundle" >}} $TM$, the Levi-Civita connection.
3. **Connection from a matrix of 1-forms.** On a trivial rank-$r$ bundle over an open set $U\subset M$, choosing an $r\times r$ matrix $A$ of 1-forms and setting $\nabla = d + A$ defines a connection in that trivialization.
