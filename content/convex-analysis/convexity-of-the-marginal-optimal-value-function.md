---
title: "Convexity of the Marginal (Optimal Value) Function"
description: "Under convexity of the objective and the set-valued map, the value function is convex"
---

**Convexity of the Marginal Function**: Let $X$ and $Y$ be {{< knowl id="vector-space" text="vector spaces" >}}. Assume that $\varphi:X\times Y\to\overline{\mathbb{R}}$ is a {{< knowl id="convex-function-via-epigraph" text="convex function" >}} and that $F:X\rightrightarrows Y$ is a {{< knowl id="set-valued-mapping-multifunction-domain-and-graph-convex-set-valued-mapping" text="convex set-valued mapping" >}} (i.e., its graph is convex). Define the {{< knowl id="marginal-optimal-value-function" text="marginal function" >}} $\mu$ by
$$
\mu(x)=\inf\{\varphi(x,y)\mid y\in F(x)\}.
$$
Then $\mu$ is convex on $X$.

**Context:** This result explains why optimal value functions in convex optimization are convex in parameters: convexity of $\varphi$ and convexity of the feasible graph propagate through the infimum operation.

**Proof sketch (idea):** Fix $x_1,x_2$ and choose near-minimizers $y_1\in F(x_1)$, $y_2\in F(x_2)$. By graph convexity, $\lambda y_1+(1-\lambda)y_2\in F(\lambda x_1+(1-\lambda)x_2)$. Use convexity of $\varphi$ to bound $\mu(\lambda x_1+(1-\lambda)x_2)$ by $\lambda\mu(x_1)+(1-\lambda)\mu(x_2)$ (letting the approximation error go to $0$).
