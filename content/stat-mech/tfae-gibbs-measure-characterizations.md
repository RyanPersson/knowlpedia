---
title: "TFAE: Characterizations of Gibbs Measures"
description: "Equivalent definitions of infinite-volume Gibbs measures via DLR equations, specifications, thermodynamic limits, and the variational principle."
---

Let the configuration space be $\Omega$ (e.g. spins on $\mathbb{Z}^d$) and fix an interaction / {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}} (finite-range or summable, as needed). A probability measure $\mu$ on $\Omega$ (see {{< knowl id="probability-measure" section="probability" text="probability measure" >}}) is an **infinite-volume Gibbs measure** for this interaction (see {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}}) if and only if any (hence all) of the following equivalent conditions hold.

1. **DLR (Dobrushin–Lanford–Ruelle) equations.**  
   For every finite region $\Lambda$ and every bounded local observable $f$ depending only on spins in $\Lambda$,
   $$
   \mathbb{E}_\mu[f \mid \mathcal{F}_{\Lambda^c}](\omega)
   \;=\;
   \int f(\sigma_\Lambda \omega_{\Lambda^c})\,\gamma_\Lambda(d\sigma_\Lambda \mid \omega_{\Lambda^c}),
   $$

   where $\gamma_\Lambda(\cdot \mid \omega_{\Lambda^c})$ is the finite-volume Gibbs kernel determined by the interaction and the outside configuration.  
   This is precisely the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}} characterization.

2. **Consistency with a Gibbs specification.**  
   There exists a consistent family of conditional distributions (a specification) $\{\gamma_\Lambda\}_\Lambda$ coming from the interaction such that $\mu$ is consistent with it:
   $$
   \mu \gamma_\Lambda = \mu \quad \text{for all finite } \Lambda.
   $$

   (Here $\mu\gamma_\Lambda$ denotes “update $\mu$ inside $\Lambda$ using the kernel $\gamma_\Lambda$ while keeping the outside fixed.”)

3. **Thermodynamic limit of finite-volume Gibbs measures.**  
   There exists a sequence of volumes $\Lambda_n \uparrow \mathbb{Z}^d$ and boundary conditions $\eta^{(n)}$ such that
   $$
   \mu = \lim_{n\to\infty} \mu_{\Lambda_n}^{\eta^{(n)}},
   $$

   where $\mu_{\Lambda}^{\eta}$ is the {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}} in $\Lambda$ with boundary condition $\eta$ (limit in the weak topology).  
   Any such limit point is a Gibbs measure, and every Gibbs measure arises as such a limit point (for standard interaction classes).

4. **Gibbs variational principle (equilibrium state).**  
   Among translation-invariant probability measures $\nu$ (when translation invariance is part of the setup), $\mu$ maximizes the functional
   $$
   \nu \mapsto h(\nu) - \beta e(\nu),
   $$

   where $h(\nu)$ is the entropy density (Shannon/Gibbs entropy rate) and $e(\nu)$ is the energy density induced by the interaction.  
   Equivalently, $\mu$ minimizes the appropriate free-energy density (see {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}).  
   This characterization is often expressed in terms of relative entropy density (see {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}}) with respect to a reference specification.

5. **Quasilocal conditional probabilities (Gibbsianity).**  
   The conditional distributions of $\mu$ in finite volumes depend on the outside configuration in a quasilocal (continuous) way and coincide with the interaction-defined kernels $\gamma_\Lambda(\cdot\mid\omega_{\Lambda^c})$.  
   This is the “regularity + DLR” form of being Gibbs.

Prerequisites and context: {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}, {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equations" >}}, {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}, {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonians" >}}, {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}}.
