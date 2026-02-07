---
title: "Chain homotopy"
description: "A degree +1 family of maps witnessing that two chain maps differ by a boundary operator."
---

Let \(f,g:C_\bullet\to D_\bullet\) be {{< knowl id="chain-map" text="chain maps" >}} between {{< knowl id="chain-complex" text="chain complexes" >}} \((C_\bullet,d^C)\) and \((D_\bullet,d^D)\).
A **chain homotopy** from \(f\) to \(g\) is a family of \(R\)-linear maps
\[
s_n: C_n \longrightarrow D_{n+1}\qquad (n\in\mathbb Z)
\]
such that, for every \(n\),
\[
f_n - g_n \;=\; d^D_{n+1}\circ s_n \;+\; s_{n-1}\circ d^C_n.
\]
One writes \(f\simeq g\) if such an \(s\) exists.

### Key consequence
If \(f\simeq g\), then the induced maps on homology agree:
\[
H_n(f)=H_n(g)\quad\text{for all }n,
\]
where {{< knowl id="homology-module" text="homology module" >}} is used.

## Cross-links
- Special case: a **contracting homotopy** \( \mathrm{id}\simeq 0\) shows a complex is “contractible,” hence {{< knowl id="exact-complex" text="exact" >}}.
- Chain homotopy is the basic equivalence relation behind chain-homotopy categories; compare {{< knowl id="chain-map" text="chain map" >}}.

## Examples
1. **Degree-0 complexes: homotopy forces equality.**  
   If \(C_\bullet\) and \(D_\bullet\) are concentrated in degree \(0\), then any \(s_n\) must be \(0\) (there is no \(D_{1}\)), so the homotopy identity becomes \(f_0-g_0=0\). Thus \(f\simeq g\) implies \(f=g\) in this case.

2. **A contractible 2-term complex.**  
   Consider the complex \(C_\bullet\) with \(C_1=R\), \(C_0=R\), and \(d_1=\mathrm{id}_R\) (all other \(C_n=0\)). This is a chain complex since \(d_0=0\).  
   Define \(s_0:C_0\to C_1\) to be \(\mathrm{id}_R\) and all other \(s_n=0\). Then for \(n=0\),
   \[
   (\mathrm{id}-0)_{0} = d_1 s_0 + s_{-1} d_0 = \mathrm{id}\circ \mathrm{id} + 0,
   \]
   and for \(n=1\),
   \[
   (\mathrm{id}-0)_{1} = d_2 s_1 + s_0 d_1 = 0 + \mathrm{id}\circ \mathrm{id}.
   \]
   Hence \(\mathrm{id}_{C_\bullet}\simeq 0\). In particular \(H_n(C_\bullet)=0\) for all \(n\), so \(C_\bullet\) is {{< knowl id="exact-complex" text="exact" >}}.

3. **Split exact complexes admit contracting homotopies.**  
   If each short exact sequence
   \[
   0\to \operatorname{im}(d_{n+1}) \to C_n \to \operatorname{im}(d_n)\to 0
   \]
   splits (as in many algebraic settings), then one can choose splittings to build maps \(s_n:C_n\to C_{n+1}\) with \(\mathrm{id}\simeq 0\). This provides a conceptual way to recognize contractible (hence exact) complexes.
