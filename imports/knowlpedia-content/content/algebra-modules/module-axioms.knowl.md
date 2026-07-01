+++
id = "algebra-modules/module-axioms"
title = "Module axioms"
kind = "knowl"
summary = "The axioms defining a (left) module over a unital ring."
aliases = ["module-axioms", "Module axioms"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/module-axioms.md"
+++

The **module axioms** define a (left) [[algebra-modules/module|module]] \(M\) over a [[algebra-rings/unital-ring|unital ring]] \(R\) as follows. One requires:
1. \((M,+)\) is an abelian group (so \(+\) is a [[shared-foundations/binary-operation|binary operation]] with associativity, commutativity, identity \(0\), and inverses).
2. A scalar multiplication map \(R\times M\to M\), \((r,m)\mapsto rm\), satisfying for all \(r,s\in R\) and \(m,n\in M\):
   - \((r+s)m = rm + sm\),
   - \(r(m+n) = rm + rn\),
   - \((rs)m = r(sm)\),
   - \(1_R m = m\).

These axioms encode “linearity” over a [[algebra-rings/ring|ring]]; replacing \(R\) by a field yields the [[algebra-modules/vector-space-axioms|vector space axioms]].
