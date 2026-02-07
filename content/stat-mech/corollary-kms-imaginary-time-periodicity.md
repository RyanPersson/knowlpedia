---
title: "KMS imaginary-time periodicity"
description: "For a β-KMS equilibrium state, real-time correlation functions extend analytically to a complex-time strip and satisfy a β-periodicity (KMS boundary) relation in imaginary time."
---

## Statement

Let $(\mathcal A,\tau_t)$ be a quantum dynamical system (a $C^*$-algebra $\mathcal A$ with a strongly continuous one-parameter group of $*$-automorphisms $t\mapsto \tau_t$). Let $\omega$ be a $\beta$-KMS state at inverse temperature $\beta>0$ (see {{< knowl id="kms-condition-finite" section="stat-mech-quantum" text="KMS condition" >}}).

For any $\tau$-analytic observables $A,B\in\mathcal A$, the real-time two-point function
$F_{A,B}(t):=\omega\!\big(A\,\tau_t(B)\big)$, $t\in\mathbb R$,
admits an analytic continuation to the strip
$$
S_\beta:=\{z\in\mathbb C: 0<\operatorname{Im}z<\beta\},
$$

continuous on the closed strip $\overline{S_\beta}$, with boundary values
$$
F_{A,B}(t)=\omega\!\big(A\,\tau_t(B)\big),
\qquad
F_{A,B}(t+i\beta)=\omega\!\big(\tau_t(B)\,A\big)
\quad (t\in\mathbb R).
$$

Equivalently, whenever $\tau_{t+i\beta}(B)$ is defined (e.g. for $\tau$-analytic $B$),
$$
\omega\!\big(A\,\tau_{t+i\beta}(B)\big)=\omega\!\big(\tau_t(B)\,A\big),
\quad t\in\mathbb R.
$$

In particular (take $t=0$),
$$
\omega\!\big(A\,\tau_{i\beta}(B)\big)=\omega(BA),
$$

which is the imaginary-time “$\beta$-periodicity” relation (a shift by $i\beta$ in time corresponds to moving the second observable past the first).

## Key hypotheses

- $\beta>0$.
- $(\mathcal A,\tau_t)$ is a $C^*$-dynamical system.
- $\omega$ is a $\beta$-KMS state for $\tau_t$ ({{< knowl id="kms-condition-finite" section="stat-mech-quantum" text="KMS condition" >}}).
- $A,B$ belong to the $\tau$-analytic subalgebra (so $\tau_z(B)$ is meaningful for complex $z$ in the strip).

## Main conclusions

- **Analyticity in complex time:** $t\mapsto \omega(A\tau_t(B))$ extends to an analytic function on the strip $0<\operatorname{Im}z<\beta$.
- **Imaginary-time boundary relation:** the values on the upper boundary $\operatorname{Im}z=\beta$ match the lower boundary $\operatorname{Im}z=0$ after a cyclic permutation of operators:
  $$
  \omega(A\tau_{t+i\beta}(B))=\omega(\tau_t(B)A).
  $$

- **Endpoint condition at imaginary time $\beta$:** $\omega(A\tau_{i\beta}(B))=\omega(BA)$.

## Cross-links to definitions and context

- The equilibrium notion here is the {{< knowl id="kms-condition-finite" section="stat-mech-quantum" text="KMS condition" >}}.
- In finite quantum systems, the standard equilibrium state is the {{< knowl id="gibbs-state-quantum" section="stat-mech-quantum" text="quantum Gibbs state" >}} written via a {{< knowl id="density-operator" section="quantum-foundations" text="density operator" >}} and the {{< knowl id="quantum-partition-function" section="stat-mech-quantum" text="quantum partition function" >}}.
- The identification “Gibbs state $\Rightarrow$ KMS” is commonly packaged as {{< knowl id="gibbs-kms-theorem" text="Gibbs–KMS theorem" >}} (and converses as {{< knowl id="kms-gibbs-converse" text="KMS–Gibbs converse" >}} in settings where it holds).

## significance

**Finite-dimensional (Gibbs) case.**  
Let $H$ be the Hamiltonian and $\tau_t(B)=e^{itH}Be^{-itH}$. Let $\rho_\beta=e^{-\beta H}/Z_\beta$ be the Gibbs density operator ({{< knowl id="gibbs-state-quantum" section="stat-mech-quantum" text="Gibbs state" >}}), and define
$$
F_{A,B}(z)=\operatorname{Tr}\!\big(\rho_\beta\,A\,e^{izH}Be^{-izH}\big).
$$

Because $z\mapsto e^{izH}$ is entire, $F_{A,B}(z)$ is analytic in $z$. Evaluating at $z=t+i\beta$ and using $e^{i(t+i\beta)H}=e^{itH}e^{-\beta H}$ together with cyclicity of the trace gives the boundary identity
$$
F_{A,B}(t+i\beta)=\operatorname{Tr}\!\big(\rho_\beta\,e^{itH}Be^{-itH}\,A\big)=\omega(\tau_t(B)A),
$$
which is exactly the KMS imaginary-time periodicity.

**Why it matters.**  
This boundary relation is the conceptual basis of the *imaginary-time (Matsubara) formalism*: equilibrium correlation functions can be studied as analytic functions on a strip and, after Wick rotation, as functions on an imaginary-time circle of circumference $\beta$ (with the KMS cyclic permutation at the “cut”).
