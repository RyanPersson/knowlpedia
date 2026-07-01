+++
id = "probability/iid-sequence"
title = "i.i.d. sequence"
kind = "knowl"
summary = "A sequence of random variables that are independent and identically distributed."
aliases = ["iid-sequence", "i.i.d. sequence"]
domains = ["probability"]
legacy_source_path = "probability/iid-sequence.md"
+++

A **sequence of i.i.d. random variables** is a [[shared-foundations/sequence|sequence]] \((X_n)_{n\ge 1}\) of [[probability/random-variable|random variables]] on a common [[probability/probability-space|probability space]] such that the family \((X_n)_{n\ge 1}\) is [[probability/independence-random-variables|independent]] and the variables are [[probability/identically-distributed|identically distributed]] (equivalently, each \(X_n\) has the same [[probability/distribution-law|distribution law]] as \(X_1\)).

i.i.d. sequences formalize repeated sampling and are the basic setting for the [[probability/weak-law-large-numbers|weak law of large numbers]], the [[probability/strong-law-large-numbers|strong law of large numbers]], and the [[probability/central-limit-theorem|central limit theorem]].

**Examples:**
- Let \(X_n\) be the indicator that the \(n\)th fair coin toss is heads. Then \((X_n)_{n\ge 1}\) is i.i.d. Bernoulli\((1/2)\).
- Let \(X_1,X_2,\dots\) be independent samples from a normal distribution \(N(0,1)\). Then \((X_n)_{n\ge 1}\) is an i.i.d. sequence with that common law.
