+++
id = "fiber-bundles/connection-on-a-vector-bundle"
title = "Connection on a vector bundle"
kind = "knowl"
summary = "A rule for differentiating sections along vector fields, linear over constants and satisfying a Leibniz rule."
aliases = ["connection-on-a-vector-bundle", "Connection on a vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/connection-on-a-vector-bundle.md"
+++

Let $E\to M$ be a smooth vector bundle over a [[fiber-bundles/smooth-manifold|smooth manifold]] $M$. Write $\Gamma(E)$ for the space of smooth sections of $E$, and $\mathfrak X(M)$ for the space of smooth [[fiber-bundles/vector-field|vector fields]] on $M$.

**Definition.** A (Koszul) connection on $E$ is a map
\[
\nabla:\mathfrak X(M)\times \Gamma(E)\to \Gamma(E),\quad (X,s)\mapsto \nabla_X s,
\]
such that for all $X,Y\in\mathfrak X(M)$, $s\in\Gamma(E)$, and $f\in C^\infty(M)$:
1. $\nabla_{X+Y}s=\nabla_X s+\nabla_Y s$ and $\nabla_{fX}s=f\,\nabla_X s$ (so it is $C^\infty(M)$-linear in the vector field), and
2. $\nabla_X(fs)=X(f)\,s+f\,\nabla_X s$ (the [[fiber-bundles/leibniz-rule-for-a-connection|Leibniz rule]] in the section slot).

The expression $\nabla_X s$ is called the [[fiber-bundles/covariant-derivative-of-a-section|covariant derivative of the section]] $s$ along $X$. Equivalently, a connection is an $\mathbb R$-linear operator $\nabla:\Gamma(E)\to\Gamma(T^*M\otimes E)$ such that $\nabla(fs)=df\otimes s+f\,\nabla s$, where $df$ is the 1-form obtained by differentiating $f$.

Connections on associated vector bundles are often constructed from a [[fiber-bundles/principal-connection|principal connection]] on a principal bundle.

## Examples
1. **Trivial connection on a product bundle.** For $E=M\times\mathbb R^r$, writing a section as a vector-valued function $s:M\to\mathbb R^r$, define $\nabla_X s:=X(s)$ (apply $X$ componentwise). This is a connection.
2. **Levi-Civita connection.** A Riemannian metric on $M$ determines a unique torsion-free metric connection on the [[fiber-bundles/tangent-bundle|tangent bundle]] $TM$, the Levi-Civita connection.
3. **Connection from a matrix of 1-forms.** On a trivial rank-$r$ bundle over an open set $U\subset M$, choosing an $r\times r$ matrix $A$ of 1-forms and setting $\nabla = d + A$ defines a connection in that trivialization.
