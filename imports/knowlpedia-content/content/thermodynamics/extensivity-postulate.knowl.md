+++
id = "thermodynamics/extensivity-postulate"
title = "Extensivity postulate"
kind = "knowl"
summary = "Postulate that thermodynamic state functions scale linearly with system size (up to subextensive corrections) in the thermodynamic limit."
aliases = ["extensivity-postulate", "Extensivity postulate"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/extensivity-postulate.md"
+++

## Definition (and physical meaning)

The **extensivity postulate** asserts that macroscopic thermodynamics can be formulated so that the fundamental state description becomes *scale-invariant* under replication of the system. Concretely, in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] (where boundary effects are negligible compared with bulk), the thermodynamic [[thermodynamics/thermodynamic-entropy|entropy]] in the entropy representation can be taken to satisfy **homogeneity of degree one** in the extensive variables:
$$
S(\lambda E,\lambda V,\lambda N)=\lambda\,S(E,V,N)\qquad (\lambda>0),
$$

where $E$ is [[thermodynamics/internal-energy-thermo|internal energy]], $V$ is [[thermodynamics/volume-thermo|volume]], and $N$ is [[thermodynamics/particle-number|particle number]]. Equivalently, other thermodynamic potentials (with the appropriate choice of independent variables) become homogeneous in their extensive arguments.

**Physical interpretation:** if you make $\lambda$ independent copies of the same macroscopic state and combine them without introducing significant interfacial effects, bulk properties “scale with size.” This is the content behind calling $E,V,N,S$ [[thermodynamics/extensive-variable|extensive variables]].

## Key consequences and relations

- **Intensive variables are scale-invariant.** If $S(E,V,N)$ is homogeneous of degree one, then derived [[thermodynamics/intensive-variable|intensive variables]] like [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], and [[thermodynamics/chemical-potential-thermo|chemical potential]] are homogeneous of degree zero (they do not change under uniform scaling of $E,V,N$).

- **Euler relation and Gibbs–Duhem.** Homogeneity (a [[thermodynamics/homogeneous-function-degree-one|homogeneous function of degree one]] property) implies the [[thermodynamics/euler-relation-thermodynamics|Euler relation]]. In the entropy representation (with only $pV$ work),
  $$
  S=\frac{1}{T}E+\frac{p}{T}V-\frac{\mu}{T}N,
  $$
  and in the energy representation,
  $$
  E=TS-pV+\mu N.
  $$

  Differentiating Euler’s relation yields the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]], constraining how $T,p,\mu$ can vary.

- **Connection to additivity.** Extensivity is typically justified by (approximate) [[thermodynamics/additivity-postulate|additivity]] together with negligible interfacial/boundary contributions in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]].

## When it can fail (usefully to remember)

Extensivity can break down when boundary or long-range interaction contributions remain comparable to bulk terms (e.g., strong surface effects, unscreened long-range forces, or constraints that prevent decomposition into weakly interacting parts). In such cases, thermodynamic potentials may acquire non-negligible subextensive terms, and the usual Euler/Gibbs–Duhem structure must be modified.
