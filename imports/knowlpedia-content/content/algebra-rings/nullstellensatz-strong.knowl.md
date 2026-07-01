+++
id = "algebra-rings/nullstellensatz-strong"
title = "Hilbert's Nullstellensatz (strong)"
kind = "knowl"
summary = "Over an algebraically closed field, the ideal of a variety is the radical of the defining ideal."
aliases = ["nullstellensatz-strong", "Hilbert's Nullstellensatz (strong)"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/nullstellensatz-strong.md"
+++

**Hilbert's Nullstellensatz (strong)**: Let \(k\) be an algebraically closed [[algebra-rings/field|field]] and let \(I\triangleleft k[x_1,\dots,x_n]\) be an [[algebra-rings/ideal|ideal]] in the [[algebra-rings/polynomial-ring|polynomial ring]]. Let
\[
I(V(I))=\{f\in k[x_1,\dots,x_n] : f(a)=0\ \text{for all }a\in V(I)\}.
\]
Then
\[
I(V(I))=\sqrt{I},
\]
where \(\sqrt{I}\) denotes the [[algebra-rings/radical-of-ideal|radical of an ideal]].

This identifies geometric vanishing with algebraic nilpotence modulo \(I\) and implies, for instance, that varieties correspond to radical ideals and irreducible varieties correspond to [[algebra-rings/prime-ideal|prime ideals]].
