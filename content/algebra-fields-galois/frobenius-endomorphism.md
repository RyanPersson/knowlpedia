---
title: "Frobenius endomorphism"
description: "In characteristic p, the map x ↦ x^p is a ring endomorphism; on finite fields it is an automorphism."
---

Let \(F\) be a {{< knowl id="field" section="algebra-rings" text="field" >}} of {{< knowl id="characteristic" section="algebra-rings" text="characteristic" >}} \(p>0\). The **Frobenius endomorphism** of \(F\) is the map
\[
\mathrm{Fr}_F: F\to F,\qquad x\mapsto x^p.
\]
It is a ring endomorphism because in characteristic \(p\) one has \((x+y)^p=x^p+y^p\) (all intermediate binomial coefficients are divisible by \(p\)), and \((xy)^p=x^p y^p\).

If \(F\) is a {{< knowl id="finite-field" text="finite field" >}}, then \(\mathrm{Fr}_F\) is bijective (hence a {{< knowl id="field-automorphism" text="field automorphism" >}}); indeed, any injective map \(F\to F\) is automatically surjective because \(F\) is finite. More generally, in characteristic \(p\) the Frobenius is an automorphism precisely when \(F\) is {{< knowl id="perfect-field" text="perfect" >}}.

For \(F=\mathbb{F}_{q^n}\) over \(\mathbb{F}_q\), the \(q\)-power Frobenius \(x\mapsto x^q\) generates the {{< knowl id="galois-group" text="Galois group" >}} of the extension (see {{< knowl id="finite-field-galois-group-cyclic" text="finite-field Galois group is cyclic" >}}), and the fixed field of \(x\mapsto x^q\) is \(\mathbb{F}_q\) (compare {{< knowl id="fixed-field" text="fixed field" >}}).

### Examples
1. **Prime field.** On \(\mathbb{F}_p\), Frobenius is the identity map since \(a^p=a\) for all \(a\in\mathbb{F}_p\).

2. **\(\mathbb{F}_4\).** In \(\mathbb{F}_4=\mathbb{F}_2(\alpha)\) with \(\alpha^2=\alpha+1\), the Frobenius is \(x\mapsto x^2\). It satisfies \(\alpha\mapsto \alpha^2=\alpha+1\) and \(\alpha+1\mapsto (\alpha+1)^2=\alpha\), so it is a nontrivial automorphism of order \(2\).

3. **A non-surjective Frobenius (imperfect field).** Let \(F=\mathbb{F}_p(t)\), the rational function field. Then Frobenius sends \(t\mapsto t^p\), so \(t\) is not a \(p\)th power in \(F\); hence Frobenius is not surjective and not an automorphism.
