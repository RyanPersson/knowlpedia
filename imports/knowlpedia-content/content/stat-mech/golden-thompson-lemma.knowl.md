+++
id = "stat-mech/golden-thompson-lemma"
title = "Golden–Thompson lemma"
kind = "knowl"
summary = "Trace exponential inequality: for self-adjoint A,B, Tr e^{A+B} ≤ Tr(e^{A}e^{B})."
aliases = ["golden-thompson-lemma", "Golden–Thompson lemma"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/golden-thompson-lemma.md"
+++

## Definitions and notation

- [[quantum-foundations/density-operator|Density operator]] (states on a Hilbert space).
- [[stat-mech-quantum/quantum-partition-function|Quantum partition function]] (as a trace of an exponential).
- See also [[quantum-foundations/golden-thompson-inequality|Golden–Thompson inequality]] for a general reference statement.

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
