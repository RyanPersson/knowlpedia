---
title: "Holonomy representation"
description: "For a flat connection, the induced representation of the fundamental group into the structure group via parallel transport."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle with a {{< knowl id="flat-principal-connection" text="flat principal connection" >}}. Fix a basepoint \(x\in M\) and \(p\in P_x\).

For a loop \(\gamma\) based at \(x\), let \(g_\gamma\in G\) be the element determined by horizontal lifting as in the definition of the {{< knowl id="holonomy-group" text="holonomy group" >}}:
\[
\widetilde\gamma(1)=p\cdot g_\gamma.
\]
Flatness implies \(g_\gamma\) depends only on the homotopy class \([\gamma]\in \pi_1(M,x)\), and the assignment
\[
\rho_p:\pi_1(M,x)\longrightarrow  G,\qquad \rho_p([\gamma])\coloneqq g_\gamma
\]
is a group homomorphism. This homomorphism is the **holonomy representation** (also called the monodromy representation) of the flat connection based at \(p\).

If one replaces \(p\) by \(p\cdot h\) for \(h\in G\), then \(\rho_{p\cdot h}=h^{-1}\rho_p\,h\); thus the holonomy representation is well-defined up to conjugation in \(G\). Conversely, a representation \(\rho:\pi_1(M,x)\to G\) determines a flat principal bundle (and flat connection) via the standard \((\widetilde M\times G)/\pi_1\) construction.

## Examples
1. **Circle with \(U(1)\)-monodromy.** Flat principal \(U(1)\)-bundles over \(S^1\) are classified by a single element \(e^{i\theta}\in U(1)\); the representation sends the generator of \(\pi_1(S^1)\cong \mathbb{Z}\) to \(e^{i\theta}\), and sends \(n\mapsto e^{in\theta}\).

2. **Trivial flat connection.** On \(M\times G\) with the product flat connection, horizontal lifts return to the same point in the fiber for every loop, so \(\rho_p\) is the trivial homomorphism.

3. **Constructing a flat bundle from a representation.** Given any \(\rho:\pi_1(M,x)\to G\), the quotient \(P=(\widetilde M\times G)/\pi_1(M)\) with the \(\pi_1\)-action twisted by \(\rho\) has a canonical flat connection whose holonomy representation is \(\rho\) (up to conjugacy).
