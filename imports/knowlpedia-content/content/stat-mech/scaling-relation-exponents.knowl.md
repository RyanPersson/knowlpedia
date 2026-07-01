+++
id = "stat-mech/scaling-relation-exponents"
title = "Scaling relations among critical exponents"
kind = "knowl"
summary = "Algebraic relations (Rushbrooke, Widom, Fisher, hyperscaling) among critical exponents under scaling hypotheses near criticality."
aliases = ["scaling-relation-exponents", "Scaling relations among critical exponents"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/scaling-relation-exponents.md"
+++

**Scaling relations** are constraints among [[stat-mech/critical-exponent|critical exponents]] that follow from the assumption that near criticality there is a single diverging length scale and that the singular part of thermodynamics is approximately scale invariant.

## Scaling hypothesis (one common form)
Assume the singular free energy density satisfies a homogeneity relation
$$
f_s(t,h)=b^{-d}\, f_s(b^{y_t}t,\, b^{y_h}h)
$$

for any scale factor $b>0$, with relevant exponents $y_t,y_h$. This perspective is naturally produced by a [[stat-mech/renormalization-group-transformation|renormalization-group transformation]].

Equivalently, one often writes a reduced scaling form
$$
f_s(t,h)=|t|^{2-\alpha}\,\Phi_\pm\!\left(\frac{h}{|t|^\Delta}\right)
$$

for some scaling function $\Phi_\pm$ and gap exponent $\Delta$.

## Core scaling relations (common set)
These relations are expected to hold in many systems at a continuous transition:

### Widom relation
$$
\gamma=\beta(\delta-1).
$$

### Rushbrooke relation
$$
\alpha+2\beta+\gamma=2.
$$

### Fisher relation (links correlations to susceptibility)
$$
\gamma=\nu(2-\eta).
$$

This uses the definition of $\eta$ from the critical decay of the two-point [[stat-mech/correlation-function-two-point|correlation function]] and the divergence of the [[stat-mech/correlation-length|correlation length]].

### Josephson / hyperscaling relation (dimension-dependent)
$$
2-\alpha=d\,\nu.
$$
This relation can fail when hyperscaling is violated (for instance, above an upper critical dimension, or when dangerous irrelevant variables are present).

## Useful derived consequences
Combining Fisher + hyperscaling with standard definitions yields
$$
\beta=\frac{\nu}{2}\,(d-2+\eta),
$$
under the same set of assumptions.

## Prerequisites
- [[stat-mech/critical-exponent|definitions of critical exponents]]
- [[stat-mech/critical-point-phase-diagram|critical points]]
- [[stat-mech/rg-fixed-point|RG fixed points]]
