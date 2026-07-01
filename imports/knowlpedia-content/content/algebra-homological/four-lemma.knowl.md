+++
id = "algebra-homological/four-lemma"
title = "Four lemma"
kind = "knowl"
summary = "Diagram-chase criteria ensuring the middle map in a morphism of exact sequences is injective or surjective."
aliases = ["four-lemma", "Four lemma"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/four-lemma.md"
+++

The four lemma is a pair of related statements about a commutative diagram of exact sequences. It is weaker than the [[algebra-homological/five-lemma|five lemma]] (it gives injectivity or surjectivity, not necessarily an isomorphism), and it is often proved by diagram chasing using ideas similar to the [[algebra-homological/snake-lemma|snake lemma]].

In categorical language, “injective/surjective” correspond to [[algebra-category-theory/monomorphism-category|monomorphisms]] and [[algebra-category-theory/epimorphism-category|epimorphisms]].

## Theorem (Four lemma: injective and surjective forms)

Let
\[
\begin{array}{ccccccccc}
A_1 &\to& A_2 &\to& A_3 &\to& A_4 &\to& A_5\\
\downarrow f_1 && \downarrow f_2 && \downarrow f_3 && \downarrow f_4 && \downarrow f_5\\
B_1 &\to& B_2 &\to& B_3 &\to& B_4 &\to& B_5
\end{array}
\]
be a commutative diagram of \(R\)-modules with exact rows.

### (1) Injective form
If \(f_1\) is surjective and \(f_2\) and \(f_4\) are injective, then \(f_3\) is injective.

### (2) Surjective form
If \(f_2\) and \(f_4\) are surjective and \(f_5\) is injective, then \(f_3\) is surjective.

Combining (1) and (2) (under the usual extra hypotheses that make the “remaining” injective/surjective conditions automatic) yields the [[algebra-homological/five-lemma|five lemma]].

## Examples

1. **Injectivity in the middle when the ends are \(0\).**
   In many applications (e.g. long exact sequences), one works with a 5-term exact piece
   \[
   0\to A_2\to A_3\to A_4\to 0
   \]
   and similarly for the \(B_i\). Then \(f_1:0\to 0\) is automatically surjective and \(f_5:0\to 0\) is automatically injective.
   The injective form reduces to: if \(f_2\) and \(f_4\) are injective, then \(f_3\) is injective.
   The surjective form reduces to: if \(f_2\) and \(f_4\) are surjective, then \(f_3\) is surjective.

2. **Propagation of injectivity/surjectivity through long exact Tor or Ext sequences.**
   Naturality gives morphisms between long exact sequences such as the [[algebra-homological/long-exact-sequence-tor|long exact Tor sequence]] or [[algebra-homological/long-exact-sequence-ext|long exact Ext sequence]].
   Applying the four lemma to a 5-term window inside these long exact sequences is a standard way to conclude:
   - a map on a “middle” \(\operatorname{Tor}_n\) or \(\operatorname{Ext}^n\) group is injective, provided the adjacent maps satisfy the injective-form hypotheses;
   - or surjective, provided the adjacent maps satisfy the surjective-form hypotheses.

3. **Homology of chain complexes: injectivity/surjectivity at one degree.**
   Given a morphism between long exact homology sequences arising from a short exact sequence of [[algebra-homological/chain-complex|chain complexes]], the four lemma lets one conclude that the induced map
   \[
   H_n(C_\bullet)\to H_n(D_\bullet)
   \]
   is injective (or surjective) from corresponding injectivity/surjectivity information at neighboring degrees—often a step in proving the full isomorphism statement later via the [[algebra-homological/five-lemma|five lemma]].
