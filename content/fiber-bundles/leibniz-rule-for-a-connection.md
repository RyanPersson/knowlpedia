---
title: "Leibniz rule for a connection"
description: "The product rule relating differentiation of a scaled section to derivatives of the function and the section."
---

Let $E\to M$ be a vector bundle with a {{< knowl id="connection-on-a-vector-bundle" text="connection" >}} $\nabla$. Let $X$ be a vector field on $M$, $f\in C^\infty(M)$, and $s\in\Gamma(E)$.

**Definition.** The Leibniz rule (product rule) for $\nabla$ is the identity
\[
\nabla_X (f s) \;=\; X(f)\,s \;+\; f\,\nabla_X s.
\]
Equivalently, using the 1-form $df$ defined by the {{< knowl id="exterior-derivative" text="exterior derivative" >}} of $f$, one can write
\[
\nabla(fs)=df\otimes s + f\,\nabla s
\]
as an identity in $\Gamma(T^*M\otimes E)$.

This rule encodes that $\nabla$ differentiates sections “like a derivation” in the section slot, while remaining $C^\infty(M)$-linear in the vector field slot.

## Examples
1. **Trivial connection.** On $E=M\times\mathbb R^r$ with $\nabla_X s=X(s)$, the formula reduces to the usual product rule for differentiating a product of a scalar function and a vector-valued function.
2. **Constant scalars.** If $f$ is constant, then $X(f)=0$ and the rule becomes $\nabla_X(fs)=f\,\nabla_X s$, expressing $\mathbb R$-linearity in the section argument.
3. **Local frame computation.** In a local frame, writing $s=\sum_i s^i e_i$ and using the connection matrix $A$, the rule is reflected in the identity $\nabla(s^i e_i)=ds^i\otimes e_i + s^i \nabla e_i$.
