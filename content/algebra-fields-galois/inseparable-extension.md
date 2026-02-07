---
title: "Inseparable extension"
description: "An algebraic extension that is not separable; it contains an element with a repeated-root minimal polynomial."
---

Let \(K/F\) be an algebraic {{< knowl id="field-extension" text="field extension" >}}.

**Definition (inseparable extension).** The extension \(K/F\) is *inseparable* if it is not a {{< knowl id="separable-extension" text="separable extension" >}}; equivalently, there exists \(\alpha\in K\) whose minimal polynomial over \(F\) is not separable (has a repeated root in a splitting field). This can only occur when the {{< knowl id="characteristic" section="algebra-rings" text="characteristic" >}} of \(F\) is \(p>0\).

A particularly important special case is:

**Definition (purely inseparable).** Assume \(\mathrm{char}(F)=p>0\). The extension \(K/F\) is *purely inseparable* if for every \(\alpha\in K\) there exists \(n\ge 0\) such that
\[
\alpha^{p^n}\in F.
\]
Equivalently, every \(\alpha\in K\) is a root of a polynomial of the form \(x^{p^n}-a\) with \(a\in F\), whose derivative is \(0\), so no such element is {{< knowl id="separable-element" text="separable" >}} unless \(\alpha\in F\).

**Examples.**
1. \(K=\mathbb{F}_p(t^{1/p})\) over \(F=\mathbb{F}_p(t)\) is purely inseparable since \((t^{1/p})^p=t\in F\). The minimal polynomial \(x^p-t\) has a repeated root.
2. More generally, \(\mathbb{F}_p(t^{1/p^n})/\mathbb{F}_p(t)\) is purely inseparable of degree \(p^n\), with \((t^{1/p^n})^{p^n}=t\).
3. If \(F\) is an imperfect field of characteristic \(p\) (i.e. not {{< knowl id="perfect-field" text="perfect" >}}), then choosing \(a\in F\setminus F^p\) produces an inseparable extension \(F(a^{1/p})/F\).
