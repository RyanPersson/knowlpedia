---
title: "Identically distributed random variables"
description: "Two random variables with the same probability law."
---

A **pair of identically distributed random variables** \(X\) and \(Y\) is a pair of {{< knowl id="random-variable" text="random variables" >}} whose {{< knowl id="distribution-law" text="distribution laws" >}} agree; equivalently, for every Borel set \(A\subseteq\mathbb R\),
\[
\mathbb P(X\in A)=\mathbb P(Y\in A).
\]

Identical distribution compares only marginal behavior and does not impose {{< knowl id="independence-random-variables" text="independence" >}}. When the relevant moments exist, identically distributed variables have the same {{< knowl id="expectation" text="expectation" >}} and the same {{< knowl id="variance" text="variance" >}}.

**Examples:**
- If \(X\) is the indicator of “heads” on the first fair coin toss and \(Y\) is the indicator of “heads” on the second toss, then \(X\) and \(Y\) are identically distributed (both are Bernoulli\((1/2)\)).
- If \(U\) is uniform on \([0,1]\) and \(Y=1-U\) on the same probability space, then \(U\) and \(Y\) are identically distributed even though they are completely dependent.
