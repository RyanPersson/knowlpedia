+++
id = "algebra-rings/ufd-implies-gcd-exists"
title = "UFD implies GCDs exist"
kind = "knowl"
summary = "In a unique factorization domain, any two elements admit a gcd unique up to associates."
aliases = ["ufd-implies-gcd-exists", "UFD implies GCDs exist"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ufd-implies-gcd-exists.md"
+++

**UFD implies GCDs exist**: Let $R$ be a UFD and let $a,b\in R$ be not both zero. Then there exists $d\in R$ such that (i) $d\mid a$ and $d\mid b$, and (ii) if $c\mid a$ and $c\mid b$ then $c\mid d$. Any two such $d$ differ by multiplication by a unit; one writes $d=\gcd(a,b)$.

In a [[algebra-rings/ufd|unique factorization domain]], write $a$ and $b$ as products of [[algebra-rings/prime-element|prime elements]] and take the product of the common primes with minimal exponents to obtain a [[algebra-rings/gcd|greatest common divisor]]. Uniqueness is up to [[algebra-rings/associated-elements|associates]], and in a UFD prime elements coincide with [[algebra-rings/irreducible-element|irreducible elements]].
