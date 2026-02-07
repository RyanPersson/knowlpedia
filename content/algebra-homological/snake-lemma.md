---
title: "Snake lemma"
description: "From a commutative diagram with exact rows, produces an exact sequence of kernels and cokernels with a canonical connecting map."
---

The snake lemma is a fundamental diagram-chase statement in the category of \(R\)-modules, and more generally in any {{< knowl id="abelian-category" section="algebra-category-theory" text="abelian category" >}}.

It relates {{< knowl id="kernel-categorical" section="algebra-category-theory" text="kernels" >}} and {{< knowl id="cokernel-categorical" section="algebra-category-theory" text="cokernels" >}} (compare also {{< knowl id="cokernel-module" section="algebra-modules" text="cokernel of a module map" >}}) across two exact rows ({{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequences" >}}).

## Theorem (Snake lemma)

Suppose we have a commutative diagram of \(R\)-modules with exact rows
\[
\begin{array}{ccccccccc}
0 &\to& A' &\xrightarrow{i}& A &\xrightarrow{p}& A'' &\to& 0\\
 & & \downarrow f' & & \downarrow f & & \downarrow f'' & & \\
0 &\to& B' &\xrightarrow{j}& B &\xrightarrow{q}& B'' &\to& 0
\end{array}
\]
Then there is a canonical connecting homomorphism (boundary map)
\[
\delta:\ker(f'') \longrightarrow \operatorname{coker}(f')
\]
such that the following sequence is exact:
\[
0 \to \ker(f') \to \ker(f) \to \ker(f'') \xrightarrow{\ \delta\ } \operatorname{coker}(f') \to \operatorname{coker}(f) \to \operatorname{coker}(f'') \to 0.
\]

This \(\delta\) is natural in the diagram, and is the prototype for the {{< knowl id="connecting-homomorphism-lemma" text="connecting homomorphism" >}} appearing in long exact sequences.

### Construction of \(\delta\) (explicit)
Given \(x\in \ker(f'')\subseteq A''\):
1. pick \(a\in A\) with \(p(a)=x\);
2. since \(f''(x)=0\), commutativity implies \(q(f(a))=0\), hence \(f(a)\in \operatorname{im}(j)\);
3. choose \(b'\in B'\) with \(j(b')=f(a)\);
4. define \(\delta(x)\) to be the class of \(b'\) in \(\operatorname{coker}(f')=B'/\operatorname{im}(f')\).

A standard diagram chase shows this is well-defined (independent of choices) and gives exactness.

## Examples

1. **Induced map on quotients: the “kernel–cokernel” exact sequence.**  
   Let \(g:M\to M'\) be an \(R\)-linear map, and let \(N\subseteq M\), \(N'\subseteq M'\) satisfy \(g(N)\subseteq N'\). Consider the commutative diagram with exact rows:
   \[
   \begin{array}{ccccccccc}
   0 &\to& N &\to& M &\to& M/N &\to& 0\\
    & & \downarrow g|_N & & \downarrow g & & \downarrow \overline g & & \\
   0 &\to& N' &\to& M' &\to& M'/N' &\to& 0
   \end{array}
   \]
   The snake lemma produces the exact sequence
   \[
   0\to \ker(g|_N)\to \ker(g)\to \ker(\overline g)\xrightarrow{\delta}
   \operatorname{coker}(g|_N)\to \operatorname{coker}(g)\to \operatorname{coker}(\overline g)\to 0,
   \]
   which cleanly measures how kernels/cokernels change when passing to quotients.

2. **Boundary map in homology from a short exact sequence of complexes.**  
   Given a degreewise short exact sequence of {{< knowl id="chain-complex" text="chain complexes" >}}
   \[
   0\to C'_\bullet \to C_\bullet \to C''_\bullet \to 0,
   \]
   one applies the snake lemma to the diagram of cycles and boundaries in each degree to construct the connecting map
   \[
   \partial: H_n(C''_\bullet)\longrightarrow H_{n-1}(C'_\bullet),
   \]
   yielding the usual long exact sequence in {{< knowl id="homology-module" text="homology" >}}. (This is the chain-complex analogue of {{< knowl id="long-exact-sequence-derived" text="long exact sequences from derived functors" >}}.)

3. **Computing a boundary map concretely (multiplication on a quotient).**  
   Fix integers \(m,n\) and consider the diagram
   \[
   \begin{array}{ccccccccc}
   0&\to& \mathbb Z &\xrightarrow{\cdot m}& \mathbb Z &\to& \mathbb Z/m &\to& 0\\
    && \downarrow \cdot n && \downarrow \cdot n && \downarrow \cdot n &&\\
   0&\to& \mathbb Z &\xrightarrow{\cdot m}& \mathbb Z &\to& \mathbb Z/m &\to& 0
   \end{array}
   \]
   The connecting map \(\delta:\ker(\cdot n:\mathbb Z/m\to \mathbb Z/m)\to \operatorname{coker}(\cdot n:\mathbb Z\to \mathbb Z)\cong \mathbb Z/n\)
   sends a class \(\overline{x}\in\mathbb Z/m\) with \(nx\in m\mathbb Z\) to the class of \(\frac{nx}{m}\) in \(\mathbb Z/n\). This is a concrete instance of how \(\delta\) encodes the failure of lifting across the diagram.
