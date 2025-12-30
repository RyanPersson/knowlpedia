---
title: "Algebra: Module Theory"
description: "Foundational definitions and theorems in module theory over rings."
build:
  list: local
---

This section collects definitions and results on modules over rings: submodules, quotient modules, homomorphisms, exact sequences, free and projective modules, tensor products, and structure theorems over principal ideal domains.

## Definitions

### Basic Structures
- {{< knowl id="module" text="Module (left/right)" >}}
- {{< knowl id="bimodule" text="Bimodule" >}}
- {{< knowl id="submodule" text="Submodule" >}}
- {{< knowl id="quotient-module" text="Quotient module" >}}

### Homomorphisms
- {{< knowl id="module-homomorphism" text="Module homomorphism" >}}
- {{< knowl id="kernel-module" text="Kernel" >}}
- {{< knowl id="image-module" text="Image" >}}
- {{< knowl id="cokernel-module" text="Cokernel" >}}

### Exact Sequences
- {{< knowl id="exact-sequence-modules" text="Exact sequence of modules" >}}
- {{< knowl id="short-exact-sequence" text="Short exact sequence" >}}
- {{< knowl id="split-exact-sequence" text="Split exact sequence" >}}

### Direct Constructions
- {{< knowl id="direct-sum-modules" text="Direct sum of modules" >}}
- {{< knowl id="direct-product-modules" text="Direct product of modules" >}}

### Generation and Bases
- {{< knowl id="cyclic-module" text="Cyclic module" >}}
- {{< knowl id="finitely-generated-module" text="Finitely generated module" >}}
- {{< knowl id="free-module" text="Free module" >}}
- {{< knowl id="basis-module" text="Basis (of a free module)" >}}
- {{< knowl id="rank-module" text="Rank (of a free module)" >}}

### Torsion
- {{< knowl id="torsion-element" text="Torsion element" >}}
- {{< knowl id="torsion-module" text="Torsion module" >}}
- {{< knowl id="torsion-free-module" text="Torsion-free module" >}}

### Annihilators
- {{< knowl id="annihilator-element" text="Annihilator of an element" >}}
- {{< knowl id="annihilator-module" text="Annihilator of a module" >}}

### Simple and Semisimple Modules
- {{< knowl id="simple-module" text="Simple module" >}}
- {{< knowl id="semisimple-module" text="Semisimple module" >}}

### Composition Series and Length
- {{< knowl id="composition-series-module" text="Composition series" >}}
- {{< knowl id="length-module" text="Length (Jordan-Holder length)" >}}

### Chain Conditions
- {{< knowl id="noetherian-module" text="Noetherian module" >}}
- {{< knowl id="artinian-module" text="Artinian module" >}}

### Projective, Injective, and Flat Modules
- {{< knowl id="projective-module" text="Projective module" >}}
- {{< knowl id="injective-module" text="Injective module" >}}
- {{< knowl id="flat-module" text="Flat module" >}}

### Tensor Products
- {{< knowl id="tensor-product" text="Tensor product of modules" >}}
- {{< knowl id="bilinear-map" text="Bilinear map" >}}
- {{< knowl id="tensor-product-universal-property" text="Universal property of tensor product" >}}

### Hom and Duality
- {{< knowl id="hom-module" text="Hom module" >}}
- {{< knowl id="dual-module" text="Dual module" >}}
- {{< knowl id="tensor-hom-adjunction" text="Tensor-Hom adjunction data" >}}

### Algebras
- {{< knowl id="algebra-over-ring" text="Algebra over a commutative ring" >}}
- {{< knowl id="algebra-homomorphism" text="Algebra homomorphism" >}}
- {{< knowl id="tensor-product-algebras" text="Tensor product of algebras" >}}

### Graded and Filtered Structures
- {{< knowl id="graded-ring" text="Graded ring" >}}
- {{< knowl id="graded-module" text="Graded module" >}}
- {{< knowl id="filtered-ring" text="Filtered ring" >}}
- {{< knowl id="associated-graded-ring" text="Associated graded ring" >}}

