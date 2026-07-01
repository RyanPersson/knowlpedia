+++
id = "real-analysis/field-axioms"
title = "Field axioms"
kind = "knowl"
summary = "Axioms for addition and multiplication in a field, as used for the real numbers."
aliases = ["field-axioms", "Field axioms"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/field-axioms.md"
+++

**Field axioms:** Let $F$ be a [[shared-foundations/set|set]] equipped with binary operations $+$ and $\cdot$ and distinguished elements $0,1\in F$ with $0\neq 1$. The following are required for all $a,b,c\in F$:

- (Additive associativity) $(a+b)+c=a+(b+c)$.
- (Additive commutativity) $a+b=b+a$.
- (Additive identity) $a+0=a$.
- (Additive inverse) there exists $-a\in F$ such that $a+(-a)=0$.
- (Multiplicative associativity) $(ab)c=a(bc)$.
- (Multiplicative commutativity) $ab=ba$.
- (Multiplicative identity) $a1=a$.
- (Multiplicative inverse) if $a\neq 0$ then there exists $a^{-1}\in F$ such that $aa^{-1}=1$.
- (Distributivity) $a(b+c)=ab+ac$.

These axioms say exactly that $F$ is a [[algebra-rings/field|field]] (equivalently, a commutative [[algebra-rings/ring|ring]] in which every nonzero element is invertible). Together with the [[real-analysis/order-axioms|order axioms]] and the [[real-analysis/completeness-axiom|completeness axiom]], they characterize the real number system up to isomorphism.
