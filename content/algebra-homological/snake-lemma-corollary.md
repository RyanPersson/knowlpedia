---
title: "Snake lemma corollary: long exact sequence in homology"
description: "A short exact sequence of chain complexes induces a natural long exact sequence in homology."
---

## Statement
Let
\[
0 \longrightarrow A_\bullet \longrightarrow B_\bullet \longrightarrow C_\bullet \longrightarrow 0
\]
be a **short exact sequence** of {{< knowl id="chain-complex" text="chain complexes" >}}, meaning that for each \(n\) the sequence
\[
0 \to A_n \to B_n \to C_n \to 0
\]
is exact in the sense of {{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequences of modules" >}}, and all differentials commute with the structure maps.

Then there are **connecting homomorphisms**
\[
\delta_n : H_n(C_\bullet) \longrightarrow H_{n-1}(A_\bullet)
\]
such that the sequence of {{< knowl id="homology-module" text="homology modules" >}}
\[
\cdots \to H_n(A_\bullet) \to H_n(B_\bullet) \to H_n(C_\bullet)
\xrightarrow{\ \delta_n\ } H_{n-1}(A_\bullet) \to H_{n-1}(B_\bullet) \to \cdots
\]
is exact.

This long exact sequence is **natural** in morphisms of short exact sequences of complexes. The maps \(\delta_n\) are constructed by a standard diagram chase and can be viewed as arising from the {{< knowl id="snake-lemma" text="snake lemma" >}}; see also {{< knowl id="connecting-homomorphism-lemma" text="connecting homomorphisms" >}}.

## Examples

### Example 1: Complexes concentrated in degree \(0\)
If \(A_\bullet,B_\bullet,C_\bullet\) are concentrated in degree \(0\), then \(H_0(A_\bullet)=A_0\), \(H_0(B_\bullet)=B_0\), \(H_0(C_\bullet)=C_0\) and \(H_n(-)=0\) for \(n\ge 1\). The long exact sequence collapses to
\[
0 \to A_0 \to B_0 \to C_0 \to 0,
\]
i.e. it recovers the original short exact sequence of modules.

### Example 2: A nontrivial connecting map \(\delta_1\) detecting reduction mod \(n\)
Fix \(n\ge 2\). Define complexes (nonzero only in degrees \(1,0\)):

- \(A_\bullet\): \(A_1=\mathbb Z \xrightarrow{d_1=\cdot n} A_0=\mathbb Z\).
- \(B_\bullet\): \(B_1=\mathbb Z\oplus \mathbb Z \xrightarrow{d_1(x,y)=nx+y} B_0=\mathbb Z\).
- \(C_\bullet\): \(C_1=\mathbb Z \to C_0=0\) (so \(d_1=0\)).

Define maps \(A_\bullet \to B_\bullet\) by
\[
A_1\to B_1,\ x\mapsto (x,0), \qquad A_0\to B_0,\ x\mapsto x,
\]
and \(B_\bullet\to C_\bullet\) by
\[
B_1\to C_1,\ (x,y)\mapsto y,\qquad B_0\to C_0,\ z\mapsto 0.
\]
Then \(0\to A_\bullet\to B_\bullet\to C_\bullet\to 0\) is short exact degreewise.

Compute homology:
- \(H_1(A_\bullet)=0\), \(H_0(A_\bullet)\cong \mathbb Z/n\mathbb Z\).
- \(H_1(C_\bullet)\cong \mathbb Z\), \(H_0(C_\bullet)=0\).
- \(H_1(B_\bullet)=\ker(d_1)=\{(x,-nx)\}\cong\mathbb Z\), and \(H_0(B_\bullet)=0\) (since \(d_1(0,1)=1\)).

The relevant part of the long exact sequence is
\[
H_1(B_\bullet)\to H_1(C_\bullet)\xrightarrow{\delta_1} H_0(A_\bullet)\to H_0(B_\bullet)=0.
\]
Under the identifications above, the map \(H_1(B_\bullet)\to H_1(C_\bullet)\) is multiplication by \(n\), hence its image is \(n\mathbb Z\). Exactness forces
\[
\ker(\delta_1)=n\mathbb Z,
\]
so \(\delta_1:\mathbb Z\to \mathbb Z/n\mathbb Z\) is precisely reduction mod \(n\).

### Example 3: Split short exact sequences give \(\delta_n=0\)
If the short exact sequence of complexes splits degreewise (e.g. \(B_\bullet \cong A_\bullet \oplus C_\bullet\) as complexes), then the induced sequence in homology splits and all connecting maps \(\delta_n\) are zero.