---

## Axioms

- {{< knowl id="module-axioms" text="Module axioms" >}}
- {{< knowl id="vector-space-axioms" text="Vector space axioms" >}}

---

## Theorems

### Isomorphism Theorems
- {{< knowl id="first-isomorphism-theorem-modules" text="First isomorphism theorem (modules)" >}}
- {{< knowl id="second-isomorphism-theorem-modules" text="Second isomorphism theorem (modules)" >}}
- {{< knowl id="third-isomorphism-theorem-modules" text="Third isomorphism theorem (modules)" >}}
- {{< knowl id="correspondence-theorem-modules" text="Correspondence theorem (modules)" >}}

### Structure Theorems
- {{< knowl id="structure-theorem-pid" text="Structure theorem for f.g. modules over PID" >}}
- {{< knowl id="elementary-divisor-theorem" text="Elementary divisor theorem" >}}
- {{< knowl id="smith-normal-form-theorem" text="Smith normal form theorem" >}}
- {{< knowl id="rational-canonical-form-theorem" text="Rational canonical form theorem" >}}
- {{< knowl id="jordan-canonical-form-theorem" text="Jordan canonical form theorem" >}}
- {{< knowl id="krull-schmidt-azumaya-theorem" text="Krull-Schmidt-Azumaya theorem" >}}

---

## Lemmas

- {{< knowl id="splitting-lemma" text="Splitting lemma" >}}
- {{< knowl id="projective-ses-criterion" text="Projective iff every s.e.s. ending in it splits" >}}
- {{< knowl id="projective-summand-of-free" text="Projective is direct summand of free" >}}
- {{< knowl id="baers-criterion" text="Baer's criterion (injectivity)" >}}
- {{< knowl id="tensor-preserves-direct-sums" text="Tensor product preserves direct sums" >}}
- {{< knowl id="tensor-hom-adjunction-lemma" text="Tensor-Hom adjunction lemma" >}}
- {{< knowl id="quotient-module-universal-property" text="Universal property of quotient modules" >}}
- {{< knowl id="kernels-are-submodules" text="Kernels are submodules" >}}

---

## Propositions

- {{< knowl id="submodule-criterion" text="Submodule criterion" >}}
- {{< knowl id="kernel-image-submodules" text="Kernel and image are submodules" >}}
- {{< knowl id="first-isomorphism-consequence-modules" text="M/ker(f) ≅ im(f)" >}}
- {{< knowl id="exactness-via-kernels-images" text="Exactness via kernels and images" >}}
- {{< knowl id="direct-sum-universal-property" text="Direct sum universal property" >}}
- {{< knowl id="free-module-universal-property" text="Free module universal property" >}}
- {{< knowl id="tensor-product-universal-property-prop" text="Tensor product universal property" >}}
- {{< knowl id="tensor-commutes-with-sums" text="Tensor commutes with direct limits/sums" >}}
- {{< knowl id="hom-sums-to-products" text="Hom turns sums into products" >}}
- {{< knowl id="projective-implies-flat" text="Projective implies flat" >}}
- {{< knowl id="fg-projective-locally-free" text="f.g. projective are locally free" >}}
- {{< knowl id="semisimple-direct-summand" text="Semisimple iff every submodule is direct summand" >}}
- {{< knowl id="artinian-noetherian-finite-length" text="Artinian + Noetherian implies finite length" >}}

---

## Corollaries

- {{< knowl id="fg-torsion-free-pid-free" text="f.g. torsion-free over PID is free" >}}
- {{< knowl id="classification-fg-abelian-groups" text="Classification of f.g. abelian groups" >}}
- {{< knowl id="rcf-from-structure-theorem" text="Rational canonical form from structure theorem" >}}
- {{< knowl id="jcf-from-rcf" text="Jordan canonical form from RCF" >}}
- {{< knowl id="smith-normal-form-invariants" text="Smith normal form invariants" >}}
- {{< knowl id="chinese-remainder-modules" text="Chinese remainder for modules" >}}
