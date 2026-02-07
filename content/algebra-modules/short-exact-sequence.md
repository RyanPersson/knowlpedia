---
title: "Short exact sequence"
description: "An exact sequence 0 → A → B → C → 0 capturing a module extension."
---

A **short exact sequence** is an exact sequence (see {{< knowl id="exact-sequence-modules" text="exact sequence of modules" >}})
\[
0 \to A \xrightarrow{i} B \xrightarrow{p} C \to 0
\]
such that $i$ is injective and $p$ is surjective, and $\operatorname{im}(i)=\ker(p)$. In elementary terms, $i$ is an {{< knowl id="injective-function" section="shared-foundations" text="injective" >}} map identifying $A$ with a submodule of $B$, and $p$ is a {{< knowl id="surjective-function" section="shared-foundations" text="surjective" >}} map with $C\cong B/i(A)$.

Short exact sequences classify extensions: they encode how $B$ is built from a submodule isomorphic to $A$ and a quotient isomorphic to $C$.

**Examples:**
- For any module $M$ and submodule $N\le M$, the canonical sequence $0\to N\to M\to M/N\to 0$ is short exact.
- For $n\ne 0$, the sequence $0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0$ is short exact.
- (Edge case) If $A=0$, a short exact sequence is just $0\to B\xrightarrow{\sim} C\to 0$, so $B\cong C$.
