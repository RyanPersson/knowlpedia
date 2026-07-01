+++
id = "convex-analysis/linear-combination"
title = "Linear combination"
kind = "knowl"
summary = "A finite sum of scalar multiples of vectors"
aliases = ["linear-combination", "Linear combination"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/linear-combination.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] over a field $K$. Given vectors $x_1,\dots,x_m\in X$ and scalars $\alpha_1,\dots,\alpha_m\in K$, a **linear combination** of $x_1,\dots,x_m$ is any vector of the form
$$
\alpha_1x_1+\cdots+\alpha_m x_m=\sum_{i=1}^m \alpha_i x_i.
$$
Only **finite** sums are allowed in this definition.

Linear combinations are the basic algebraic operation behind the [[convex-analysis/subspace-generated-by-a-set-span|span]], and a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] is precisely a set that generates every vector via a unique linear combination.

**Examples:**
- In $\mathbb{R}^2$, the vector $(3,1)$ is a linear combination of $(1,0)$ and $(0,1)$ via $(3,1)=3(1,0)+1(0,1)$.
- In the polynomial space $P$, the polynomial $2+5t-t^3$ is a linear combination of $1,t,t^3$ with coefficients $2,5,-1$.
- If $f,g\in F(\Omega)$, then $\alpha f+\beta g$ is the function $x\mapsto \alpha f(x)+\beta g(x)$.
