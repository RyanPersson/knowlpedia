---
title: "Existence and uniqueness of finite fields"
description: "For each prime power q=p^n there is a unique (up to isomorphism) field with q elements."
---

A {{< knowl id="finite-field" text="finite field" >}} is a field with finitely many elements.

**Theorem (Existence and uniqueness).** Let \(q=p^n\) where \(p\) is prime and \(n\ge1\).
1. (**Existence**) There exists a field \(\mathbb{F}_q\) with exactly \(q\) elements. It has {{< knowl id="characteristic" section="algebra-rings" text="characteristic" >}} \(p\).
2. (**Uniqueness**) Any two fields with \(q\) elements are isomorphic (so \(\mathbb{F}_q\) is well-defined up to unique isomorphism).

A concrete construction is:
- Start with \(\mathbb{F}_p\).
- Choose an irreducible polynomial \(f(x)\in \mathbb{F}_p[x]\) of degree \(n\).
- Form the quotient \(\mathbb{F}_p[x]/(f)\), which is a field of size \(p^n\).

Uniqueness can be seen by noting that every field with \(q\) elements is the {{< knowl id="splitting-field" text="splitting field" >}} of \(x^q-x\) over \(\mathbb{F}_p\), and splitting fields are unique up to \(\mathbb{F}_p\)-isomorphism.

### Examples
1. \(q=p\). Then \(\mathbb{F}_p\cong \mathbb{Z}/p\mathbb{Z}\) is the unique field of order \(p\).

2. \(q=4=2^2\). Take \(f(x)=x^2+x+1\in\mathbb{F}_2[x]\), which has no root in \(\mathbb{F}_2\) and hence is irreducible.  
   Then \(\mathbb{F}_4\cong \mathbb{F}_2[x]/(x^2+x+1)\).

3. \(q=9=3^2\). The polynomial \(f(x)=x^2+1\in\mathbb{F}_3[x]\) has no root in \(\mathbb{F}_3\) (since \(0^2+1=1\), \(1^2+1=2\), \(2^2+1=2\)), so it is irreducible.  
   Then \(\mathbb{F}_9\cong \mathbb{F}_3[x]/(x^2+1)\).
