+++
id = "algebra-groups/quotient-group-universal-property"
title = "Universal Property of Quotient Groups"
kind = "knowl"
summary = "Homomorphisms out of G that kill N factor uniquely through G/N"
aliases = ["quotient-group-universal-property", "Universal Property of Quotient Groups"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/quotient-group-universal-property.md"
+++

**Universal Property of Quotient Groups**: Let $G$ be a [[algebra-groups/group|group]] and let $N\trianglelefteq G$ be a [[algebra-groups/normal-subgroup|normal subgroup]]. Let $\pi:G\to G/N$ be the canonical projection to the [[algebra-groups/quotient-group|quotient group]]. If $K$ is a group and $f:G\to K$ is a [[algebra-groups/group-homomorphism|group homomorphism]] such that $N\subseteq \ker(f)$ (where $\ker(f)$ is the [[algebra-groups/kernel-group|kernel]] of $f$), then there exists a unique homomorphism $\bar f:G/N\to K$ with
$
f = \bar f \circ \pi.
$

Equivalently: giving a homomorphism $G/N\to K$ is the same as giving a homomorphism $G\to K$ that sends every element of $N$ to the identity of $K$.
