---
title: "Hydrodynamic Limit Theorem"
description: "Convergence of the empirical density of an interacting particle system (Markov dynamics) to a deterministic PDE under macroscopic scaling, exemplified by exclusion processes."
---

## Prerequisites

- {{< knowl id="master-equation" text="master equation" >}}
- {{< knowl id="markov-semigroup-continuous" text="continuous-time Markov semigroups" >}}
- {{< knowl id="probability-measure" section="probability" text="probability measures" >}}
- {{< knowl id="expectation" section="probability" text="expectation" >}}
- {{< knowl id="nonequilibrium-steady-state" text="nonequilibrium steady states" >}}
- {{< knowl id="donsker-varadhan-ldp" text="Donsker–Varadhan LDP" >}}

## Empirical density field

Let $(\eta_t)_{t\ge 0}$ be a conservative interacting particle system on a discrete torus $\mathbb{T}_N^d=(\mathbb{Z}/N\mathbb{Z})^d$ with Markov generator $L_N$ (described by a {{< knowl id="master-equation" text="master equation" >}} / {{< knowl id="markov-semigroup-continuous" text="Markov semigroup" >}}).

A standard macroscopic observable is the empirical measure (density field)
$$
\pi_t^N(du)
={}
\frac{1}{N^d}\sum_{x\in\mathbb{T}_N^d}\eta_t(x)\,\delta_{x/N}(du),
$$

viewed as a random measure on the continuum torus $\mathbb{T}^d$.
Equivalently, for a smooth test function $G$,
$$
\langle \pi_t^N, G\rangle
={}
\frac{1}{N^d}\sum_{x\in\mathbb{T}_N^d}\eta_t(x)\,G(x/N).
$$

## Theorem (hydrodynamic limit, typical form)

Fix a macroscopic time scale and a macroscopic initial profile $\rho_0:\mathbb{T}^d\to[0,1]$.
Assume the initial distributions of $\eta_0$ are “associated” to $\rho_0$ in the sense that $\pi_0^N$ converges (in probability) to $\rho_0(u)\,du$.

Then, under an appropriate scaling of time (diffusive or hyperbolic, depending on the model), the path $(\pi_t^N)_{t\in[0,T]}$ converges in probability to a deterministic trajectory $\rho(t,u)\,du$, where $\rho$ solves a macroscopic PDE of conservation/diffusion type.

## Example: symmetric simple exclusion process (SSEP)

For SSEP, the natural scaling is **diffusive**: observe the process at times $tN^2$.
The hydrodynamic limit states that $\rho(t,u)$ solves the heat equation on $\mathbb{T}^d$:
$$
\partial_t \rho(t,u) = \Delta \rho(t,u),
\qquad
\rho(0,u)=\rho_0(u).
$$

## Example: asymmetric exclusion (ASEP, 1D)

For ASEP with nonzero drift, the natural scaling is often **hyperbolic**: observe at times $tN$.
In one dimension, the limiting density typically solves a scalar conservation law (inviscid Burgers type):
$$
\partial_t \rho(t,u) + \partial_u\big(\rho(t,u)(1-\rho(t,u))\big)=0,
\qquad
\rho(0,u)=\rho_0(u),
$$
under appropriate entropy-solution interpretation.

## What “hydrodynamic limit” encodes

- **Law of large numbers at the macroscopic scale**: fluctuations vanish after scaling, yielding deterministic PDE behavior.
- **Local equilibrium principle**: microscopic configurations near a macroscopic point behave approximately like equilibrium Gibbs measures at the local density.
- **Connection to dynamical large deviations**: hydrodynamic limits are often paired with path-space LDPs; the time-averaged DV theory ({{< knowl id="donsker-varadhan-ldp" text="Donsker–Varadhan" >}}) is one cornerstone in this direction.

