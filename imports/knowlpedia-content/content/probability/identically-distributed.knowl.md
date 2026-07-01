+++
id = "probability/identically-distributed"
title = "Identically distributed random variables"
kind = "knowl"
summary = "Two random variables with the same probability law."
aliases = ["identically-distributed", "Identically distributed random variables"]
domains = ["probability"]
legacy_source_path = "probability/identically-distributed.md"
+++

A **pair of identically distributed random variables** \(X\) and \(Y\) is a pair of [[probability/random-variable|random variables]] whose [[probability/distribution-law|distribution laws]] agree; equivalently, for every Borel set \(A\subseteq\mathbb R\),
\[
\mathbb P(X\in A)=\mathbb P(Y\in A).
\]

Identical distribution compares only marginal behavior and does not impose [[probability/independence-random-variables|independence]]. When the relevant moments exist, identically distributed variables have the same [[probability/expectation|expectation]] and the same [[probability/variance|variance]].

**Examples:**
- If \(X\) is the indicator of “heads” on the first fair coin toss and \(Y\) is the indicator of “heads” on the second toss, then \(X\) and \(Y\) are identically distributed (both are Bernoulli\((1/2)\)).
- If \(U\) is uniform on \([0,1]\) and \(Y=1-U\) on the same probability space, then \(U\) and \(Y\) are identically distributed even though they are completely dependent.
