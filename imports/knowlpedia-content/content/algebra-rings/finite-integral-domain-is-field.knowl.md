+++
id = "algebra-rings/finite-integral-domain-is-field"
title = "Finite integral domains are fields"
kind = "knowl"
summary = "A finite integral domain has multiplicative inverses for all nonzero elements."
aliases = ["finite-integral-domain-is-field", "Finite integral domains are fields"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/finite-integral-domain-is-field.md"
+++

**Finite integral domains are fields**: If $D$ is a finite integral domain, then $D$ is a field.

Using [[algebra-rings/cancellation-integral-domain|cancellation]] in an [[algebra-rings/integral-domain|integral domain]], the map $x\mapsto ax$ is injective for $a\neq 0$; finiteness forces it to be surjective, so $a$ is a [[algebra-rings/unit|unit]]. Hence every nonzero element is invertible and the ring is a [[algebra-rings/field|field]].
