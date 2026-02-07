---
title: "Higher derivatives"
description: "Derivatives of order two and higher, defined iteratively."
---

A **higher derivative** of a function $f$ is a derivative of order $n\ge 2$, defined recursively by $f^{(0)}=f$, $f^{(1)}=f'$, and $f^{(n)}=(f^{(n-1)})'$ wherever the {{< knowl id="derivative" text="derivative" >}} exists.

Higher derivatives quantify finer local behavior and are central in approximation results such as {{< knowl id="taylors-theorem-with-remainder" text="Taylor's theorem with remainder" >}}. They also determine smoothness classes such as {{< knowl id="class-ck-function" text="class C^k functions" >}}.

**Examples:**
- For $f(x)=e^x$, one has $f^{(n)}(x)=e^x$ for every $n\ge 0$.
- For $f(x)=x^m$ (a polynomial), $f^{(n)}\equiv 0$ for all $n>m$.
