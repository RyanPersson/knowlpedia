+++
id = "algebra-homological/ext-tor-derived-functors"
title = "Ext and Tor as derived functors"
kind = "knowl"
summary = "Ext and Tor are the right/left derived functors of Hom and tensor, computed via injective/projective (or flat) resolutions."
aliases = ["ext-tor-derived-functors", "Ext and Tor as derived functors"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/ext-tor-derived-functors.md"
+++

Let \(R\) be a ring and \(M,N\) \(R\)-modules. The functors
- \(N \mapsto \operatorname{Hom}_R(M,N)\) (covariant in \(N\)) are [[algebra-homological/hom-left-exact|left exact]],
- \(M \mapsto M\otimes_R N\) are [[algebra-homological/tensor-right-exact|right exact]].

Their failure to be exact is measured by derived functors, giving rise to [[algebra-homological/ext|Ext]] and [[algebra-homological/tor|Tor]].

## Definitions (via resolutions)

### Ext as a right derived functor
Fix \(M\). Choose an [[algebra-homological/injective-resolution|injective resolution]] \(0\to N\to I^0\to I^1\to \cdots\).
Apply \(\operatorname{Hom}_R(M,-)\) degreewise to get a cochain complex \(\operatorname{Hom}_R(M,I^\bullet)\).
Define
\[
\operatorname{Ext}^n_R(M,N) := H^n(\operatorname{Hom}_R(M,I^\bullet)).
\]
Equivalently (often more computationally), choose a [[algebra-homological/projective-resolution|projective resolution]] \( \cdots \to P_1\to P_0\to M\to 0\) and set
\[
\operatorname{Ext}^n_R(M,N) := H^n(\operatorname{Hom}_R(P_\bullet,N)).
\]
These agree and are well-defined up to canonical isomorphism because projective/injective resolutions exist (see [[algebra-homological/projective-resolutions-exist|projective resolutions exist]] and [[algebra-homological/injective-resolutions-exist|injective resolutions exist]]).

### Tor as a left derived functor
Fix \(N\). Choose a projective (or flat) resolution \( \cdots \to P_1\to P_0\to M\to 0\).
Apply \(-\otimes_R N\) to get a chain complex \(P_\bullet\otimes_R N\).
Define
\[
\operatorname{Tor}^R_n(M,N) := H_n(P_\bullet\otimes_R N).
\]

## Functorial consequences
- Short exact sequences induce long exact sequences of derived functors (see [[algebra-homological/long-exact-sequence-derived|long exact sequence of derived functors]], [[algebra-homological/long-exact-sequence-ext|for Ext]], [[algebra-homological/long-exact-sequence-tor|for Tor]]).
- \(\operatorname{Ext}^1\) classifies extensions (see [[algebra-homological/ext1-classifies-extensions|Ext\(^1\) classifies extensions]]).

## Examples

### Example 1 (Tor over \(\mathbb Z\): \(\operatorname{Tor}_1^\mathbb Z(\mathbb Z/n,\mathbb Z/m)\))
Use the standard projective resolution
\[
0\to \mathbb Z \xrightarrow{\cdot n} \mathbb Z \to \mathbb Z/n\to 0.
\]
Tensor with \(\mathbb Z/m\) to get
\[
0\to \mathbb Z/m \xrightarrow{\cdot n} \mathbb Z/m \to (\mathbb Z/n)\otimes(\mathbb Z/m)\to 0.
\]
Then
\[
\operatorname{Tor}_1^\mathbb Z(\mathbb Z/n,\mathbb Z/m)=\ker(\cdot n:\mathbb Z/m\to \mathbb Z/m)\cong \mathbb Z/\gcd(n,m),
\]
and \(\operatorname{Tor}_i=0\) for \(i\ge 2\) because the resolution has length \(1\).

### Example 2 (Ext over \(\mathbb Z\): \(\operatorname{Ext}^1_\mathbb Z(\mathbb Z/n,\mathbb Z/m)\))
Apply \(\operatorname{Hom}_\mathbb Z(-,\mathbb Z/m)\) to the same resolution:
\[
0\to \mathbb Z \xrightarrow{\cdot n} \mathbb Z \to \mathbb Z/n\to 0
\]
to obtain
\[
0\to \operatorname{Hom}(\mathbb Z,\mathbb Z/m)\xrightarrow{\cdot n}\operatorname{Hom}(\mathbb Z,\mathbb Z/m)\to \operatorname{Ext}^1(\mathbb Z/n,\mathbb Z/m)\to 0.
\]
Since \(\operatorname{Hom}(\mathbb Z,\mathbb Z/m)\cong \mathbb Z/m\), we get
\[
\operatorname{Ext}^1_\mathbb Z(\mathbb Z/n,\mathbb Z/m)\cong (\mathbb Z/m)/n(\mathbb Z/m)\cong \mathbb Z/\gcd(n,m),
\]
and \(\operatorname{Ext}^i=0\) for \(i\ge 2\).

### Example 3 (a quick vanishing test: projective/flat inputs)
If \(M\) is [[algebra-modules/projective-module|projective]], then \(\operatorname{Ext}^n_R(M,N)=0\) for all \(n\ge 1\) and all \(N\).
If \(N\) is [[algebra-modules/flat-module|flat]], then \(\operatorname{Tor}^R_n(M,N)=0\) for all \(n\ge 1\) and all \(M\).
Both statements follow because you can take a resolution of length \(0\) (exactness of the relevant functor), reflecting the general principle that derived functors measure failure of exactness (see [[algebra-homological/hom-tensor-exactness|Hom/tensor exactness]]).
