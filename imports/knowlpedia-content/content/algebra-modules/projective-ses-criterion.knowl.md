+++
id = "algebra-modules/projective-ses-criterion"
title = "Projective short exact sequence criterion"
kind = "knowl"
summary = "A module is projective iff every short exact sequence ending in it splits."
aliases = ["projective-ses-criterion", "Projective short exact sequence criterion"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/projective-ses-criterion.md"
+++

**Projective s.e.s. criterion**: An \(R\)-[[algebra-modules/module|module]] \(P\) is [[algebra-modules/projective-module|projective]] if and only if every [[algebra-modules/short-exact-sequence|short exact sequence]]
\[
0\to A\to B\to P\to 0
\]
is [[algebra-modules/split-exact-sequence|split exact]].

This reformulates projectivity as a splitting property for extensions of \(P\). The "only if" direction uses a lift of \(\mathrm{id}_P\) along the surjection \(B\to P\), and the "if" direction follows by encoding a lifting problem as the splitting of an induced extension (compare the [[algebra-modules/splitting-lemma|splitting lemma]]).
