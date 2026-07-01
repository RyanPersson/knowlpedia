+++
id = "real-analysis/class-ck-function"
title = "Class C^k function"
kind = "knowl"
summary = "A function with continuous derivatives up to order k."
aliases = ["class-ck-function", "Class C^k function"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/class-ck-function.md"
+++

A **class $C^k$ function** on an interval $I$ is a [[shared-foundations/function|function]] $f:I\to\mathbb{R}$ such that $f^{(j)}$ exists on $I$ and is continuous for every integer $0\le j\le k$ (with $f^{(0)}=f$); it is class $C^\infty$ if this holds for all $k$.

This definition is built from [[real-analysis/higher-derivatives|higher derivatives]] together with continuity (viewed generally as a [[topology/continuous-map|continuous map]] property). In several variables, the analogous notion is a [[real-analysis/class-ck-map|class C^k map]].

**Examples:**
- Every [[real-analysis/polynomial|polynomial]] function is class $C^\infty$ on $\mathbb{R}$.
- The function $f(x)=|x|$ is class $C^0$ on $\mathbb{R}$ but not class $C^1$.
