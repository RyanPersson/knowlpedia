+++
id = "lie-groups/root-lie-algebra"
title = "Root of a Lie algebra"
kind = "knowl"
summary = "A nonzero weight for the adjoint action of a Cartan subalgebra on a semisimple Lie algebra."
aliases = ["root-lie-algebra", "Root of a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/root-lie-algebra.md"
+++

Let $\mathfrak g$ be a finite-dimensional complex semisimple Lie algebra (see [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]]) and let $\mathfrak h\subset \mathfrak g$ be a [[lie-groups/cartan-subalgebra|Cartan subalgebra]]. For $\alpha\in \mathfrak h^*$, define the **$\alpha$-weight space for the adjoint action** by
\[
\mathfrak g_\alpha \;:=\;\{X\in\mathfrak g : [H,X]=\alpha(H)\,X\ \text{for all }H\in\mathfrak h\}.
\]
A nonzero functional $\alpha\in\mathfrak h^*$ is called a **root** of $\mathfrak g$ (relative to $\mathfrak h$) if $\mathfrak g_\alpha\neq 0$. The set of roots is denoted $\Phi\subset \mathfrak h^*$.

Equivalently, roots are the nonzero weights of the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] restricted to $\mathfrak h$. Each root comes with its [[lie-groups/root-space|root space]] $\mathfrak g_\alpha$, and together they assemble into the [[lie-groups/root-space-decomposition|root space decomposition]]. With the inner product on $\mathfrak h^*$ induced by the [[lie-groups/killing-form|Killing form]], the set $\Phi$ satisfies the axioms of a [[lie-groups/root-system|root system]].

Roots are the combinatorial shadow of $\mathfrak g$: much of the structure and classification of semisimple Lie algebras is encoded in $\Phi$ (compare [[lie-groups/dynkin-diagram|Dynkin diagrams]] and [[lie-groups/classification-simple-lie-algebras|classification of simple Lie algebras]]).
