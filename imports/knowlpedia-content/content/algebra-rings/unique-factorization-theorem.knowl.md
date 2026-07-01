+++
id = "algebra-rings/unique-factorization-theorem"
title = "Unique factorization theorem"
kind = "knowl"
summary = "In a UFD, every nonzero nonunit factors uniquely into irreducibles up to associates and order."
aliases = ["unique-factorization-theorem", "Unique factorization theorem"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/unique-factorization-theorem.md"
+++

**Unique factorization theorem**: Let \(R\) be a [[algebra-rings/ufd|unique factorization domain]]. Every nonzero element of \(R\) that is not a [[algebra-rings/unit|unit]] can be written as a finite product of [[algebra-rings/irreducible-element|irreducible elements]]. Moreover, if
\[
r = u\,p_1\cdots p_m = v\,q_1\cdots q_n
\]
with \(u,v\) units and \(p_i,q_j\) irreducible, then \(m=n\) and after reordering, each \(p_i\) is [[algebra-rings/associated-elements|associated]] to \(q_i\). In particular, irreducibles are [[algebra-rings/prime-element|prime]] in a UFD.

This theorem is the foundational reason gcd/lcm notions behave well in UFDs and underlies factorization results in polynomial rings via Gauss-type arguments.
