+++
id = "shale-paper/wiener-transform"
title = "Wiener Transform W"
kind = "knowl"
summary = "A unitary transform on Gaussian L₂ intertwining T with T^{*-1}"
aliases = ["wiener-transform", "Wiener Transform W"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/wiener-transform.md"
+++

The **Wiener transform** \(W\) is a unitary on \(L_2(M,n)\) defined (on polynomials) by
\[
(Wf)(x)=\int f(\sqrt2\,y+i x)\,dn(y).
\]

**Key property (paper use):**
- Intertwining (Cor. 3.1.1): \(W\,\mathfrak U(T)\,W^{-1}=\mathfrak U(T^{*-1})\).
- In §4, this yields \(P(x)=WQ(x)W^{-1}\) for the Fock-Cook field operators.

**Example:** In 1D, under an explicit unitary identification, \(W\) becomes the Fourier transform.
