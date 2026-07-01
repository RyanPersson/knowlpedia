+++
id = "algebra-modules/direct-sum-universal-property"
title = "Direct sum universal property"
kind = "knowl"
summary = "The direct sum is characterized by a universal mapping property from the summands."
aliases = ["direct-sum-universal-property", "Direct sum universal property"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/direct-sum-universal-property.md"
+++

**Direct sum universal property**: Let $\{M_i\}_{i\in I}$ be a family of $R$-modules, and let $\iota_i:M_i\to \bigoplus_{i\in I}M_i$ be the canonical maps. For any $R$-module $N$ and any family of homomorphisms $f_i:M_i\to N$, there exists a unique homomorphism $f:\bigoplus_{i\in I}M_i\to N$ such that $f\circ \iota_i=f_i$ for all $i\in I$.

This is the defining coproduct property of the [[algebra-modules/direct-sum-modules|direct sum]] in the category of $R$-modules, stated in terms of [[algebra-modules/module-homomorphism|module homomorphisms]].
