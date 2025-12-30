---
title: "Wedderburn's little theorem"
description: "Every finite division ring is commutative, hence a field."
---

**Wedderburn's little theorem**: Every finite {{< knowl id="division-ring" text="division ring" >}} is commutative. Equivalently, every finite division ring is a {{< knowl id="field" text="field" >}}.

A standard approach studies the finite group \(D^\times\) of units, i.e. the {{< knowl id="group-of-units" text="group of units" >}}, and compares its conjugacy structure with the {{< knowl id="center-of-ring" text="center" >}} of the ring using the {{< knowl id="class-equation" text="class equation" >}}.

**Proof sketch**: Let \(D\) be finite with center \(Z\), so \(Z\) is a finite field. The conjugation action of \(D^\times\) on itself partitions \(D^\times\) into conjugacy classes whose sizes are indices of centralizers, and each centralizer is a \(Z\)-subalgebra. Counting conjugacy classes and exploiting that \(|Z^\times|\) divides centralizer sizes forces every element to commute with \(Z\) in a way that ultimately yields \([D:Z]=1\), hence \(D=Z\) is commutative.