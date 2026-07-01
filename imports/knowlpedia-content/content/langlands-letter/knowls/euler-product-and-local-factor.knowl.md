+++
id = "langlands-letter/knowls/euler-product-and-local-factor"
title = "Euler Product and Determinant Local $L$-Factor"
kind = "knowl"
summary = "An -function defined as at unramified primes"
aliases = ["euler-product-and-local-factor", "Euler Product and Determinant Local $L$-Factor"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/euler-product-and-local-factor.md"
+++

An **Euler product** is a product over primes (or places) of local factors, typically convergent for $\mathrm{Re}(s)\gg 0$.

In the letter, given a representation $\pi$ of the [[langlands-letter/knowls/l-group-satake-parameter|$L$-group]] and Satake parameters $\alpha_p$, the unramified local factor is
$
L_p(s)=\det\!\bigl(1-\pi(\alpha_p)\,p^{-s}\bigr)^{-1}.
$

The global $L$-function is $L(s)=\prod_p L_p(s)$, with finitely many "bad primes" omitted or modified.

**Key point:** changing auxiliary choices typically changes only finitely many local factors.
