---
title: "Class C^k function"
description: "A function with continuous derivatives up to order k."
---

A **class $C^k$ function** on an interval $I$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:I\to\mathbb{R}$ such that $f^{(j)}$ exists on $I$ and is continuous for every integer $0\le j\le k$ (with $f^{(0)}=f$); it is class $C^\infty$ if this holds for all $k$.

This definition is built from {{< knowl id="higher-derivatives" text="higher derivatives" >}} together with continuity (viewed generally as a {{< knowl id="continuous-map" section="topology" text="continuous map" >}} property). In several variables, the analogous notion is a {{< knowl id="class-ck-map" text="class C^k map" >}}.

**Examples:**
- Every {{< knowl id="polynomial" text="polynomial" >}} function is class $C^\infty$ on $\mathbb{R}$.
- The function $f(x)=|x|$ is class $C^0$ on $\mathbb{R}$ but not class $C^1$.
