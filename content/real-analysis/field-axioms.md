---
title: "Field axioms"
description: "Axioms for addition and multiplication in a field, as used for the real numbers."
---

**Field axioms:** Let $F$ be a {{< knowl id="set" section="shared-foundations" text="set" >}} equipped with binary operations $+$ and $\cdot$ and distinguished elements $0,1\in F$ with $0\neq 1$. The following are required for all $a,b,c\in F$:

- (Additive associativity) $(a+b)+c=a+(b+c)$.
- (Additive commutativity) $a+b=b+a$.
- (Additive identity) $a+0=a$.
- (Additive inverse) there exists $-a\in F$ such that $a+(-a)=0$.
- (Multiplicative associativity) $(ab)c=a(bc)$.
- (Multiplicative commutativity) $ab=ba$.
- (Multiplicative identity) $a1=a$.
- (Multiplicative inverse) if $a\neq 0$ then there exists $a^{-1}\in F$ such that $aa^{-1}=1$.
- (Distributivity) $a(b+c)=ab+ac$.

These axioms say exactly that $F$ is a {{< knowl id="field" section="algebra-rings" text="field" >}} (equivalently, a commutative {{< knowl id="ring" section="algebra-rings" text="ring" >}} in which every nonzero element is invertible). Together with the {{< knowl id="order-axioms" text="order axioms" >}} and the {{< knowl id="completeness-axiom" text="completeness axiom" >}}, they characterize the real number system up to isomorphism.
