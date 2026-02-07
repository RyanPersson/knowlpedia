---
title: "Basic forms theorem"
description: "Characterizes which differential forms on a principal bundle descend to the base manifold."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle with right action \(R_g:P\to P\). A differential form \(\alpha \in \Omega^k(P)\) is called **basic** if it satisfies:

1. **\(G\)-invariance:**
   $$
   R_g^*\alpha = \alpha \quad \text{for all } g\in G.
   $$
2. **Horizontality:** for every \(X\in \mathfrak{g}\), letting \(X^\#\) denote the corresponding fundamental vertical vector field on \(P\),
   $$
   \iota_{X^\#}\alpha = 0.
   $$

### Theorem (basic forms theorem)
A form \(\alpha \in \Omega^k(P)\) is basic **if and only if** there exists a unique form \(\beta \in \Omega^k(M)\) such that
$$
\pi^*\beta = \alpha.
$$
In other words, basic forms are exactly those that "descend" from \(P\) to the base \(M\).

### Why the conditions are exactly right (proof idea)
- If \(\alpha=\pi^*\beta\), then \(\alpha\) is automatically \(G\)-invariant because \(\pi\circ R_g=\pi\), and \(\alpha\) is horizontal because \(\pi_*(X^\#)=0\) for vertical vectors.
- Conversely, if \(\alpha\) is horizontal and invariant, choose a local section \(s:U\to P\) and define \(\beta_U := s^*\alpha\). On overlaps \(U\cap V\), two sections differ by a gauge transformation \(s_V = s_U \cdot g\) for a map \(g:U\cap V\to G\). Invariance and horizontality imply \(s_U^*\alpha = s_V^*\alpha\), so the \(\beta_U\) glue to a global \(\beta\) with \(\pi^*\beta=\alpha\).

### Example: characteristic forms
If \(\omega\) is a connection on \(P\) with curvature \(\Omega\), then applying an \(\mathrm{Ad}\)-invariant polynomial \(P\) on \(\mathfrak{g}\) produces a real-valued form \(P(\Omega)\) that is horizontal and \(G\)-invariant, hence basic, so it descends to \(M\). Its closedness is proved using the {{< knowl id="bianchi-identity" text="Bianchi identity" >}}.
