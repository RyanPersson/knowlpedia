---
title: "Splitting lemma"
description: "A short exact sequence splits iff it has a section or a retraction."
---

**Splitting lemma**: Given a {{</* knowl id="short-exact-sequence" text="short exact sequence" */>}
\[
0\to A \xrightarrow{i} B \xrightarrow{p} C \to 0
\]
of \(R\)-modules, the following are equivalent:
1. There exists a {{</* knowl id="module-homomorphism" text="module homomorphism" */>}} \(s\colon C\to B\) with \(p\circ s=\mathrm{id}_C\) (a section of \(p\)).
2. There exists a homomorphism \(r\colon B\to A\) with \(r\circ i=\mathrm{id}_A\) (a retraction of \(i\)).
3. The sequence is {{</* knowl id="split-exact-sequence" text="split exact" */>}}, i.e. \(B\cong A\oplus C\) as a {{</* knowl id="direct-sum-modules" text="direct sum" */>}}

This lemma is the basic bridge between homomorphisms that admit one-sided inverses and internal direct sum decompositions.
