---
title: "Sackur–Tetrode entropy (monatomic ideal gas)"
description: "Entropy of a dilute classical monatomic ideal gas including the quantum/indistinguishability constant: canonical and microcanonical forms."
---

This formula gives the {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}} of a *dilute* monatomic ideal gas (classical regime), and fixes the additive constant by incorporating the Gibbs $1/N!$ factor in the classical phase-space count.

Let $\lambda_T$ be the thermal wavelength
$$\lambda_T=\frac{h}{\sqrt{2\pi m k_B T}}.$$

## Statement (canonical form)
For a monatomic ideal gas of $N$ particles of mass $m$ in volume $V$ at temperature $T$ (with $n\lambda_T^3\ll 1$ for number density $n=N/V$),
$$
S(T,V,N)=N k_B\left[\ln\!\left(\frac{V}{N\lambda_T^3}\right)+\frac{5}{2}\right].
$$

This is consistent with the {{< knowl id="example-ideal-gas-classical" text="classical ideal-gas partition function computation" >}}.

## Statement (microcanonical form)
In terms of internal energy $U$ (see {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}),
$$
S(U,V,N)=N k_B\left[\ln\!\left(\frac{V}{N}\left(\frac{4\pi m U}{3N h^2}\right)^{3/2}\right)+\frac{5}{2}\right].
$$

## Context / derivation sketch
- Start from the canonical {{< knowl id="partition-function-canonical" section="stat-mech" text="partition function" >}} for the ideal-gas Hamiltonian and include the Gibbs factor $1/N!$ for indistinguishable particles:
  $$Z_N=\frac{1}{N!}\left(\frac{V}{\lambda_T^3}\right)^N.$$
- Use the canonical identity
  $$S = k_B\big(\log Z_N + \beta U\big), \qquad \beta=\frac{1}{k_B T},$$

  together with $U=(3/2)Nk_B T$.
- The $1/N!$ term is what resolves the classical Gibbs paradox and produces the $\ln(V/N)$ dependence rather than $\ln V$.

## Scope and limitations
- The condition $n\lambda_T^3\ll 1$ is the classical/dilute requirement; when it fails, quantum statistics become essential (see {{< knowl id="bose-einstein-condensation" text="Bose–Einstein condensation" >}} and {{< knowl id="degenerate-fermi-gas" text="degenerate Fermi gas" >}}).
- Interactions modify the entropy beyond the ideal-gas form (compare {{< knowl id="van-der-waals-gas" text="van der Waals gas" >}}).
