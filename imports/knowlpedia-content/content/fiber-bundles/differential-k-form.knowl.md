+++
id = "fiber-bundles/differential-k-form"
title = "Differential k-form"
kind = "knowl"
summary = "A smooth alternating covariant k-tensor field; equivalently, a smooth section of the kth exterior power of the cotangent bundle."
aliases = ["differential-k-form", "Differential k-form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/differential-k-form.md"
+++

Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let $\pi:T^*M\to M$ be its [[fiber-bundles/cotangent-bundle|cotangent bundle]].

**Definition.** A **differential $k$-form** on $M$ is a smooth section of the vector bundle $\Lambda^k T^*M\to M$. Concretely, it is a rule that assigns to each $p\in M$ an alternating $k$-linear map
\[
\omega_p:(T_pM)^k\to \mathbb{R},
\]
depending smoothly on $p$ (here $T_pM$ is the [[fiber-bundles/tangent-space-at-a-point|tangent space]]).

The set of all smooth $k$-forms is denoted $\Omega^k(M)$. For $k=0$, one has $\Omega^0(M)=C^\infty(M)$. For $k=1$, a $1$-form is the same thing as a smooth covector field (a smooth section of $T^*M$), and its behavior under smooth maps is governed by the [[fiber-bundles/pullback-of-covectors|pullback of covectors]] (more generally by the [[fiber-bundles/pullback-of-differential-forms|pullback of differential forms]]).

**Local expression.** In a [[fiber-bundles/smooth-chart-coordinate-chart|smooth chart]] $(U,x^1,\dots,x^n)$, every $k$-form can be written uniquely as
\[
\omega = \sum_{1\le i_1<\cdots<i_k\le n} a_{i_1\cdots i_k}\, dx^{i_1}\wedge\cdots\wedge dx^{i_k}
\quad\text{on }U,
\]
with smooth coefficient functions $a_{i_1\cdots i_k}\in C^\infty(U)$, using the [[fiber-bundles/wedge-product-of-differential-forms|wedge product]].

Two fundamental operations on forms are the wedge product $\wedge$ and the [[fiber-bundles/exterior-derivative|exterior derivative]] $d:\Omega^k(M)\to \Omega^{k+1}(M)$, which leads to the notions of [[fiber-bundles/closed-differential-form|closed forms]], [[fiber-bundles/exact-differential-form|exact forms]], and [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology]].

### Examples

1. **A $0$-form and its differential.** Any smooth function $f\in C^\infty(M)$ is a $0$-form. Its exterior derivative $df$ is a $1$-form characterized by $df_p(v)=v(f)$ for $v\in T_pM$.

2. **A $1$-form on $\mathbb{R}^2$.** On $\mathbb{R}^2$ with coordinates $(x,y)$, the expression
   \[
   \omega = x\,dy - y\,dx
   \]
   defines a smooth $1$-form. At each point $(x,y)$, it is a covector that eats a tangent vector $(u,v)$ and returns $xv-yu$.

3. **Standard volume form on $\mathbb{R}^n$.** On $\mathbb{R}^n$ with coordinates $x^1,\dots,x^n$, the $n$-form
   \[
   dx^1\wedge\cdots\wedge dx^n
   \]
   is a nowhere-vanishing differential form (a smooth choice of oriented volume density).
