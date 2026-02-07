---
title: "Class function"
description: "A function on a group that is constant on conjugacy classes"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $A$ be a set. A **class function** on $G$ with values in $A$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f\colon G\to A$ such that for all $x,g\in G$,
$
f(xgx^{-1})=f(g).
$
Equivalently, $f$ is constant on each {{< knowl id="conjugacy-class" text="conjugacy class" >}} of $G$.

Class functions are precisely the functions invariant under the {{< knowl id="conjugation-action" text="conjugation action" >}} of $G$ on itself. In representation theory, the {{< knowl id="character" section="algebra-representation-theory" text="character" >}} of a finite-dimensional complex representation is a fundamental example of a class function.

**Examples:**
- Any constant function $f(g)=a$ is a class function.
- Fix a conjugacy class $C\subseteq G$. The indicator function $1_C\colon G\to\{0,1\}$ defined by $1_C(g)=1$ if $g\in C$ and $0$ otherwise is a class function.
- In $S_n$, the sign map $\mathrm{sgn}\colon S_n\to\{\pm1\}$ is a class function (it depends only on the cycle type, hence is constant on conjugacy classes).
