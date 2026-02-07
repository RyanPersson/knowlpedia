---
title: "Natural logarithm convention"
description: "In thermodynamics and statistical mechanics, log typically means the natural logarithm."
---

A common convention in thermodynamics and statistical mechanics is that \(\log\) means the **natural logarithm**:
$$
\log x \equiv \ln x,
$$
unless another base is explicitly stated.

### Where it appears
This convention is built into standard formulas such as:
- **Boltzmann entropy:**
  $$
  S = k_B \ln \Omega,
  $$
  where \(\Omega\) is a count (or suitably normalized measure) of accessible microstates.
- **Helmholtz free energy (canonical ensemble):**
  $$
  F = -k_B T \ln Z,
  $$
  where \(Z\) is the partition function.
- **Free energy density in the thermodynamic limit:**
  $$
  f = -\frac{1}{\beta}\lim \frac{1}{|\Lambda|}\ln Z_\Lambda,
  \quad \beta = \frac{1}{k_B T}.
  $$
  (See {{< knowl id="thermodynamic-limit-convention" text="thermodynamic limit convention" >}}.)

### Why natural logs are the default
Changing the logarithm base rescales results by a constant factor:
$$
\log_b x = \frac{\ln x}{\ln b}.
$$
If one insisted on base \(b\), formulas like \(S=k_B\log_b\Omega\) would amount to replacing \(k_B\) by \(k_B/\ln b\). Using \(\ln\) keeps the usual physical value and units conventions for \(k_B\) without extra conversion factors.

(When comparing with information theory, note that entropies may be measured in "bits" using base \(2\); the conversion is a constant factor.)
