---
title: "Seminorm"
description: "A subadditive, absolutely homogeneous function p(λx)=|λ|p(x)."
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}} over $\mathbb{R}$ or $\mathbb{C}$. A function $p:X\to\mathbb{R}$ is called a **seminorm** if:

1. (**Subadditivity**) $p(x+y)\le p(x)+p(y)$ for all $x,y\in X$.
2. (**Absolute homogeneity**) $p(\lambda x)=|\lambda|\,p(x)$ for all $x\in X$ and all scalars $\lambda$.

Every {{< knowl id="norm-normed-vector-space" text="norm" >}} is a seminorm, but a seminorm may vanish on nonzero vectors (e.g., $p(x_1,x_2)=|x_1|$ on $\mathbb{R}^2$).

Seminorms are the natural domination bounds in the seminorm versions of Hahn–Banach, including {{< knowl id="hahn-banach-extension-dominated-by-a-seminorm-real-case" text="the real seminorm Hahn–Banach theorem" >}} and {{< knowl id="hahn-banach-theorem-in-complex-vector-spaces" text="the complex seminorm Hahn–Banach theorem" >}}.
