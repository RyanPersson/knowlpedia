---
title: "Group Presentation"
description: "A description of a group by generators and relations"
---

A **group presentation** is a way to specify a {{< knowl id="group" text="group" >}} by choosing a {{< knowl id="generating-set" text="generating set" >}} $S$ and a set of relations $R$ among those generators. Formally, the presentation
$$
\langle S \mid R\rangle
$$
denotes the quotient of the {{< knowl id="free-group" text="free group" >}} $F(S)$ by the {{< knowl id="normal-closure" text="normal closure" >}} of the relations:
$$
\langle S \mid R\rangle \;:=\; F(S)\big/\!\langle\!\langle R\rangle\!\rangle,
$$
a {{< knowl id="quotient-group" text="quotient group" >}}. Intuitively, one starts with all formal words in $S$ and forces the relations in $R$ to hold.

Presentations are ubiquitous: they encode groups by finitely many symbols when possible, and many structural questions reduce to understanding the relations.

**Examples:**
- The cyclic group of order $n$ has presentation $\langle a \mid a^n = e\rangle$.
- The free abelian group of rank $2$ has presentation $\langle a,b \mid ab=ba\rangle$.
- The dihedral group $D_{2n}$ has presentation $\langle r,s \mid r^n=e,\ s^2=e,\ srs^{-1}=r^{-1}\rangle$.
