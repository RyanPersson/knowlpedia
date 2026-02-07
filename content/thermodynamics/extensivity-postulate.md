---
title: "Extensivity postulate"
description: "Postulate that thermodynamic state functions scale linearly with system size (up to subextensive corrections) in the thermodynamic limit."
---

## Definition (and physical meaning)

The **extensivity postulate** asserts that macroscopic thermodynamics can be formulated so that the fundamental state description becomes *scale-invariant* under replication of the system. Concretely, in the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}} (where boundary effects are negligible compared with bulk), the thermodynamic {{< knowl id="thermodynamic-entropy" text="entropy" >}} in the entropy representation can be taken to satisfy **homogeneity of degree one** in the extensive variables:
$$
S(\lambda E,\lambda V,\lambda N)=\lambda\,S(E,V,N)\qquad (\lambda>0),
$$

where $E$ is {{< knowl id="internal-energy-thermo" text="internal energy" >}}, $V$ is {{< knowl id="volume-thermo" text="volume" >}}, and $N$ is {{< knowl id="particle-number" text="particle number" >}}. Equivalently, other thermodynamic potentials (with the appropriate choice of independent variables) become homogeneous in their extensive arguments.

**Physical interpretation:** if you make $\lambda$ independent copies of the same macroscopic state and combine them without introducing significant interfacial effects, bulk properties “scale with size.” This is the content behind calling $E,V,N,S$ {{< knowl id="extensive-variable" text="extensive variables" >}}.

## Key consequences and relations

- **Intensive variables are scale-invariant.** If $S(E,V,N)$ is homogeneous of degree one, then derived {{< knowl id="intensive-variable" text="intensive variables" >}} like {{< knowl id="temperature-thermo" text="temperature" >}}, {{< knowl id="pressure-thermo" text="pressure" >}}, and {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} are homogeneous of degree zero (they do not change under uniform scaling of $E,V,N$).

- **Euler relation and Gibbs–Duhem.** Homogeneity (a {{< knowl id="homogeneous-function-degree-one" text="homogeneous function of degree one" >}} property) implies the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}}. In the entropy representation (with only $pV$ work),
  $$
  S=\frac{1}{T}E+\frac{p}{T}V-\frac{\mu}{T}N,
  $$
  and in the energy representation,
  $$
  E=TS-pV+\mu N.
  $$

  Differentiating Euler’s relation yields the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}, constraining how $T,p,\mu$ can vary.

- **Connection to additivity.** Extensivity is typically justified by (approximate) {{< knowl id="additivity-postulate" text="additivity" >}} together with negligible interfacial/boundary contributions in the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}}.

## When it can fail (usefully to remember)

Extensivity can break down when boundary or long-range interaction contributions remain comparable to bulk terms (e.g., strong surface effects, unscreened long-range forces, or constraints that prevent decomposition into weakly interacting parts). In such cases, thermodynamic potentials may acquire non-negligible subextensive terms, and the usual Euler/Gibbs–Duhem structure must be modified.
