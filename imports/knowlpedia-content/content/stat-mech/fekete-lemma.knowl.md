+++
id = "stat-mech/fekete-lemma"
title = "Fekete’s lemma"
kind = "knowl"
summary = "For subadditive (or superadditive) sequences, the limit a_n/n exists and equals the infimum (or supremum); central for thermodynamic limits via (super/sub)additivity."
aliases = ["fekete-lemma", "Fekete’s lemma"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/fekete-lemma.md"
+++

## Statement (subadditive form)
Let $(a_n)_{n\ge 1}$ be a real sequence satisfying **subadditivity**
$$
a_{m+n}\le a_m+a_n\qquad\text{for all }m,n\ge 1.
$$
Then the limit
$$
\lim_{n\to\infty}\frac{a_n}{n}
$$

exists (possibly as $-\infty$ if one allows extended reals), and in the real-valued case it satisfies
$$
\lim_{n\to\infty}\frac{a_n}{n}=\inf_{n\ge 1}\frac{a_n}{n}.
$$

## Statement (superadditive form)
If instead $(b_n)_{n\ge 1}$ is **superadditive**,
$$
b_{m+n}\ge b_m+b_n\qquad\text{for all }m,n\ge 1,
$$
then
$$
\lim_{n\to\infty}\frac{b_n}{n}=\sup_{n\ge 1}\frac{b_n}{n}.
$$

## Key hypotheses
- A sequence $(a_n)$ (or $(b_n)$) indexed by $n\ge 1$.
- Subadditivity $a_{m+n}\le a_m+a_n$ (or superadditivity $b_{m+n}\ge b_m+b_n$) for all $m,n$.

## Key conclusions
- The “specific value” $a_n/n$ has a well-defined asymptotic limit under subadditivity, computable as an infimum.
- The analogous “specific value” $b_n/n$ has a limit under superadditivity, computable as a supremum.

Thermodynamic significance: Fekete’s lemma is the standard mechanism behind existence of thermodynamic limits derived from [[thermodynamics/subadditivity-partition-function|subadditivity of log partition functions]] and [[thermodynamics/superadditivity-entropy|superadditivity of entropy]]. Concretely, it underpins results like [[thermodynamics/thermodynamic-limit-pressure-existence|existence of the thermodynamic-limit pressure]], where $a_n$ is typically (minus) $\log Z$ for a finite system and the limit defines the intensive [[stat-mech-lattice/pressure-lattice|pressure]] (or free-energy density).
