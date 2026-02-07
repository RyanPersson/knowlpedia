---
title: "Golden–Thompson lemma"
description: "Trace exponential inequality: for self-adjoint A,B, Tr e^{A+B} ≤ Tr(e^{A}e^{B})."
---

## Definitions and notation

- {{< knowl id="density-operator" section="quantum-foundations" text="Density operator" >}} (states on a Hilbert space).
- {{< knowl id="quantum-partition-function" section="stat-mech-quantum" text="Quantum partition function" >}} (as a trace of an exponential).
- See also {{< knowl id="golden-thompson-inequality" section="quantum-foundations" text="Golden–Thompson inequality" >}} for a general reference statement.

## Statement

Let $A$ and $B$ be self-adjoint operators on a finite-dimensional Hilbert space (or assume $e^{A+B}$ is trace-class so the trace is finite). Then
$$
\operatorname{Tr}\big(e^{A+B}\big) \le \operatorname{Tr}\big(e^{A}e^{B}\big).
$$

If $A$ and $B$ commute, then $e^{A+B}=e^{A}e^{B}$ and equality holds.

## Key hypotheses and conclusions

**Hypotheses**
- $A$ and $B$ are self-adjoint.
- The traces involved are finite (automatic in finite dimension).

**Conclusions**
- A fundamental bound for trace exponentials: $\operatorname{Tr}(e^{A+B}) \le \operatorname{Tr}(e^{A}e^{B})$.
- Equality when $[A,B]=0$.

