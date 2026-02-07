---
title: "Probability space"
description: "A sample space with a sigma-algebra of events and a probability measure."
---

A **probability space** is a triple $(\Omega,\mathcal{F},\mathbb{P})$ where $\Omega$ is a {{< knowl id="set" section="shared-foundations" text="set" >}}, $\mathcal{F}$ is a {{< knowl id="sigma-algebra" section="measure-theory" text="sigma-algebra" >}} on $\Omega$, and $\mathbb{P}$ is a {{< knowl id="probability-measure" text="probability measure" >}} on $(\Omega,\mathcal{F})$.

Elements of $\mathcal{F}$ are the events whose {{< knowl id="event-probability" text="probabilities" >}} are evaluated by $\mathbb{P}$, and a {{< knowl id="random-variable" text="random variable" >}} is a measurable function defined on $(\Omega,\mathcal{F},\mathbb{P})$.

**Examples:**
- Fair coin toss: $\Omega=\{H,T\}$, $\mathcal{F}=2^\Omega$, and $\mathbb{P}(\{H\})=\mathbb{P}(\{T\})=1/2$.
- Uniform draw from $[0,1]$: $\Omega=[0,1]$, $\mathcal{F}$ is the Borel $\sigma$-algebra, and $\mathbb{P}(A)=\lambda(A)$ where $\lambda$ is {{< knowl id="lebesgue-measure" section="measure-theory" text="Lebesgue measure" >}}.
