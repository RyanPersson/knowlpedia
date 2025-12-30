---
title: "Split exact sequence"
description: "A short exact sequence that decomposes as a direct sum."
---

A short exact sequence
\[
0 \to A \xrightarrow{i} B \xrightarrow{p} C \to 0
\]
(see {{< knowl id="short-exact-sequence" text="short exact sequence" >}}) **splits** if there exists a homomorphism $s:C\to B$ with $p\circ s=\mathrm{id}_C$ (a section), or equivalently a homomorphism $r:B\to A$ with $r\circ i=\mathrm{id}_A$ (a retraction), where $\mathrm{id}$ is the {{< knowl id="identity-function" text="identity" >}} map. In this case one has an isomorphism $B\cong A\oplus C$ as in {{< knowl id="direct-sum-modules" text="direct sums" >}}; a standard proof is the {{< knowl id="splitting-lemma" text="splitting lemma" >}}.

Split exactness is the precise condition that the extension carries no “twisting”: $B$ is just a direct sum of the ends.

**Examples:**
- The sequence $0\to A \to A\oplus C \to C\to 0$ splits (take $s(c)=(0,c)$).
- For an $R$-linear projection $p:B\to C$ with a right-inverse $s$, the sequence $0\to \ker(p)\to B\to C\to 0$ splits.
- (Nonexample) For $n>1$, the sequence $0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0$ does not split.
