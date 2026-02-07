---
title: "Constructing the grand canonical partition function"
description: "Definition of the grand partition function as a weighted sum over particle numbers, normalizing the grand canonical ensemble."
---

The grand canonical ensemble is used when a system can exchange particles with a reservoir, so the particle number fluctuates while temperature $T$, volume $V$, and chemical potential $\mu$ are fixed (see {{< knowl id="grand-canonical-ensemble" text="grand canonical ensemble" >}} and {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}). Its normalization constant is the **grand partition function**.

## Definition (classical/abstract formulation)

Let $Z_N(\beta,V)$ be the {{< knowl id="construction-canonical-partition-function" text="canonical partition function" >}} at fixed $N$. The grand partition function is
$$
\Xi(\beta,\mu,V) \;=\; \sum_{N=0}^\infty e^{\beta\mu N}\, Z_N(\beta,V),
$$
whenever the series converges.

It is common to introduce the **fugacity** $z = e^{\beta\mu}$, so the same definition reads
$$
\Xi(\beta,\mu,V) \;=\; \sum_{N=0}^\infty z^{N}\, Z_N(\beta,V).
$$

The corresponding grand canonical probability measure on the disjoint union of $N$-particle phase spaces is obtained by weighting each $N$ sector by $e^{\beta\mu N}$ and normalizing by $\Xi$. Expectations with respect to this measure are again {{< knowl id="ensemble-average" text="ensemble averages" >}}, now including fluctuations of $N$.

## Quantum version (trace with number operator)

For a quantum system with Hamiltonian $\hat H$ and particle number operator $\hat N$,
$$
\Xi(\beta,\mu,V) \;=\; \mathrm{Tr}\, e^{-\beta(\hat H - \mu \hat N)}.
$$

This makes explicit that the reservoir control parameter $\mu$ couples to $\hat N$ in the same way that external fields couple linearly to their conjugate observables.

## Link to thermodynamic potentials

The grand partition function encodes the grand potential via the construction {{< knowl id="construction-free-energy-from-partition" text="grand potential from a partition function" >}}:
$$
\Omega(T,V,\mu) \;=\; -\frac{1}{\beta}\,\log \Xi(\beta,\mu,V).
$$

This statistical-mechanical $\Omega$ corresponds to the thermodynamic {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}} and is related to the Helmholtz free energy by the Legendre construction {{< knowl id="construction-legendre-f-to-omega" text="Legendre transform from $F$ to $\Omega$" >}}.

## Physical interpretation

- The factor $e^{\beta\mu N}$ rewards or suppresses sectors with different particle number, depending on $\mu$; it implements exchange with a particle reservoir at chemical potential $\mu$.
- The sum over $N$ turns fixed-$N$ canonical physics into variable-$N$ grand canonical physics, and $\log \Xi$ acts as the generating function for particle-number statistics (see {{< knowl id="construction-observables-from-log-z" text="observables from derivatives of log-partition functions" >}}).
- In homogeneous equilibrium, $\Omega$ is typically proportional to $-V$, so $\Xi$ encodes the pressure through $\Omega = -pV$ (up to boundary corrections).
