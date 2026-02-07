---
title: "i.i.d. sequence"
description: "A sequence of random variables that are independent and identically distributed."
---

A **sequence of i.i.d. random variables** is a {{< knowl id="sequence" section="shared-foundations" text="sequence" >}} \((X_n)_{n\ge 1}\) of {{< knowl id="random-variable" text="random variables" >}} on a common {{< knowl id="probability-space" text="probability space" >}} such that the family \((X_n)_{n\ge 1}\) is {{< knowl id="independence-random-variables" text="independent" >}} and the variables are {{< knowl id="identically-distributed" text="identically distributed" >}} (equivalently, each \(X_n\) has the same {{< knowl id="distribution-law" text="distribution law" >}} as \(X_1\)).

i.i.d. sequences formalize repeated sampling and are the basic setting for the {{< knowl id="weak-law-large-numbers" text="weak law of large numbers" >}}, the {{< knowl id="strong-law-large-numbers" text="strong law of large numbers" >}}, and the {{< knowl id="central-limit-theorem" text="central limit theorem" >}}.

**Examples:**
- Let \(X_n\) be the indicator that the \(n\)th fair coin toss is heads. Then \((X_n)_{n\ge 1}\) is i.i.d. Bernoulli\((1/2)\).
- Let \(X_1,X_2,\dots\) be independent samples from a normal distribution \(N(0,1)\). Then \((X_n)_{n\ge 1}\) is an i.i.d. sequence with that common law.
