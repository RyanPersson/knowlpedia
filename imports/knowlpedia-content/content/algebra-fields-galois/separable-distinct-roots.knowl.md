+++
id = "algebra-fields-galois/separable-distinct-roots"
title = "Separable polynomials have distinct roots"
kind = "knowl"
summary = "A polynomial is separable iff it has no repeated roots in an algebraic closure (equivalently gcd(f,f')=1)."
aliases = ["separable-distinct-roots", "Separable polynomials have distinct roots"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/separable-distinct-roots.md"
+++

Let \(K\) be a [[algebra-rings/field|field]] and \(f(x)\in K[x]\) be nonzero. In an [[algebra-fields-galois/algebraic-closure|algebraic closure]] \(\overline K\), the following are equivalent:

1. \(f\) has **no repeated roots** in \(\overline K\), i.e. every root \(\alpha\in\overline K\) occurs with multiplicity \(1\).
2. \(\gcd(f,f')=1\) in \(K[x]\), where \(f'\) is the formal derivative.
3. In the [[algebra-fields-galois/splitting-field|splitting field]] \(L\) of \(f\) over \(K\), the polynomial \(f\) factors as a product of **distinct** linear factors.

When these conditions hold, \(f\) is called **separable**. In particular, an [[algebra-fields-galois/algebraic-element|algebraic element]] \(\alpha\) is [[algebra-fields-galois/separable-element|separable]] over \(K\) precisely when its minimal polynomial (over \(K\)) has distinct roots in \(\overline K\).

A useful characteristic-\(p\) test: if \(\mathrm{char}(K)=p>0\), then \(f'=0\) iff \(f(x)=g(x^p)\) for some \(g\in K[x]\); in that case \(f\) cannot be separable unless \(\deg(f)=1\).

### Examples

1. **Characteristic \(0\): always distinct for irreducibles.**
   Over \(\mathbb{Q}\), \(f(x)=x^3-2\) has derivative \(f'(x)=3x^2\), and \(\gcd(f,f')=1\), so its three complex roots are distinct in its [[algebra-fields-galois/splitting-field|splitting field]].

2. **A purely inseparable example.**
   Over \(K=\mathbb{F}_p(t)\), the polynomial \(f(x)=x^p-t\) satisfies \(f'(x)=px^{p-1}=0\). In \(\overline K\), it has a single root \(\alpha=t^{1/p}\) with multiplicity \(p\), so \(f\) is not separable and \(\alpha\) is not a [[algebra-fields-galois/separable-element|separable element]] over \(K\).

3. **A separable polynomial in characteristic \(p\).**
   Over \(K=\mathbb{F}_p\), \(f(x)=x^p-x\) has derivative \(f'(x)=-1\neq 0\), hence \(\gcd(f,f')=1\). It splits as \(\prod_{a\in \mathbb{F}_p}(x-a)\) with distinct roots (indeed it cuts out the prime field).
