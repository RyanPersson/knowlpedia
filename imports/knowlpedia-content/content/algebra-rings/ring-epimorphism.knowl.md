+++
id = "algebra-rings/ring-epimorphism"
title = "Ring epimorphism"
kind = "knowl"
summary = "A surjective ring homomorphism."
aliases = ["ring-epimorphism", "Ring epimorphism"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ring-epimorphism.md"
+++

A **ring epimorphism** is a [[algebra-rings/ring-homomorphism|ring homomorphism]] $\varphi:R\to S$ that is [[shared-foundations/surjective-function|surjective]] as a function.

Epimorphisms present $S$ as a quotient of $R$; the basic example is the natural projection onto a [[algebra-rings/quotient-ring|quotient ring]]. They are the appropriate maps for “presenting” rings by generators and relations.

**Examples:**
- The quotient map $R\to R/I$, $r\mapsto r+I$, is a ring epimorphism.
- The evaluation map $k[x]\to k$, $f\mapsto f(c)$, is surjective for any field $k$ and $c\in k$.
- The inclusion $\mathbb Z\hookrightarrow \mathbb Q$ is not an epimorphism (not surjective).
