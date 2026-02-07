---
title: "Center of a simple Lie algebra is trivial"
description: "A simple Lie algebra has zero center, since the center is always an ideal."
---

Let $\mathfrak g$ be a {{< knowl id="simple-lie-algebra" text="simple Lie algebra" >}}. Then its center is trivial:
\[
Z(\mathfrak g)=\{0\},
\]
where $Z(\mathfrak g)$ denotes the {{< knowl id="center-of-a-lie-algebra" text="center of a Lie algebra" >}}.

**Reason.** The center $Z(\mathfrak g)=\{z\in\mathfrak g:[z,x]=0\ \forall x\in\mathfrak g\}$ is always an ideal: if $z$ commutes with everything, then so does $[x,z]=0$ for any $x$, and invariance under brackets is automatic (this is a special case of the general “invariance under adjoint action” viewpoint). Since $\mathfrak g$ is simple, $Z(\mathfrak g)$ must be either $0$ or all of $\mathfrak g$. If $Z(\mathfrak g)=\mathfrak g$, then $\mathfrak g$ is abelian, contradicting the definition of simple.

This fact is often used when comparing simplicity to semisimplicity (see {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebra" >}}) and when analyzing the kernel of adjoint representations (compare {{< knowl id="kernel-of-ad-is-center-lemma" text="kernel of ad is the center" >}}).
