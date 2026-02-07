---
title: "Gibbs' inequality (lemma)"
description: "Relative entropy (KL divergence) is nonnegative: D(P‖Q) ≥ 0, with equality iff P = Q (a.s.)."
---

## Definitions and notation

- {{< knowl id="probability-measure" section="probability" text="Probability measures" >}}, {{< knowl id="expectation" section="probability" text="expectation" >}}.
- {{< knowl id="relative-entropy-kl-divergence" section="probability" text="Relative entropy (KL divergence)" >}}.
- {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}} (for the cross-entropy interpretation).

## Statement

Let $P$ and $Q$ be probability measures on the same measurable space $(\Omega,\mathcal F)$ with $P \ll Q$ (absolute continuity). Let $f=\frac{dP}{dQ}$ be the Radon–Nikodym derivative. Then the relative entropy satisfies
$$
D(P\|Q) \;=\; \int_\Omega \log\!\Big(\frac{dP}{dQ}\Big)\,dP \;\ge\; 0.
$$

Moreover, $D(P\|Q)=0$ if and only if $P=Q$ (equivalently, $f=1$ $Q$-a.s.).

In the discrete case, for probability vectors $(p_i)_i$ and $(q_i)_i$ with $p_i>0 \Rightarrow q_i>0$,
$$
\sum_i p_i \log\frac{p_i}{q_i} \ge 0,
$$

with equality iff $p_i=q_i$ for all $i$.

## Key hypotheses and conclusions

**Hypotheses**
- $P$ and $Q$ are probability measures on the same space.
- Absolute continuity $P\ll Q$ (so $\frac{dP}{dQ}$ exists).
- Integrability of $\log\!\big(\frac{dP}{dQ}\big)$ under $P$ (automatic in many finite/discrete settings).

**Conclusions**
- Nonnegativity: $D(P\|Q)\ge 0$.
- Rigidity of equality: $D(P\|Q)=0$ iff the two measures coincide.

In statistical mechanics, Gibbs’ inequality underlies “maximum entropy” and free-energy variational principles; it is a measure-theoretic form of the statement that the Gibbs distribution minimizes free energy (or equivalently maximizes entropy subject to constraints).
