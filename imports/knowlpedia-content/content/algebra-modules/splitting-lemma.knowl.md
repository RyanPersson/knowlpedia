+++
id = "algebra-modules/splitting-lemma"
title = "Splitting lemma"
kind = "knowl"
summary = "A short exact sequence splits iff it has a section or a retraction."
aliases = ["splitting-lemma", "Splitting lemma"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/splitting-lemma.md"
+++

**Splitting lemma**: Given a [[algebra-modules/short-exact-sequence|short exact sequence]]
\[
0\to A \xrightarrow{i} B \xrightarrow{p} C \to 0
\]
of \(R\)-[[algebra-modules/module|modules]], the following are equivalent:
1. There exists a [[algebra-modules/module-homomorphism|module homomorphism]] \(s\colon C\to B\) with \(p\circ s=\mathrm{id}_C\) (a section of \(p\)).
2. There exists a homomorphism \(r\colon B\to A\) with \(r\circ i=\mathrm{id}_A\) (a retraction of \(i\)).
3. The sequence is [[algebra-modules/split-exact-sequence|split exact]], i.e. \(B\cong A\oplus C\) as a [[algebra-modules/direct-sum-modules|direct sum]].

This lemma is the basic bridge between homomorphisms that admit one-sided inverses and internal direct sum decompositions.
