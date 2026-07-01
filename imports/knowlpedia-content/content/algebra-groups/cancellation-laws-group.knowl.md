+++
id = "algebra-groups/cancellation-laws-group"
title = "Cancellation laws"
kind = "knowl"
summary = "Left and right cancellation hold in every group"
aliases = ["cancellation-laws-group", "Cancellation laws"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/cancellation-laws-group.md"
+++

**Proposition (Cancellation laws).**
Let $G$ be a [[algebra-groups/group|group]] and let $a,b,c\in G$.

- (**Left cancellation**) If $ab=ac$, then $b=c$.
- (**Right cancellation**) If $ba=ca$, then $b=c$.

Equivalently, for each fixed $a\in G$, the left-translation map $L_a:G\to G$, $L_a(x)=ax$, and the right-translation map $R_a:G\to G$, $R_a(x)=xa$, are injective.

**Context.**
Cancellation is the algebraic shadow of invertibility: you "cancel" by multiplying by $a^{-1}$ on the appropriate side. Uniqueness of inverses (see [[algebra-groups/uniqueness-of-inverses-group|uniqueness of inverses]]) ensures $a^{-1}$ is well-defined.
