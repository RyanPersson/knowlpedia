---
title: "Principal bundle over S1 from a clutching function"
description: "A principal G bundle over the circle can be constructed by gluing a cylinder using a group element or clutching data."
---

This is the $1$-dimensional case of the general {{< knowl id="clutching-function" text="clutching construction" >}} for bundles.

Let $G$ be a Lie group, and consider the circle as a quotient $S^1 \cong [0,1]/(0\sim 1)$.

## Construction (gluing by an element of G)
Fix an element $g\in G$. Define
\[
P_g := \big([0,1]\times G\big)\big/\sim,
\]
where the equivalence relation identifies the ends by
\[
(0,h)\sim (1,gh)\qquad\text{for all }h\in G.
\]
Let $\pi:P_g\to S^1$ be induced by the projection $[0,1]\times G\to [0,1]\to S^1$, and let $G$ act on $P_g$ by the right action
\[
[(t,h)]\cdot k := [(t,hk)].
\]
Then $\pi:P_g\to S^1$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}.

One can describe this equivalently in transition-function language: choose an open cover of $S^1$ by two arcs $U_0,U_1$ so that $U_0\cap U_1$ has two connected components, and take transition functions that are constant on each component, with one of them equal to $g$. This viewpoint ties the construction to {{< knowl id="principal-bundle-transition-function" text="principal bundle transition functions" >}} and the {{< knowl id="cocycle-condition-for-transition-functions" text="cocycle condition" >}}.

## Isomorphism remarks
- If $G$ is connected, then every principal $G$-bundle over $S^1$ is trivial (since $[S^1,BG]\cong \pi_1(BG)\cong \pi_0(G)$). In that case, each $P_g$ is isomorphic to the {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}} even when $g\neq e$.
- If $G$ is discrete (or more generally not connected), different clutching data can produce non-isomorphic bundles. Over $S^1$, the classification reduces to homomorphisms $\pi_1(S^1)\cong \mathbb Z\to G$ up to conjugation, i.e. conjugacy classes of elements of $G$, matching the intuition that $g$ records a “monodromy.”

## Examples
1. **Discrete group G = Z2: trivial vs nontrivial double cover.**  
   For $G=\mathbb Z_2=\{\pm 1\}$, the construction gives two isomorphism classes: $P_{+1}$ (trivial) and $P_{-1}$ (nontrivial). The nontrivial bundle corresponds to the connected double cover $S^1\to S^1$, $z\mapsto z^2$, viewed as a principal $\mathbb Z_2$-bundle.

2. **O(1) bundles and the Möbius line bundle.**  
   Since $O(1)\cong \mathbb Z_2$, the two principal $O(1)$-bundles over $S^1$ are exactly the ones above. The nontrivial principal $O(1)$-bundle yields, via the standard action on $\mathbb R$, the Möbius real line bundle as an associated vector bundle (compare {{< knowl id="associated-vector-bundle" text="associated vector bundle" >}}).

3. **Connected groups: U(1) gives only the trivial principal bundle over S1.**  
   For $G=U(1)$ (connected), any choice of $g\in U(1)$ produces a bundle $P_g$ that is isomorphic to $S^1\times U(1)$. This is a concrete instance of the equivalence “bundle is trivial iff it admits a global section,” as in {{< knowl id="tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm" text="the triviality criteria for principal bundles" >}}.
