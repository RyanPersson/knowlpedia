+++
id = "algebra-groups/conjugacy-class"
title = "Conjugacy class"
kind = "knowl"
summary = "The set of all conjugates of a given group element"
aliases = ["conjugacy-class", "Conjugacy class"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/conjugacy-class.md"
+++

Let $G$ be a [[algebra-groups/group|group]] and let $g\in G$. The **conjugacy class of $g$ in $G$** is the subset
$
\mathrm{Cl}_G(g)=\{xgx^{-1} : x\in G\}.
$
Equivalently, $\mathrm{Cl}_G(g)$ is the set of all [[algebra-groups/conjugate-element|conjugates]] of $g$.

Conjugacy classes are exactly the orbits of the [[algebra-groups/conjugation-action|conjugation action]] of $G$ on itself, so they form a [[shared-foundations/partition|partition]] of $G$. An element lies in the [[algebra-groups/center-of-group|center]] of $G$ if and only if its conjugacy class is a singleton. The sizes of conjugacy classes feature prominently in the [[algebra-groups/class-equation|class equation]].

**Examples:**
- In $S_3$, the conjugacy classes are $\{e\}$, the three transpositions $\{(12),(13),(23)\}$, and the two $3$-cycles $\{(123),(132)\}$.
- If $G$ is abelian, then $\mathrm{Cl}_G(g)=\{g\}$ for every $g\in G$.
- In $D_8=\langle r,s\mid r^4=s^2=e,\ srs=r^{-1}\rangle$, one has $\mathrm{Cl}_{D_8}(r)=\{r,r^{-1}\}=\{r,r^3\}$, so conjugacy classes need not be singletons in nonabelian groups.
