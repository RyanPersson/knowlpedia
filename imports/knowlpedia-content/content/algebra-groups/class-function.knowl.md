+++
id = "algebra-groups/class-function"
title = "Class function"
kind = "knowl"
summary = "A function on a group that is constant on conjugacy classes"
aliases = ["class-function", "Class function"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/class-function.md"
+++

Let $G$ be a [[algebra-groups/group|group]] and let $A$ be a set. A **class function** on $G$ with values in $A$ is a [[shared-foundations/function|function]] $f\colon G\to A$ such that for all $x,g\in G$,
$
f(xgx^{-1})=f(g).
$
Equivalently, $f$ is constant on each [[algebra-groups/conjugacy-class|conjugacy class]] of $G$.

Class functions are precisely the functions invariant under the [[algebra-groups/conjugation-action|conjugation action]] of $G$ on itself. In representation theory, the [[algebra-representation-theory/character|character]] of a finite-dimensional complex representation is a fundamental example of a class function.

**Examples:**
- Any constant function $f(g)=a$ is a class function.
- Fix a conjugacy class $C\subseteq G$. The indicator function $1_C\colon G\to\{0,1\}$ defined by $1_C(g)=1$ if $g\in C$ and $0$ otherwise is a class function.
- In $S_n$, the sign map $\mathrm{sgn}\colon S_n\to\{\pm1\}$ is a class function (it depends only on the cycle type, hence is constant on conjugacy classes).
